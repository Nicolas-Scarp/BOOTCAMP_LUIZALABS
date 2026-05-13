class Estudante:
    escola = input("Digite a escola: ").upper()

    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
    def cumprimento(self):
        return f"Meu nome é {self.nome} e eu estudo na {self.escola} e minha matricula é {self.matricula}"

aluno_1 = Estudante("Nicolas",2107)
print(aluno_1)


