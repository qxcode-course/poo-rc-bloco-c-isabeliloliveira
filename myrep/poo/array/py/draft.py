# Sequencia de número com teste (par ou impar). 
# Se o item pretendido for par, ele terá direito de entrar na lista, mas, senão, não entrará.
# Se o número escolhido for um quadrado perfeito
import math

numeros_aceitos=[]
qtd_num = int(input())
qtd=0 

def verificar(num_digit):
    raiz= math.isqrt(num_digit)

    return raiz

for i in range(qtd_num):
    num_digit = int(input())
    raiz = verificar(num_digit)

    if num_digit%2==0 or raiz*raiz==num_digit:
        numeros_aceitos.append(num_digit)
    
    else:
        qtd+=1

    # elif raiz*raiz==num_digit:
    #     numeros_aceitos.append(num_digit)

# print(pares)
# print(perf)
# print(ambos)
# print(f"e você digitou {qtd} que não foram aceitos na lista")

# No fim, vai mostrar quantos número pares tem, quantos quadrados perfeitos impares e quantos são pares e quadrados perfeitos.