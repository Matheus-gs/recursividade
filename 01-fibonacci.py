# Atividade 1: Fibonacci

# A atividade 1 consiste em implementar uma função recursiva para 
# calcular o número de Fibonacci. O número de Fibonacci é uma sequência 
# de números inteiros em que cada número é a soma dos dois números anteriores. 

# Os primeiros números da sequência são:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
 
# A função recursiva para calcular o número de Fibonacci deve receber um 
# número inteiro como entrada e retornar o número de Fibonacci correspondente.

def fibonacci(number):
    if number == 0 or number == 1:  
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(20)) # Resultado esperado: 6765