import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

def raiz_quadrada(n):
    if n < 0:
        raise ValueError("Raiz de número negativo não é definida nos reais")
    return math.sqrt(n)

def porcentagem(valor, percentual):
    return valor * percentual / 100
