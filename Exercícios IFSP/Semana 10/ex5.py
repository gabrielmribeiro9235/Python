def tuplaStrings():
    n = int(input("Quantas strings você quer inserir? "))
    tupla = ()
    for i in range(n):
        elemento = input(f"{i+1}ª string: ")
        tupla += len(elemento),
    return tupla


print(tuplaStrings())
