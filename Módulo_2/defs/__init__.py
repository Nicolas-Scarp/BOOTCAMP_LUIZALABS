class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim Plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

b1 = Bicicleta(1,2,3,4)
b1.correr()
b1.parar()
b1.buzinar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)


"""
        self.cor = input("Informe a cor da bicicleta: ")
        self.modelo = input("Informe o modelo da bicicleta: ")
        self.ano = input("Informe o ano da bicicleta: ")
        self.valor = input("Informe o valor da bicicleta: ")

"""