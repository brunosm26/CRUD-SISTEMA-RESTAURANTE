import json
import os 



cardapio = {
    "Feijoada": 30.00,
    "Baião de Dois": 25.00,
    "Carne de Sol com Macaxeira": 35.00,
    "Macarronada": 20.00,
    "Pizza Calabresa": 40.00,
    "Strogonoff de Frango": 28.00,
    "Lasanha à Bolonhesa": 32.00,
    "Suco de Laranja": 7.00,
    "Refrigerante": 5.00,
    "Cuscuz com Ovo": 10.00
}

pedidos = []
numero_pedido = 1

def criar_pedido(numero_pedido): 
    print("\n==== Criando novo pedido ====\n")

    cpfcliente = int(input("Digite o CPF do cliente: "))

    print("\nCardápio:\n")
    for prato, preco in cardapio.items():
        print(f"{prato} - R${preco:.2f}")

    pratos = input("\nDigite os pratos (separados por vírgula): ").split(",")
    pratos = [prato.strip() for prato in pratos]

    lista_pratos = [] 
    total = 0.0

    for prato in pratos: 
        if prato in cardapio: 
            lista_pratos.append(prato)#m
            total += cardapio[prato]#c 
        else:
            print(f"Prato '{prato}' não encontrado")

    print("\nDigite o status do pedido: ")
    status_pedido = int(input("1 - Pronto \n2 - Em Preparo \n3 - Cancelado \n4 - Entregue\n"))
    
    if status_pedido == 1: 
        status = "Pronto"
    elif status_pedido == 2: 
        status = "Em Preparo"
    elif status_pedido == 3: 
        status = "Cancelado"
    elif status_pedido == 4:
        status = "Entregue"
    else:
        status = "Desconhecido"

    pedido = {
        "num_pedido": numero_pedido,
        "cpf_cliente": cpfcliente,
        "pratos": lista_pratos, 
        "total": total,
        "status": status
    }

    pedidos.append(pedido)

    print("\n✅ Pedido criado com sucesso!")
    print(f"✅ Numero do pedido: {pedido['num_pedido']}")
    print(f"✅ CPF Cliente: {pedido['cpf_cliente']}")
    print(f"✅ Pratos: {', '.join(pedido['pratos'])}")
    print(f"✅ Total: R${pedido['total']:.2f}")
    print(f"✅ Status: {pedido['status']}\n")


while True:
    criar_pedido(numero_pedido)
    numero_pedido += 1

    continuar = input("Deseja adicionar outro pedido? (s/n): ")
    if continuar != 's':
        break

print("\n Lista final:")
for pedido in pedidos:
    print(f"🍽️ Pedido {pedido['num_pedido']} - 🙋‍♂️ Cliente: {pedido['nome_cliente']} - 💸 Total: {pedido['total']:.2f} - ⏰ Status: {pedido['status']}")

with open ("criacao_pedidos.json", "w") as arquivo:
    json.dump(pedidos, arquivo, indent = 4)