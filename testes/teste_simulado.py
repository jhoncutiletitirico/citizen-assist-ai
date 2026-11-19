"""
teste_simulado.py - teste de uso SIMULADO do Citizen Assist AI

Não consegui fazer o teste com pessoas de fora no prazo, então simulei 4 perfis
de usuário. Cada perfil é uma sequência de teclas digitada no main.py de verdade:
o programa roda normal, grava o historico.json e o atendimentos.csv.
As perguntas foram escritas do jeito que um idoso ou um familiar costuma perguntar
(com erro de digitação, sem acento, palavras do dia a dia).

Como rodar (dentro da pasta citizen-assist-ai):  python testes/teste_simulado.py
Atenção: apaga o histórico anterior antes de começar.
"""

import json
import subprocess
import sys

# Cada perfil: (descrição, lista de entradas digitadas na ordem)
PERFIS = [
    ("Perfil 1 - senhora de 72 anos, usa pouco o computador", [
        "1",
        "como faço o cartao do sus", "s",
        "onde tomo a vacina da gripe?", "s",
        "0",
        "0", "4",                     # sair e nota 4
    ]),
    ("Perfil 2 - filha que cuida da mãe de 80 anos", [
        "1",
        "minha mae tem direito a remedio de graça?", "s",
        "sou aposentado preciso ir ao banco?",          # não encontra
        "0",
        "2", "1", "1", "s", "0", "0",                   # Assistência Social > BPC
        "0", "5",
    ]),
    ("Perfil 3 - senhor de 66 anos, digita devagar", [
        "abc",                                           # opção inválida
        "1",
        "idoso anda de onibus de graça?", "s",
        "meu cpf é 123.456.789-00",                      # recusada, não registra
        "quero desconto na conta de luz", "s",
        "0",
        "0", "3",
    ]),
    ("Perfil 4 - neto ajudando o avô de 68 anos", [
        "1",
        "como pedir o bpc pro meu avo", "s",
        "vaga de estacionamento pra idoso", "n",
        "recebi ligação pedindo senha do banco",         # não encontra
        "0",
        "2", "2", "3", "s", "0", "0",                   # Direitos e Previdência > fila prioritária
        "0", "5",
    ]),
]

# Começa do zero para o teste ficar só com estes atendimentos
with open("data/historico.json", "w", encoding="utf-8") as arquivo:
    json.dump({"atendimentos": [], "avaliacoes_facilidade": []}, arquivo, indent=2)

for descricao, teclas in PERFIS:
    print("=" * 60)
    print(descricao)
    entrada = "\n".join(teclas) + "\n"
    saida = subprocess.run([sys.executable, "main.py"], input=entrada, text=True,
                           capture_output=True, encoding="utf-8")
    if saida.returncode != 0:
        print("ERRO:", saida.stderr)
        break
    print("ok, sessão terminou normalmente")

with open("data/historico.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
print("=" * 60)
print(f"Total: {len(dados['atendimentos'])} atendimentos, notas {dados['avaliacoes_facilidade']}")
