# ==========================================================
# LOTOMANIA PRO ARCHITECTURE - PROTECTED SYSTEM CORE
# ==========================================================
import base64 as _b

_b64_data = """
aW1wb3J0IGpzb24sIHJhbmRvbSwgcmVxdWVzdHMsIG9zLCB1cmxsaWIzCmZyb20gZGF0ZXRpbWUg
aW1wb3J0IGRhdGV0aW1lLCB0aW1lem9uZSwgdGltZWRlbHRhCmZyb20gY29sbGVjdGlvbnMgaW1w
b3J0IENvdW50ZXIKdXJybGliMy5kaXNhYmxlX3dhcm5pbmdzKCkKClRFTEVHUkFNX1RPS0VOID0g
b3MuZW52aXJvbi5nZXQoIlRFTEVHUkFNX1RPS0VOIikKVEVMRUdSQU1fQ0hBVF9JRCA9IG9zLmVu
dmlyb24uZ2V0KCJURUxFR1JBTV9DSEFUX0lEIikKQVJRVUlWT19EQURPUyA9ICdkYXRhLmpzb24n
CkxJTltfUEFJTkVMID0gImh0dHBzOi8vcmVuYXRvY29zdGE5My5naXRodWIuaW8vbG90b21hbmlh
LWJvdC8iCgpkZWYgb2J0ZXJfdWx0aW1vX3Jlc3VsdG8oKToKICAgIHRyeToKICAgICAgICBoZWFk
ZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wJ30KICAgICAgICB1cmwgPSAiaHR0cHM6
Ly9zZXJ2aWNlYnVzMi5jYWl4YS5nb3YuYnIvcG9ydGFsZGVsb3Rlcmlhcy9hcGkvbG90b21hbmlh
LyIKICAgICAgICByZXNwb25zZSA9IHJlcXVlc3RzLmdldCh1cmwsIGhlYWRlcnM9aGVhZGVycywg
dmVyaWZ5PUZhbHNlLCB0aW1lb3V0PTE1KQogICAgICAgIGRhZG9zID0gcmVzcG9uc2UuanNvbigp
CiAgICAgICAgZ2FuaGFkb3JlcyA9IDAKICAgICAgICByYXRlaW8gPSBkYWRvcy5nZXQoJ2xpc3Rh
UmF0ZWlvUHJlbWlvJykKICAgICAgICBpZiByYXRlaW8gYW5k ^^iXN0YW5jZW9mKHJhdGVpbywgbGlz
dCkgYW5kIGxlbihyYXRlaW8pID4gMDoKICAgICAgICAgICAgZ2FuaGFkb3JlcyA9IHJhdGVpby[0
].get\('numeroDeGanhadores', 0)\Wn        ZGF0YV9wcm94X3N0ciA9IGRhZG9zLmdldCgn
ZGF0YVByb3hpbW9Db25jdXJzbycsICdcdykKICAgICAgICBkaWFfc2VtYW5hX3Byb3ggPSAiIgog
ICAgICAgIGlmIGRhdGFfcHJveF9zdHI6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAg
IGRpYXMgPSBbInNlZ3VuZGEtZmVpcmEiLCAidGVyY3EtZmVpcmEiLCAicXVhcnRhLWZlaXJhIiwg
InF1aW50YS1mZWlyEiIsICJzZXh0YS1mZWlyEiIsICJzw6FiYWRvIiwgImRvbWluZ28iXQogICAg
ICAgICAgICAgICAgb2JqX2RhdGEgPSBkYXRldGltZS5zdHJwdGltZShkYXRhX3Byb3hfc3RyLCAi
JTgvJTkvJFlZWVkiKQogICAgICAgICAgICAgICAgZGlhX3NlbWFuYV9wcm94ID0gZGlhc1tvYmpf
ZGF0YS53ZWVrZGF5KCldCiAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgIHBhc3MK
ICAgICAgICByZXR1cm4gewogICAgICAgICAgICAiY29uY3Vyc28iOiBkYWRvc1snbnVtZXJvJ10s
CiAgICAgICAgICAgICJkYXRhIjogZGFkb3NbJ2RhdGFBcHVyYWNhbyddLAogICAgICAgICAgICAi
ZGV6ZW5zcyI6IHNvcnRlZChbaW50KGQpIGZvciBkIGluIGRhZG9zWydsaXN0YURlemVuYXMnXVks
CiAgICAgICAgICAgICJhY3VtdWxvdSI6IGRhZG9zLmdldCgnYWN1bXVsYWRvJywgRmFsc2UpLAog
ICAgICAgICAgICAiZ2FuaGFkb3JlcyI6IGdhbmhhZG9yZXMsCiAgICAgICAgICAgICJ2YWxvcl9w
cmVtaW8iOiBkYWRvcy5nZXQoJ3ZhbG9yRXN0aW1hZG9Qcm94aW1vQ29uY3Vyc28nLCAwKSwKICAg
ICAgICAgICAgImRhdGFfcHJveGltbyI6IGRhdGFfcHJveF9zdHIsCiAgICAgICAgICAgICJkaWFf
c2VtYW5hX3Byb3hpbW8iOiBkaWFfc2VtYW5hX3Byb3gKICAgICAgICB9CiAgICBleGNlcHQgRXhj
ZXB0aW9uIGFzIGU6CiAgICAgICAgcHJpbnQoIkVycm8gbmEgQVBJOiIsIGUpCiAgICAgICAgcmV0
dXJuIE5vbmUKCmRlZiBjYXJyZWdhcl9kYWRvcygpOgogICAgdHJ5OgogICAgICAgIHdpdGggb3Bl
bihBUlFVSVZPXkRBRE9TLCAncicpIGFzIGY6IHJldHVybiBqc29uLmxvYWQoZikKICAgIGV4Y2Vw
dDoKICAgICAgICByZXR1cm4geyJjb25jdXJzb3MiOiBbXSwgImNpY2xvX2F0dWFsIjogbGlzdChy
YW5nZSgxMDApKSwgImxhc3RfbWVzc2FnZV9pZCI6IE5vbmV9CgpkZWYgc2FsdmFyX2RhZG9zKGRh
ZG9zKToKICAgIGJydCA9IHRpbWV6b25lKHRpbWVkZWx0YShob3Vycz0tMykpCiAgICBkYWRvc1sn
dWx0aW1hX2F0dWFsaXphY2FvJ10gPSBkYXRldGltZS5ub3coYnJ0KS5zdHJmdGltZShnJCVkLyVt
LyVZ4AgwHMlSBzaCB%sIMiKQogICAgd2l0aCBvcGVuKEFSUVVJV19EQURPUywgJ3cnKSBhcyBmOiBj
c29uLmR1bXAoZGFkcywgZiwgaW5kZW50PTIpCgpkZWYgY2FsY3VsYXJfcGVzb3MoZGFkcyk6CiAg
ICBmcmVxID0gQ291bnRlcigpCiAgICBmb3IgY29uYyBpbiBkYWRvcyhbJ2NvbmN1cnNvcyddOiBm
cmVxLnVwZGF0ZShjb25jWydkZXplbmFzJ10pCiAgICBvcmRlbSA9IFtpdGVtWzBdIGZvciBpdGVt
IGluIGZyZXEubW9zdF9jb21tb24oKV0KICAgIGNpY2xvID0gZGFkcy5nZXQoJ2NpY2xvX2F0dWFs
JywgbGlzdChyYW5nZSgxMDApKSkKICAgIHBlc29zID0gW10KICAgIGZvciBpIGluIHJhbmdlKDEw
MCk6CiAgICAgICAgcGVzbz0gMgoJaWYgaSBpbiBvcmRlb[:15]: peso = 3\n        if i in or
dem[-15:]: peso = 1\n        if i in ciclo: peso = 5\n        pesos.append(peso)\n
    return pesos\n\ndef gerar_palpite(pesos):\n    pop, p_atuais = list(range(10
0)), pesos.copy()\n    palpite = []\n    for _ in range(50):\n        esc = random.c
hoices(pop, weights=p_atuais, k=1)[0]\n        palpite.append(esc)\n        idx = po
p.index(esc)\n        pop.pop(idx); p_atuais.pop(idx)\n    return sorted(palpite)\n
\ndef validar_bilhete(palpite):\n    if not (22 <= sum(1 for n in palpite if n % 2
 == 0) <= 28): return False\n    q1=q2=q3=q4=0\n    for n in palpite:\n        l, c
 = n//10, n%10\n        if l<5 and c<5: q1+=1\n        elif l<5 and c>=5: q2+=1\n   
     elif l>=5 and c<5: q3+=1\n        else: q4+=1\n    if any(q < 10 or q > 15 for
 q in [q1,q2,q3,q4]): return False\n    return True\n\ndef apagar_mensagem_anterior
(message_id):\n    if message_id:\n        url = f\"https://api.telegram.org/bot
{TELEGRAM_TOKEN}/deleteMessage\"\n        requests.post(url, json={'chat_id': TELE
GRAM_CHAT_ID, 'message_id': message_id})\n\ndef enviar_telegram(msg, dados):\n   
 url = f\"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage\"\n    res = req
uests.post(url, json={'chat_id': TELEGRAM_CHAT_ID, 'text': msg, 'parse_mode': 'Mark
down', 'disable_web_page_preview': True})\n    if res.status_code == 200:\n        n
ovo_id = res.json().get(\"result\", {}).get(\"message_id\")\n        if novo_id:\n 
           apagar_mensagem_anterior(dados.get(\"last_message_id\"))\n            d
ados[\"last_message_id\"] = novo_id\n\ndef formatar_moeda(valor):\n    try: return
 f\"R$ {float(valor):,.2f}\".replace(\",\", \"X\").replace(\".\", \",\").replace
(\"X\", \".\")\n    except: return \"R$ 0,00\"\n\ndef executar():\n    dados = carr
egar_dados()\n    novo = obter_ultimo_resultado()\n    if novo and (not dados['con
cursos'] or dados['concursos'][0]['concurso'] != novo['concurso']):\n        dados['
concursos'].insert(0, novo)\n        if len(dados['concursos']) > 50: dados['concurs
os'].pop()\n        for d in novo['dezenas']:\n            if d in dados['ciclo_atua
l']: dados['ciclo_atual'].remove(d)\n        if not dados['ciclo_atual']: dados['ci
clo_atual'] = list(range(100))\n    salvar_dados(dados)\n    if not dados['concurso
s']: return \n    ultimo_conc = dados['concursos'][0]\n    concurso_base = ultimo_c
onc['concurso']\n    data_sorteio = ultimo_conc['data']\n    ultimas_dezenas = ulti
mo_conc['dezenas']\n    ganhadores = ultimo_conc.get('ganhadores', 0)\n    premio =
 formatar_moeda(ultimo_conc.get('valor_premio', 0))\n    prox_concurso = int(concur
so_base) + 1\n    data_prox = ultimo_conc.get('data_proximo', 'Data Indefinida')\n 
   dia_semana = ultimo_conc.get('dia_semana_proximo', '')\n    str_data_prox = f\"{
data_prox}, {dia_semana}\" if dia_semana else data_prox\n    if ultimo_conc.get('a
cumulou'): status_premio = \"🚨 ACUMULOU!\"\n    else: status_premio = f\"🎉 {gan
hadores} Ganhador(es)\"\n    pesos = calcular_pesos(dados)\n    t, bilhete = 0, None\n
    while t < 500:\n        c = gerar_palpite(pesos)\n        if validar_bilhete(c
): bilhete = c; break\n        t+=1\n    if not bilhete: return enviar_telegram(\"
⚠️ *Alerta:* Falha ao gerar palpite.\", dados)\n    espelho = sorted(list(set(range(
100)) - set(bilhete)))\n    freq = Counter()\n    for conc in dados['concursos']: f
req.update(conc['dezenas'])\n    ordem = [item[0] for item in freq.most_common()]\n
    quente = ordem[0] if ordem else 0\n    fria = ordem[-1] if ordem else 0\n    str
_prin = ' '.join(f'{n:02d}' for n in bilhete)\n    str_esp = ' '.join(f'{n:02d}' for
 n in espelho)\n    str_ult = ' '.join(f'{n:02d}' for n in ultimas_dezenas)\n    msg
 = (f\"🍀 *Painel Lotomania Atualizado*\\n\"\n           f\"🔄 Última Atualização: 
{datetime.now(timezone(timedelta(hours=-3))).strftime('%d/%m/%Y às %H:%M')}\\n\\n\"
\n           f\"🏆 *Último Sorteio:* {concurso_base} ({data_sorteio})\\n\"\n       
    f\"🏆 *Dezenas:* {str_ult}\\n\"\n           f\"👤 *Ganhadores (20 pts):* {status
_premio}\\n\"\n           f\"💰 *Estimativa Próximo:* {premio}\\n\\n\"\n           f
\"🔮 *Próximo Sorteio:* {prox_concurso} ({str_data_prox})\\n\\n\"\n           f\"🤖
 *Análise do Assistente Preditivo:*\\n\"\n           f\"Aqui vai a minha leitura cru
zando as estatísticas dos 50 jogos:\\n\\n\"\n           f\"• *Para Fixar:* A dezen
a {quente:02d} está muito quente. A chance matemática dela continuar saindo hoje é a
ltíssima.\\n\"\n           f\"• *Para Evitar:* A dezena {fria:02d} atingiu seu limite
 de atraso (está fria demais). O algoritmo minimizou a chance dela.\\n\\n\"\n     
      f\"🎯 *Palpite Principal (50 Dezenas):*\\n`{str_prin}`\\n\\n\"\n           f\"
🛡️ *Aposta Espelho (50 Dezenas):*\\n`{str_esp}`\\n\"\n           f\"_(Gerado cruzan
do atrasos e balanceando quadrantes)_\\n\\n\"\n           f\"✅ *Base:* 50 Jogos\\n
\"\n           f\"🔗 *Seu Painel:* [Clique Aqui]({LINK_PAINEL})\\n\"\n           f\"
🏦 *Fonte Oficial:* Caixa Econômica\")\n    enviar_telegram(msg, dados)\n    salvar_d
ados(dados)\n\nif __name__ == "__main__": executar()\n
"""

exec(_b.b64decode(_b64_data.encode('utf-8')).decode('utf-8', errors='ignore'))
