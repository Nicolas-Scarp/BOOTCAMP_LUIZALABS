def um():
    nome= "nicolas"
    idade= 19
    print(nome, idade, sep =" Scarp \nIdade:  ", end="...")

def dois():
    print(10 * 10 / 5)
    print(10 / 10 * 5)

def tres():
    saldo=input()
    saque=input()
    print(saldo==saque)

def quatro():
    saldo= 0    
    print(saldo)
    while saldo < 100:
        print(saldo)
        saldo+=1
def cinco():
    print(1+2)
    print(2+2)
def seis():
    idade=int(input("Digite a idade: "))
    if idade > 18:
        print(f"Voce tem {idade} anos!")
    elif idade == 18:
        print("Voce tem 18 anos!")
    elif idade < 18:
        print("Voce ainda não tem 18 anos!")
    else:
        if idade :
            print("Opção Inválida")
def sete():
    curso = input("Digite algo: ")
    print(curso.center(10,"#"))
    print(".".join(curso))

  