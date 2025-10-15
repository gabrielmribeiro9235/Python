def tiraElementos(lista, retira):
    if lista == []:
        return 'Lista vazia!'
    elif len(lista) == 1:
        return lista[0]
    else:
        if lista[0] in retira:
            del lista[0]
        tiraElementos(lista[1:], retira)
        return lista


numeros = [21, 9, 35, 9, 43, 7]
tirar = [7, 9, 8]
print(tiraElementos(numeros, tirar))

