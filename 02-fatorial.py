# Atividade 2: Fatorial

# A atividade 2 consiste em implementar uma função recursiva para 
# calcular o fatorial de um número inteiro. O fatorial de um número inteiro
# é o produto de todos os números inteiros menores ou iguais a ele. 

# Por exemplo, o fatorial de 5 é 120, pois 5! = 5 * 4 * 3 * 2 * 1 = 120.

# A função recursiva para calcular o fatorial de um número inteiro deve 
# receber um número inteiro como entrada e retornar o fatorial do número.

def fatorial(number):
    if number > 0 and number <= 2:
        return number 
    else:
        return number * fatorial(number - 1)


print(fatorial(5)) # Resultado esperado: 120
