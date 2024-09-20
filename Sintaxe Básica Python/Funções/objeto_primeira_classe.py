def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return (a * 2) + (b * 3)

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(35, 25, subtrair)
exibir_resultado(8, 3, multiplicar)