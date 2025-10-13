def calculaExpressoes(string):
    if len(string) == 0:
        return 'String vazia!'
    else:
        nova = so_parenteses = ''
        resutado = 0
        for char in string:
            if char != ' ':
                nova += char
        for char in nova:
            if char in '[{':
                so_parenteses += '('
            elif char in ']}':
                so_parenteses += ')'
            else:
                so_parenteses += char
        resultado = so_parenteses
        return resultado


expressao = "3 + {100 - [4 + (15-7) ] * 7 }"
print(calculaExpressoes(expressao))
