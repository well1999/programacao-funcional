
##1. Função map Aplique a função map na lista de emprestimos para extrair os valores da chave valor_emprestimos na lista valor_emprestimos_lista . ###

numeros = [1, 2, 3]
numeros_ao_cubo = map(lambda num: num ** 3, numeros)
print(list(numeros_ao_cubo))

### atividade 2 ##
valor_emprestimos_lista_filtrada = [12.00,1000.11,305.55]
print(valor_emprestimos_lista_filtrada) 


##atividade 3##
numeros = [1, 2, 3]
from functools import reduce
soma_do_valor_do_emprestimo= reduce(lambda x, y: x + y, numeros)
print(soma_do_valor_do_emprestimo)

## ativide 3.2 ###
def maior_entre(vel: int, mve: int) -> int:
    return vel if vel >= mve else mve
vel = 11
mve = 0
print(maior_entre(vel=vel, mve=mve))


## atividade 3.3 ###
list = [1258, 2784, ]
print("List : " + str(list))

st_dev = statistics.pstdev(list)
print("desvio padrao valor do emprestimo: " + str(st_dev))
