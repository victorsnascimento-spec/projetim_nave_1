combustivel = 110
tripulantes = []

def viajar():
    global combustivel
    print("---------------------------STATUS DA GASOLINA------------------------------")
    if (combustivel >= 30):
        combustivel = combustivel - 30
        print("A nave viajou🛫🛫🛫")
    else:
        print("Você esta sem combustivel suficiente. Abasteça!")


def abastecer():
    global combustivel
    print("--------------------------- ABASTECIMENTO ------------------------------")
    combustivel = 110
    print("O tanque esta cheio⛽⛽⛽")

def status_nave():
    print("--------------------------- STATUS DA NAVE ------------------------------")
    print(f"O combustivel é {combustivel}")
    print(f"Os tripulantes são {tripulantes}")

def registrarTripulantes():
    print("--------------------------- STATUS TRIPULANTES ------------------------------")
    novoTripulante = input("Qual o nome do novo tripulantes? ")
    tripulantes.append(novoTripulante)
    print("Tripulante inserido com secesso!🚀🚀🚀")

while True:
    print("\nBem vindo ao menu interrativo da nave. Por favor selecione uma opção")
    print("\n1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo tripulante | 5- Sair")
    opcao = input("Escolha:" )
    if (opcao == "1"):
        status_nave()
    elif(opcao == "2"):
        viajar()
    elif(opcao == "3"):
        abastecer()
    elif(opcao == "4"):
        registrarTripulantes()
    elif(opcao == "5"):
        break
    
