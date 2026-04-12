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
    print(curso.upper())
    print(curso.lower())
    print(curso.title())
    print(curso.center(16,"#"))
    print(".".join(curso))

def oito():
    nome="nicolas"
    sobrenome="scarp"
    idade=19
    universidade="uff"
    curso="computação"

    dados={
        "a": "Nicolas",
        "b": "Scarp",
        "c": "19",
        "d": "Computação",
        "e": "UFF"
        }

    print("\nMeu nome é %s %s, eu tenho %d anos e faço %s na %s!" % (nome.title(),sobrenome.title(),idade,curso.title(),universidade.upper()))
    print("\nMeu nome é {} {}, eu tenho {} anos e faço {} na {}!" .format(nome.title(),sobrenome.title(),idade,curso.title(),universidade.upper()))
    print("\nMeu nome é {0} {3}, eu tenho {1} anos e faço {2} na {4}!" .format(nome.title(),idade,curso.title(),sobrenome.title(),universidade.upper()))
    print("\nMeu nome é {a} {b}, eu tenho {c} anos e faço {d} na {e}!" .format(**dados))
    print(f"\nMeu nome é {nome.title()} {sobrenome.title()}, eu tenho {idade} anos e faço {curso.title()} na {universidade.upper()}!")

def nove():
    variable="Nick Scarp: The Programmer"
    print(variable[:10])
    print(variable[12:])
    print(variable[5:10])
    print(variable[5:15:2])
    print(variable[::-1])

def dez():
    pessoa1=["Nick", "19 anos", "Estudante UFF"]
    print(pessoa1)
    pessoa2=["Livi", "18 anos", "Estudante UFJF"]
    print(pessoa2)
    python=list("Python")
    print(python)
    numeros=list(range(10))
    print(numeros)
    matriz=[
        ["Nick", "19 anos", "Estudante UFF"],
        ["Livi", "18 anos", "Estudante UFJF"],
        ["Namorando", "3 anos", "Felizes"]
    ]
    print(f"{matriz[0][0]} e {matriz[1][0]} estão {matriz[2][0]} há {matriz[2][1]}.")
    for i,j in enumerate(pessoa1):
        print(f"{i+1} : {j}")
    print("====================================")
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print(f"{j+1}_Lista{i+1}: {matriz[i][j]}")

def onze():

    dic={
        "Nicolas Scarp": {"Idade" : "19 Anos" , "Faculdade" : "UFF"},
        "Genilson Santos": {"Idade" : "32 Anos", "Faculdade" : "Fiap"}
    }

    print(dic["Nicolas Scarp"]["Idade"])
    print(dic["Nicolas Scarp"]["Faculdade"])
    print(dic["Genilson Santos"]["Idade"])
    print(dic["Genilson Santos"]["Faculdade"])
    print("====================================================")
    for chave,valor in dic.items():
        print(chave,valor)
