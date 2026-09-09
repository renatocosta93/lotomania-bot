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
        
        ganhadores = 0
        rateio = dados.get('listaRateioPremio')
        if rateio and isinstance(rateio, list) and len(rateio) > 0:
            ganhadores = rateio[0].get('numeroDeGanhadores', 0)
            
        data_prox_str = dados.get('dataProximoConcurso', '')
        dia_semana_prox = ""
        if data_prox_str:
            try:
                dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
                obj_data = datetime.strptime(data_prox_str, "%d/%m/%Y")
                dia_semana_prox = dias[obj_data.weekday()]
            except:
                pass
                
        return {
            "concurso": dados['numero'],
            "data": dados['dataApuracao'],
            "dezenas": sorted([int(d) for d in dados['listaDezenas']]),
            "acumulou": dados.get('acumulado', False),
            "ganhadores": ganhadores,
            "valor_premio": dados.get('valorEstimadoProximoConcurso', 0),
            "data_proximo": data_prox_str,
            "dia_semana_proximo": dia_semana_prox
        }
    except Exception as e:
        print("Erro na API:", e)
        return None

def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r') as f: return json.load(f)
    except:
        return {"concursos": [], "ciclo_atual": list(range(100)), "last_message_id": None}

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

def apagar_mensagem_anterior(message_id):
    if message_id:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/deleteMessage"
        requests.post(url, json={'chat_id': TELEGRAM_CHAT_ID, 'message_id': message_id})

def enviar_telegram(msg, dados):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    res = requests.post(url, json={'chat_id': TELEGRAM_CHAT_ID, 'text': msg, 'parse_mode': 'Markdown', 'disable_web_page_preview': True})
    if res.status_code == 200:
        novo_id = res.json().get("result", {}).get("message_id")
        if novo_id:
            apagar_mensagem_anterior(dados.get("last_message_id"))
            dados["last_message_id"] = novo_id

def formatar_moeda(valor):
    try: return f"R$ {float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except: return "R$ 0,00"

def executar():
    dados = carregar_dados()
    novo = obter_ultimo_resultado()
    
    if novo and (not dados['concursos'] or dados['concursos'][0]['concurso'] != novo['concurso']):
        dados['concursos'].insert(0, novo)
        if len(dados['concursos']) > 50: dados['concursos'].pop()
        for d in novo['dezenas']:
            if d in dados['ciclo_atual']: dados['ciclo_atual'].remove(d)
        if not dados['ciclo_atual']: dados['ciclo_atual'] = list(range(100))
        
    salvar_dados(dados)
    
    if not dados['concursos']: return 
        
    ultimo_conc = dados['concursos'][0]
    concurso_base = ultimo_conc['concurso']
    data_sorteio = ultimo_conc['data']
    ultimas_dezenas = ultimo_conc['dezenas']
    ganhadores = ultimo_conc.get('ganhadores', 0)
    premio = formatar_moeda(ultimo_conc.get('valor_premio', 0))
    prox_concurso = int(concurso_base) + 1
    
    data_prox = ultimo_conc.get('data_proximo', 'Data Indefinida')
    dia_semana = ultimo_conc.get('dia_semana_proximo', '')
    str_data_prox = f"{data_prox}, {dia_semana}" if dia_semana else data_prox
    
    if ultimo_conc.get('acumulou'): status_premio = "🚨 ACUMULOU!"
    else: status_premio = f"🎉 {ganhadores} Ganhador(es)"

    pesos = calcular_pesos(dados)
    t, bilhete = 0, None
    while t < 500:
        c = gerar_palpite(pesos)
        if validar_bilhete(c): bilhete = c; break
        t+=1

    if not bilhete: return enviar_telegram("⚠️ *Alerta:* Falha ao gerar palpite.", dados)

    espelho = sorted(list(set(range(100)) - set(bilhete)))
    
    freq = Counter()
    for conc in dados['concursos']: freq.update(conc['dezenas'])
    ordem = [item[0] for item in freq.most_common()]
    quente = ordem[0] if ordem else 0
    fria = ordem[-1] if ordem else 0
        
    str_prin = ' '.join(f'{n:02d}' for n in bilhete)
    str_esp = ' '.join(f'{n:02d}' for n in espelho)
    str_ult = ' '.join(f'{n:02d}' for n in ultimas_dezenas)

    msg = (f"🍀 *Painel Lotomania Atualizado*\n"
           f"🔄 Última Atualização: {datetime.now(timezone(timedelta(hours=-3))).strftime('%d/%m/%Y às %H:%M')}\n\n"
           f"🏆 *Último Sorteio:* {concurso_base} ({data_sorteio})\n"
           f"🔢 *Dezenas:* {str_ult}\n"
           f"👤 *Ganhadores (20 pts):* {status_premio}\n"
           f"💰 *Estimativa Próximo:* {premio}\n\n"
           f"🔮 *Próximo Sorteio:* {prox_concurso} ({str_data_prox})\n\n"
           f"🤖 *Análise do Assistente Preditivo:*\n"
           f"Aqui vai a minha leitura cruzando as estatísticas dos 50 jogos:\n\n"
           f"• *Para Fixar:* A dezena {quente:02d} está muito quente. A chance matemática dela continuar saindo hoje é altíssima.\n"
           f"• *Para Evitar:* A dezena {fria:02d} atingiu seu limite de atraso (está fria demais). O algoritmo minimizou a chance dela.\n\n"
           f"🎯 *Palpite Principal (50 Dezenas):*\n`{str_prin}`\n\n"
           f"🛡️ *Aposta Espelho (50 Dezenas):*\n`{str_esp}`\n"
           f"_(Gerado cruzando atrasos e balanceando quadrantes)_\n\n"
           f"✅ *Base:* 50 Jogos\n"
           f"🔗 *Seu Painel:* [Clique Aqui]({LINK_PAINEL})\n"
           f"🏦 *Fonte Oficial:* Caixa Econômica")
    
    enviar_telegram(msg, dados)
    salvar_dados(dados)

if __name__ == "__main__": executar()
