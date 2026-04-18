def bike():
    class Bicicleta:
        def __init__(self, cor, modelo, ano, valor):
            self.cor = input("Informe a cor da bicicleta: ")
            self.modelo = input("Informe o modelo da bicicleta: ")
            self.ano = input("Informe o ano da bicicleta: ")
            self.valor = input("Informe o valor da bicicleta: ")
        
        def buzinar(self):
            print("\nPlim Plim...")
        
        def parar(self):
            print("\nParando bicicleta...")
            print("Bicicleta parada!")
    
        def correr(self):
            print("\nVrummmmm...")

        def __str__(self):
            return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    

<<<<<<< Updated upstream
    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
 
b1 = Bicicleta("cor","modelo","ano","valor")

fun ={
    "CORRER":b1.correr,
    "PARAR":b1.parar,
    "BUZINAR":b1.buzinar

}


=======
    b1 = Bicicleta("cor","modelo","ano","valor")

    fun ={
        "CORRER":b1.correr,
        "PARAR":b1.parar,
        "BUZINAR":b1.buzinar
    }

    print(f"\nA bicicleta tem a cor {b1.cor}, é do modelo {b1.modelo}, do ano de {b1.ano}, no valor de R${b1.valor}")
>>>>>>> Stashed changes

    print("\n================================")
    print("Faça a sua escolha!!!")
    print("Correr | Buzinar | Parar")
    print("================================")

while True:
    func = input("O que deseja fazer? ").upper()

<<<<<<< Updated upstream
    if func == "EXIT":
        break

    escolha = fun.get(func)

    if escolha:
        escolha()
    else:
        print("Valor inválido!")
=======
    while True:
        func = input("\n").upper()
        if func in fun:
            fun[func]()
        elif func == "EXIT":
            break
        else:
            print("Comando Inválido!")

def wait():
    print("wait a moment")
>>>>>>> Stashed changes

def wait2():
    print("wait a moment 2")