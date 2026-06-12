combustivel = 100
tripulantes = []

def travarMenu():
    input("Pressione <ENTER> para continuar...")

def viajar():
    global combustivel
    print("--------------------------- STATUS DA GASOLINA ---------------------------")
    if (combustivel >= 30):
        combustivel = combustivel - 30
        print("A nave viajou🛫🛫🛫")
    else:
        print("Você esta sem combustivel suficiente. Abasteça!")

    travarMenu()
    
def abastecer():
    global combustivel
    print("--------------------------- ABASTECIMENTO ---------------------------")
    combustivel = 100
    print("O tanque esta cheio⛽⛽⛽")
    print("------------------------------------------------------")

    travarMenu()

def status_nave():
    print("--------------------------- STATUS DA NAVE ---------------------------")
    print(f"O combustivel é {combustivel}")
    print(f"Os tripulantes são {tripulantes}")
    print("------------------------------------------------------")

    travarMenu()

def registrarTripulantes():
    print("--------------------------- STATUS TRIPULANTES ---------------------------")
    novoTripulante = input("Qual o nome do novo tripulantes? ")
    tripulantes.append(novoTripulante)
    print("Tripulante inserido com secesso!🚀🚀🚀")
    print("------------------------------------------------------")
    travarMenu()

def retirarTripulante():
    i = int(input("Qual tripulante deseja remover(Lembrando, a sequência começa com 0)? "))
    tripulantes.pop(i)
    print("Tripulante removido com sucesso!🚀🚀🚀")

    travarMenu()

while True:
    print("\n--------------------------- MENU DA NAVE ---------------------------")
    print("\n1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 4- Novo tripulante | 5- Remover tripulante | 6- Sair\n")
    opcao = input("Escolha a opção que dejasa fazer:" )
    if (opcao == "1"):
        status_nave()
    elif(opcao == "2"):
        if (len(tripulantes)== 0):
            print("ERRO ⚠️⚠️⚠️")
            print("Não há tripulantes!!!")
            i = input("Dejesa adicionar um tripulante? (s/n)")
            if i == "s":
                 registrarTripulantes
        else:
            viajar()
    elif(opcao == "3"):
        abastecer()
    elif(opcao == "4"):
        registrarTripulantes()
    elif(opcao == "5"):
        if len(tripulantes) == 0:
            print("ERRO ⚠️⚠️⚠️")
            print("Não há tripulantes!!!")
            i = input("Dejesa adicionar um tripulante? (s/n)")
            if i == "s":
                registrarTripulantes
        else:
            retirarTripulante()
    elif(opcao == "6"):
        break