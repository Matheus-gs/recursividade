# Atividade 4: Máximo

# A atividade 4 consiste em implementar uma função recursiva 
# para encontrar o maior número de uma sequência de números.

# A função recursiva para encontrar o maior número de uma 
# sequência de números deve receber uma sequência de números 
# como entrada e retornar o maior número da sequência.

def encontraMaiorNumero(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]

    maiorNumero = encontraMaiorNumero(lista[1:])

    if lista[0] > maiorNumero:
        return lista[0]
    
    return maiorNumero

print(encontraMaiorNumero([12, 39, 15, 27, 4, 21])) # Resultado esperado: 39 