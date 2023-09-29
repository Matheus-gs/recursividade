# Atividade 5: Reverso

# A atividade 5 consiste em implementar uma função 
# recursiva para inverter uma sequência de caracteres.

# A função recursiva para inverter uma sequência de caracteres 
# deve receber uma sequência de caracteres como entrada e 
# retornar uma nova sequência com os caracteres invertidos.

def inverteString(string):
    if len(string) <= 1:
        return string

    stringInvertida = inverteString(string[1: -1])

    return (string[-1] + stringInvertida + string[0]).lower()
    

print(inverteString("Onibus")) # Resultado esperado: "subino"