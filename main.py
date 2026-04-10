import defs

functions = {
    "UM":defs.um,
    "DOIS":defs.dois,
    "TRES":defs.tres,
    "QUATRO":defs.quatro,
    "CINCO":defs.cinco,
    "SEIS":defs.seis,
    "SETE":defs.sete,
    "OITO":defs.oito,
    "NOVE":defs.nove,
    "DEZ":defs.dez
}

func = input("Qual código voce quer rodar?").upper()

escolha = functions.get(func)

if escolha:
    escolha()
else:
    print("Função Não Encontrada!")