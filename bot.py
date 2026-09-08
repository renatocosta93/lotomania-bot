import json, random, requests, os, urllib3
from datetime import datetime, timezone, timedelta
from collections import Counter
urllib3.disable_warnings()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
ARQUIVO_DADOS = 'data.json'
LINK_PAINEL = "https://renatocosta93.github.io/lotomania-bot/"

def obter_ultimo_resultado():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania/"
        response = requests.get(url, headers=headers, verify=False, timeout=15)
        dados = response.json()
        return {
            "concurso": dados['numero'],
            "data": dados['dataApuracao'],
            "dezenas": sorted([int(d) for d in dados['listaDezenas']]),
            "acumulou": dados.get('acumulado', False),
            "ganhadores": dados.get('quantidadeGanhadores', 0)
        }
    except Exception as e:
        print("Erro na API:", e)
        return None

def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r') as f: return json.load(f)
    except:
        return {"concursos": [], "ciclo_atual": list(range(100))}

def salvar_dados(dados):
    brt = timezone(timedelta(hours=-3))
    dados['ultima_atualizacao'] = datetime.now(brt).strftime("%d/%m/%Y às %H:%M:%S")
    with open(ARQUIVO_DADOS, 'w') as f: json.dump(dados, f, indent=2)

def calcular_pesos(dados):
    freq = Counter()
    for conc in dados['concursos']: freq.update(conc['dezenas'])
    ordem = [item[0] for item in freq.most_common()]
    ciclo = dados.get('ciclo_atual', list(range(100)))
    pesos = []
    for i in range(100):
        peso = 2 
        if i in ordem[:15]: peso = 3
        if i in ordem[-15:]: peso = 1
        if i in ciclo: peso = 5 
        pesos.append(peso)
    return pesos

def gerar_palpite(pesos):
    pop, p_atuais = list(range(100)), pesos.copy()
    palpite = []
    for _ in range(50):
        esc = random.choices(pop, weights=p_atuais, k=1)[0]
        palpite.append(esc)
        idx = pop.index(esc)
        pop.pop(idx); p_atuais.pop(idx)
    return sorted(palpite)

def validar_bilhete(palpite):
    if not (22 <= sum(1 for n in palpite if n % 2 == 0) <= 28): return False
    q1=q2=q3=q4=0
    for n in palpite:
        l, c = n//10, n%10
        if l<5 and c<5: q1+=1
        elif l<5 and c>=5: q2+=1
        elif l>=5 and c<5: q3+=1
        else: q4+=1
    if any(q < 10 or q > 15 for q in [q1,q2,q3,q4]): return False
    return True

def enviar_telegram(msg):
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                  json={'chat_id': TELEGRAM_CHAT_ID, 'text': msg, 'parse_mode': 'Markdown', 'disable_web_page_preview': True})

def executar():
    dados = carregar_dados()
    novo = obter_ultimo_resultado()
    
    concurso_base = "Desconhecido"
    
    if novo and (not dados['concursos'] or dados['concursos'][0]['concurso'] != novo['concurso']):
        dados['concursos'].insert(0, novo)
        if len(dados['concursos']) > 50: dados['concursos'].pop()
        for d in novo['dezenas']:
            if d in dados['ciclo_atual']: dados['ciclo_atual'].remove(d)
        if not dados['ciclo_atual']: dados['ciclo_atual'] = list(range(100))
        
    salvar_dados(dados)
    
    if dados['concursos']:
        concurso_base = dados['concursos'][0]['concurso']
        ultimas_dezenas = dados['concursos'][0]['dezenas']
    else:
        ultimas_dezenas = []

    pesos = calcular_pesos(dados)
    t, bilhete = 0, None
    while t < 500:
        c = gerar_palpite(pesos)
        if validar_bilhete(c): 
            bilhete = c; break
        t+=1

    if not bilhete:
        enviar_telegram("⚠️ *Alerta:* Falha ao gerar palpite seguro.")
        return

    espelho = sorted(list(set(range(100)) - set(bilhete)))
    
    pares = sum(1 for n in bilhete if n % 2 == 0)
    impares = 50 - pares
    repetidas = len(set(bilhete).intersection(set(ultimas_dezenas)))
    faltam_ciclo = len(dados.get('ciclo_atual', []))
    
    str_prin = ' '.join(f'{n:02d}' for n in bilhete)
    str_esp = ' '.join(f'{n:02d}' for n in espelho)

    msg = (f"🤖 *Lotomania Premium* - Base Conc. {concurso_base}\n\n"
           f"📊 *Análise do Palpite:*\n"
           f"• Pares: {pares} | Ímpares: {impares}\n"
           f"• Repetidas do último: {repetidas}\n"
           f"• Faltam pro Ciclo: {faltam_ciclo} dezenas\n\n"
           f"🎯 *Aposta Principal:*\n`{str_prin}`\n\n"
           f"🛡️ *Aposta Espelho:*\n`{str_esp}`\n\n"
           f"🌐 *Acesse o Painel Completo:*\n[Clique aqui para ver o Mapa de Calor]({LINK_PAINEL})")
    
    enviar_telegram(msg)

if __name__ == "__main__": executar()
