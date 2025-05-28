import json
import os
from time import sleep
from crudCardapio import cardapio_module
from criacao_pedidos import pedido_module


arquivo = os.path.join(os.path.dirname(__file__), 'clientes.json')


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


def exibir_menu():
    print(cor.AMARELO + "\nMENU:")
    print(cor.AMARELO + "1. ADICIONAR CLIENTE")
    print(cor.AMARELO + "2. LISTAR CLIENTES")
    print(cor.AMARELO + "3. ATUALIZAR CLIENTE")
    print(cor.AMARELO + "4. EXCLUIR CLIENTE")
    print(cor.AMARELO + "5. LISTAR UM CLIENTE")
    print(cor.AMARELO + "6. VOLTAR AO MENU ANTERIOR")
    print(cor.AMARELO + "7. ENCERRAR O PROGRAMA")
    
def carregar_arquivo():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4, ensure_ascii=False)
    with open(arquivo,'r') as f:
        return json.load(f)
    

def adicionar_cliente(nome, idade, cpf, mesa):
    clientes = carregar_arquivo()
    clientes.append({'nome': nome, 'idade': idade, 'cpf': cpf, 'mesa': mesa })
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(clientes,f,indent=4,ensure_ascii=False)
    print(cor.VERDE+"CLIENTE ADICIONADO COM SUCESSO!")


def listar_cliente():
    clientes = carregar_arquivo()
    if clientes:
        print(cor.AMARELO + "="*50)
        print(cor.AMARELO + "               LISTA DE CLIENTES")
        print(cor.AMARELO + "="*50)
        print(cor.AMARELO + "="*50)
        for cliente in clientes:
            
            print(cor.RESET + f"NOME: {cliente['nome']}, IDADE: {cliente['idade']}, CPF: {cliente['cpf']} MESA: {cliente['mesa']}")
            print(cor.AMARELO + "="*50)
    else:
        print(cor.VERMELHO+"NENHUM CLIENTE CADASTRADO.")


def atualizar_cliente(cpf_antigo):
    clientes= carregar_arquivo()
    for cliente in clientes:
        if cliente['cpf']==cpf_antigo:
            cpf_novo=input("DIGITE O NOVO CPF\n>>")
            nome_novo=input("DIGITE O NOVO NOME\n>>")
            idade_nova=input("DIGITE A NOVA IDADE\n>>")
            mesa_nova=input("DIGITE A NOVA MESA\n>>")
            cliente['cpf']=cpf_novo
            cliente['nome']=nome_novo
            cliente['idade']=idade_nova
            cliente['mesa']=mesa_nova
            break
    else:
            print(cor.VERMELHO+"CLIENTE NÃO ENCONTRADO COM ESSE CPF.")
            return
    with open(arquivo, 'w') as f:
        json.dump(clientes,f,indent=4,ensure_ascii=False)
    print(cor.VERDE+"CLIENTE ATUALIZADO!")


def deletar_cliente(excluir_cpf):
    clientes = carregar_arquivo()
    encontrou = False
    for i, cliente in enumerate(clientes):
        if cliente.get('cpf') == excluir_cpf:
            clientes.pop(i)
            encontrou = True
            break
    if encontrou:
        with open(arquivo, 'w') as f:
            json.dump(clientes, f, indent=4, ensure_ascii=False)
        print(cor.VERDE + "CLIENTE APAGADO!")
    else:
        print(cor.VERMELHO + "CPF NÃO ENCONTRADO!")


def listar_um_cliente(listar_um_client):
    clientes = carregar_arquivo()
    encontrou = False
    for  cliente in clientes:
        if cliente.get('cpf') == listar_um_client:
            print(cor.AMARELO + "="*50)
            print(cor.RESET + f"NOME: {cliente['nome']}, IDADE: {cliente['idade']}, CPF: {cliente['cpf']} MESA: {cliente['mesa']}")
            print(cor.AMARELO + "="*50)
            encontrou = True
    if encontrou:
            with open(arquivo, 'w') as f:
                    json.dump(clientes, f, indent=4, ensure_ascii=False)



while True:
    def opcao():
        global op
        op=int(input("Escolha uma opção:\n>>"))

    opcao()

    if(op==1):
    
        
        while True:

            exibir_menu()
            opcaocliente=int(input("ESCOLHA UMA OPÇÃO:\n>>"))
            
            if opcaocliente==1:
                nome=input("DIGITE O NOME DO CLIENTE\n>>")
                idade=input("DIGITE A IDADE DO CLIENTE\n>>")
                cpf=input("DIGITE O CPF DO CLIENTE\n>>")
                mesa=input("DIGITE O NÚMERO DA MESA\n>>")
                adicionar_cliente(nome, idade, cpf, mesa)
                
            elif opcaocliente==2:
                listar_cliente()

            elif opcaocliente==3:
                listar_cliente()
                cpf_antigo=input("DIGITE O CPF A SER ATUALIZADO\n>>")
            
                atualizar_cliente(cpf_antigo)

            elif opcaocliente==4:
                listar_cliente()
                excluir_cpf = input("QUAL CPF VOCÊ DESEJA EXCLUIR\n>>")
                deletar_cliente(excluir_cpf)

            elif opcaocliente==5:
                clientes = carregar_arquivo()
                listar_um_client = input("\nDIGITE O CPF QUE DESEJA EXIBIR?\n>>")
                
                listar_um_cliente(listar_um_client)
            elif opcaocliente==6:
                print("VOLTANDO AO MENU...")
                sleep(2)
                menu()
                break

                

            elif opcaocliente == 7:
                print("ENCERRANDO O PROGRAMA...")
                sleep(2)
                exit()

            else:
                print(cor.VERMELHO+"NÚMERO INVÁLIDO!")

    elif(op==2):
        cardapio_module()

    elif(op==3):
        pedido_module()
        menu()
        

