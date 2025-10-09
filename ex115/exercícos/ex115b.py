from ex115.defs.b import *

print(f'{"DESAFIO 115":=^26}')
arq = 'cursoemvideo.txt'
if not arqexiste(arq):
    criararq(arq)
menu(arq)
