# Atividade 3: Somatório

# A atividade 3 consiste em implementar uma função recursiva 
# para calcular o somatório de uma sequência de números. O somatório de uma 
# sequência de números é a soma de todos os números da sequência.

# A função recursiva para calcular o somatório de uma sequência de 
# números deve receber uma sequência de números como entrada e retornar o 
# somatório da sequência.

def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma(lista[1:])

print(soma([1, 2, 3, 4, 5])) # Resultado esperado: 15 