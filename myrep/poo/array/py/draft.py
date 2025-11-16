#A ideia inicial seria implementar uma lista para os números aceitos(a partir da análise de cada número analisado pela estrutura condicional dentro do looping), 
# números esses que seriam dados pelo usuário, através de um for com número de execuções também definido pelo usuário (qtd_num). Ou seja, o usuário informaria a 
# quantidade (qtd_num) de numeros a ser testada, iriamos testar dentro de um comando de repetiçao dentro do for, que está com numero de execuções de acordo com o 
# que o usuario definiu antes, em que, a cada repetição, um número seria lido e analisado. Para entrar na lista de numeros aceitos, o numero escolhido tem que ser 
# par ou um quadrado perfeito. Sendo que fiz os testes tanto para entrar lista quanto para contar quantos são pares, quantos são quadrados perfeitos, ambos ou que não 
# atendem nenhuma condição e por isso não entraram na lista.

# Primeira tentativa usando input(ideia inicial mas que não rodou)
# import math

# numeros_aceitos=[]
# qtd_num = int(input())
# qtd=0 
# contA=0
# contP=0
# contQ=0

# def verificar(num_digit):
#     raiz= math.isqrt(num_digit)

#     return raiz

# for i in range(qtd_num):
#     num_digit = int(input())
#     raiz = verificar(num_digit)

#     if num_digit%2==0 or raiz*raiz==num_digit:
#         numeros_aceitos.append(num_digit)

#         if num_digit%2==0:
#             contP+=1
#         if raiz*raiz==num_digit:
#             contQ+=1
#         if num_digit%2==0 and raiz*raiz==num_digit:
#             contA+=1
#     else:
#         qtd+=1


# print(f"Na sua lista de numeros aceitos tem {contP} pares, {contQ} quadrados perfeitos, {contA} que atendem as duas condições e {qtd} que não atende nenhuma delas.")


# No fim, vai mostrar quantos número pares tem, quantos quadrados perfeitos impares e quantos são pares e quadrados perfeitos.


#Tentativa oficial pós execuções (como ao terminar não executou corretamente por não aceitar entrada do usuário, fiz dessa forma).

import math #importei para poder calcular a raiz

qtd_num = 10 #o que eu pensei era o usuário digitar um número, mas como o TKO não aceita o input, resolvi demonstrar definindo o número mesmo.
numeros_escolhidos=[2, 3, 9, 64, 8, 49, 7, 13, 10, 25] 
numeros_aceitos=[]
qtd=0 
contA=0
contP=0
contQ=0

for i in range (qtd_num):
    raiz=math.isqrt(numeros_escolhidos[i])
    if numeros_escolhidos[i]%2==0 or raiz*raiz==numeros_escolhidos[i]:
        numeros_aceitos.append(numeros_escolhidos[i])
        if numeros_escolhidos[i]%2==0:
            contP+=1
        if raiz*raiz==numeros_escolhidos[i]:
            contQ+=1
        if numeros_escolhidos[i]%2==0 and raiz*raiz==numeros_escolhidos[i]:
            contA+=1
    else:
        qtd+=1

print(f"Na sua lista de numeros aceitos tem {contP} pares, {contQ} quadrados perfeitos, {contA} que atende as duas condições e {qtd} que não atende nenhuma delas.")

