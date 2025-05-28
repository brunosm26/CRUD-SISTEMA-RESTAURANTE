import json
from time import sleep

from dados_cardapio import cardapio_pratos, cardapio_bebidas, PRATOS_FILE, BEBIDAS_FILE

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



def cardapio_module():
    def cardapio():
        print("  1 - ADICIONAR PRATOS")
        print("  2 - ADICIONAR BEBIDAS ")
        print("  3 - REMOVER ITENS ")
        print("  4 - ALTERAR VALORES")
        print("  5 - VOLTAR AO MENU ANTERIOR")
        print("  6 - DESLIGAR SISTEMA")

    while True:
        cardapio()
        opcar = int(input("ESCOLHA UMA OPÇÃO: \n>>>"))
        if opcar == 1 :
            while True:
                nome_prato = (input("NOME DO PRATO : "))
                numero_prato = int(input("NUMERO DO PRATO : "))
                valor_prato = float(input("VALOR DO PRATO : "))
                novo_prato = {"nome_prato": nome_prato, "numero": numero_prato, "valor": valor_prato}
                cardapio_pratos.append(novo_prato)
                with open (PRATOS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(cardapio_pratos, f, indent=4, ensure_ascii=False)
                print("PRATO ADICIONADO", novo_prato)
                print("CARDÁPIO DE PRATOS ATUAL:", cardapio_pratos) 
                print(" 1 - CONTINUAR ADICIONANDO ")
                print(" 2 - VOLTAR AO MENU CARDAPIO ")
                opcont = int (input("ESCOLHA UMA OPCAO : "))
                if opcont == 2 :
                    print("VOLTANDO . . .")
                    sleep(2) 
                    break
        elif opcar == 2:
            while True:
                nome_bebida = (input("NOME DA BEBIDA : "))
                numero_bebida = int(input("NUMERO DA BEBIDA : "))
                valor_bebida = float(input("VALOR DA BEBIDA : "))
                nova_bebida = {"nome_bebida": nome_bebida, "numero": numero_bebida, "valor": valor_bebida}
                cardapio_bebidas.append(nova_bebida)
                with open (BEBIDAS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(cardapio_bebidas, f, indent=4 , ensure_ascii=False)
                print("BEBIDA ADICIONADA", nova_bebida)
                print("CARDÁPIO DE BEBIDAS ATUAL:",cardapio_bebidas) 
                print(" 1 - CONTINUAR ADICIONANDO ")
                print(" 2 - VOLTAR AO MENU CARDAPIO ")
                opcont = int (input("ESCOLHA UMA OPCAO : "))
                if opcont == 2 :
                    print("VOLTANDO . . .")
                    sleep(2) 
                    break
                
        elif opcar == 3:
            while True:
                item_remover = input("DIGITE O NOME OU NÚMERO DO ITEM PARA REMOVER: ")
                encontrado = False
                for item in list(cardapio_pratos):
                    if item["nome_prato"].lower() == item_remover.lower() or str(item["numero"]) == item_remover:
                        cardapio_pratos.remove(item)
                        print(f"PRATO '{item_remover}' REMOVIDO.")
                        print("CARDÁPIO DE PRATOS ATUAL:", cardapio_pratos) 
                        encontrado = True
                        with open (PRATOS_FILE, 'w', encoding='utf-8') as f:
                            json.dump(cardapio_pratos, f, indent=4, ensure_ascii=False)
                        break
                    
                if not encontrado:
                    for item in list(cardapio_bebidas):
                        if item["nome_bebida"].lower() == item_remover.lower() or str(item["numero"]) == item_remover:
                            cardapio_bebidas.remove(item)
                            print(f"BEBIDA '{item_remover}' REMOVIDA.")
                            print("CARDÁPIO DE BEBIDAS ATUAL:", cardapio_bebidas) 
                            encontrado = True
                            with open (BEBIDAS_FILE, 'w', encoding='utf-8') as f:
                                json.dump(cardapio_bebidas, f, indent=4, ensure_ascii=False)
                        break
                if not encontrado:
                    print(f"ITEM '{item_remover}' NÃO ENCONTRADO NO CARDÁPIO.")
                print(" 1 - CONTINUAR REMOVENDO ITENS")
                print(" 2 - VOLTAR AO MENU CARDAPIO")
                opcont_remover = int(input("ESCOLHA UMA OPÇÃO: "))
                if opcont_remover == 2:
                    print("VOLTANDO . . .")
                    sleep(2) 
                    break
        elif opcar == 4 :
             while True :
                alterar_valor = (input("INFORME O ITEM QUE DESEJA ALTERAR O VALOR : "))
                novo = False
                for item in list(cardapio_pratos):
                    if item["nome_prato"] == alterar_valor.lower() or str(item["numero"]) == alterar_valor:
                        preço_novo = float(input("INFORME O NOVO VALOR DO PRATO: "))
                        item ["valor"]= preço_novo
                        print(f"VALOR DO PRATO FOI ALTERADO PARA R$ {preço_novo}: ")
                        print("CARDÁPIO DE PRATOS ATUAL: ", cardapio_pratos)
                        novo = True
                        with open (PRATOS_FILE, 'w', encoding='utf-8') as f:
                            json.dump(cardapio_pratos, f, indent=4, ensure_ascii=False)
                        break
                    
                if not novo:
                    for item in list(cardapio_bebidas):
                         if item["nome_bebida"] == alterar_valor.lower() or str(item["numero"]) == alterar_valor:
                              preço_novo = float(input("INFORME O NOVO VALOR DA BEBIDA: "))
                              item["valor"] = preço_novo
                              print(f"VALOR DA BEBIDA FOI ALTERADO PARA R$ {preço_novo}: ")
                              print("CARDÁPIO DE BEBIDAS ATUAL: ", cardapio_bebidas )
                              novo = True
                              with open (BEBIDAS_FILE, 'w', encoding='utf-8') as f:
                                  json.dump(cardapio_bebidas, f, indent=4, ensure_ascii=False)
                              break
                          
                if not novo:
                    print(f"ITEM '{alterar_valor}' NÃO ENCONTRADO NO CARDÁPIO.")
                print(" 1 - CONTINUAR ALTERANDO ITENS")
                print(" 2 - VOLTAR AO MENU CARDAPIO")
                opcont_alterar = int(input("ESCOLHA UMA OPÇÃO: "))
                if opcont_alterar == 2:
                    break            
        elif opcar == 5:
            print ("VOLTANDO")
            menu()
            sleep(2)
            break
        
        elif opcar == 6 :
            print("ENCERRANDO O PROGRAMA...")
            sleep(2)
            break