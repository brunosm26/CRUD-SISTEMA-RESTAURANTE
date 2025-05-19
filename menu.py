import json

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


def menu():
    print(cor.AMARELO + "╔════════════════════════════════════════════════════════════════════════════════╗")
    print(cor.AMARELO + "║      ______ _______ _______ _______      _______  _____   _____  ______        ║")
    print(cor.AMARELO + "║     |  ____ |______ |______    |         |______ |     | |     | |     \\       ║")
    print(cor.AMARELO + "║     |_____| |______ ______|    |         |       |_____| |_____| |_____/       ║")
    print(cor.AMARELO + "║                                                                                ║")
    print(cor.AMARELO + "║                          BEM-VINDO AO GEST FOOD!                               ║")
    print(cor.AMARELO + "╚════════════════════════════════════════════════════════════════════════════════╝")


    print("  1 - MÓDULO DE CLIENTES")
    print("  2 - CARDÁPIO")
    print("  3 - FAZER UM PEDIDO")
    print("  4 - DESLIGAR SISTEMA")


menu()
op=int(input("ESCOLHA UMA OPÇÃO:\n>>>"))
 
 
            


