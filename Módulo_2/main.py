import defs

dict = {
    "1":defs.bike,
    "2":defs.animal,
    "3":defs.wait2
}

while True:

    escolha = input("\nQual função deseja rodar?\n").upper()
    func = dict.get(escolha)

    if func:
        func()
        break
    elif func == "EXIT":
        break
    else:
        print("\nFunção não encontrada!\nDigite outra função!")
        continue
