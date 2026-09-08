import json, random, requests, os, urllib3
from collections import Counter
urllib3.disable_warnings() # Esconde aviso de segurança da caixa

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
ARQUIVO_DADOS = 'data.json'

def obter_ultimo_resultado():
    try:
        # Puxa direto do site da Caixa
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get("https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania/", headers=headers, verify=False, timeout=15)
        dados = response.json()
        return {"concurso": dados['numero'], "data": dados['dataApuracao'], "dezenas": [int(d) for d in dados['listaDezenas']]}
    except Exception as e:
        print("Erro na API da Caixa:", e)
        return None 

def carregar_dados():
    with open(ARQUIVO_DADOS, 'r') as f: return json.load(f)

def salvar_dados(dados):
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
    lin, col = [0]*10, [0]*10
    for n in palpite:
        lin[n//10]+=1; col[n%10]+=1
    if max(lin)>7 or max(col)>7: return False
    max_seq, seq_atual = 1, 1
    for i in range(1, 50):
        if palpite[i] == palpite[i-1]+1:
            seq_atual+=1
            if seq_atual > max_seq: max_seq = seq_atual
        else: seq_atual=1
    if max_seq >= 5: return False
    return True

def enviar_telegram(msg):
    # Print para o log do Github Actions
    print("Enviando para o Telegram...")
    res = requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={'chat_id': TELEGRAM_CHAT_ID, 'text': msg, 'parse_mode': 'Markdown'})
    print("Status Telegram:", res.status_code)

def executar():
    print("Iniciando robô...")
    dados = carregar_dados()
    novo = obter_ultimo_resultado()
    
    if novo and (not dados['concursos'] or dados['concursos'][0]['concurso'] != novo['concurso']):
        print(f"Novo concurso encontrado: {novo['concurso']}")
        dados['concursos'].insert(0, novo)
        if len(dados['concursos']) > 50: dados['concursos'].pop()
        for d in novo['dezenas']:
            if d in dados['ciclo_atual']: dados['ciclo_atual'].remove(d)
        if not dados['ciclo_atual']: dados['ciclo_atual'] = list(range(100))
        salvar_dados(dados)
    else:
         print("Nenhum concurso novo (ou erro na API). Gerando palpite mesmo assim...")

    pesos = calcular_pesos(dados)
    t, bilhete = 0, None
    while t < 500:
        c = gerar_palpite(pesos)
        if validar_bilhete(c): bilhete = c; break
        t+=1
        
    if not bilhete:
        print("Falha ao gerar o bilhete!")
        enviar_telegram("⚠️ *Alerta:* Falha ao gerar palpite em 500 tentativas."); return
        
    espelho = sorted(list(set(range(100)) - set(bilhete)))
    msg = f"🤖 *Lotomania - Palpite Inteligente*\n\n✅ *Principal:*\n`{' '.join(f'{n:02d}' for n in bilhete)}`\n\n🔄 *Espelho:*\n`{' '.join(f'{n:02d}' for n in espelho)}`"
    enviar_telegram(msg)
    print("Robô finalizado com sucesso!")

if __name__ == "__main__": executar()
