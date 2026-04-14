class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = input("Informe a cor da bicicleta: ")
        self.modelo = input("Informe o modelo da bicicleta: ")
        self.ano = input("Informe o ano da bicicleta: ")
        self.valor = input("Informe o valor da bicicleta: ")
    
    def buzinar(self):
        print("Plim Plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
 
    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
 

funções ={
    "CORRER":Bicicleta.correr
}

b1 = Bicicleta("cor","modelo","ano","valor")

print(f"\nA bicicleta tem a cor {b1.cor}, é do modelo {b1.modelo}, do ano de {b1.ano}, no valor de R${b1.valor}")

print("\n================================")
print("Faça a sua escolha!!!")
print("Correr | Buzinar | Parar")
print("================================")


func = input("").upper()
escolha = funções.get(func)
print(escolha)

if escolha:
    b1.escolha()

'''b1.correr()
b1.parar()
b1.buzinar()'''

