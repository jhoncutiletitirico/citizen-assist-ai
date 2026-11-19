"""
main.py - Citizen Assist AI (GS 2026.2 - Pensamento Computacional com Python)
Assistente de orientação para pessoas idosas (60+).

Jhon Cutile Titirico - RM 571976 - Turma 1CCPI

Como rodar (dentro da pasta citizen-assist-ai):  python main.py
"""

from assistente import Assistente, ler_opcao
from base_conhecimento import BaseConhecimento


def main():
    base = BaseConhecimento("data/base_conhecimento.json")
    if not base.carregar():
        print("Não foi possível abrir a base de conhecimento. Confira a pasta data/.")
        return

    assistente = Assistente("Citizen Assist AI", base)

    print("=" * 60)
    print(f"  {assistente.nome} - Orientação para pessoas idosas (60+)")
    print("=" * 60)
    print("Este assistente NÃO é canal oficial e NÃO pede seus dados pessoais.")
    print(f"Base carregada: {len(base.orientacoes)} orientações em "
          f"{len(base.categorias())} categorias.")

    while True:
        print("\n------------- MENU -------------")
        print(" 1 - Fazer uma pergunta")
        print(" 2 - Navegar por categorias")
        print(" 3 - Ver indicadores")
        print(" 4 - Exportar atendimentos (CSV)")
        print(" 0 - Sair")
        opcao = ler_opcao("Escolha uma opção: ", 0, 4)

        if opcao == 1:
            assistente.perguntar()
        elif opcao == 2:
            assistente.navegar()
        elif opcao == 3:
            assistente.indicadores()
        elif opcao == 4:
            assistente.exportar_csv()
        else:
            assistente.pedir_nota()
            assistente.exportar_csv()
            print("Até logo! Procure sempre os canais oficiais.")
            break


main()
