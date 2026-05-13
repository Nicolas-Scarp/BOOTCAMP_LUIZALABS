class Estudante:
    escola = input("Digite a escola: ").upper()

    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def cumprimento(self):
    return f"Meu nome é {self.nome} e eu estudo na {self.escola} e minha matricula é {self.matricula}"


"""============================================================================================"""

nome = input("Digite seu nome: ")
matricula = input("Digite sua matricula: ")

aluno_1 = Estudante(nome,matricula)

print(aluno_1)


