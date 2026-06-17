"""Módulo de operações matemáticas básicas para uma calculadora."""

import math

def somar(a, b):
    """Retorna a soma de dois números.

    Args:
        a: Primeiro operando.
        b: Segundo operando.

    Returns:
        Resultado da soma de a e b.
    """
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números.

    Args:
        a: Minuendo.
        b: Subtraendo.

    Returns:
        Resultado da subtração de a por b.
    """
    return a - b

def multiplicar(a, b):
    """Retorna o produto de dois números.

    Args:
        a: Primeiro fator.
        b: Segundo fator.

    Returns:
        Resultado da multiplicação de a por b.
    """
    return a * b

def dividir(a, b):
    """Retorna o quociente da divisão de dois números.

    Args:
        a: Dividendo.
        b: Divisor.

    Returns:
        Resultado da divisão de a por b.

    Raises:
        ValueError: Se b for igual a zero.
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

def raiz_quadrada(n):
    """Retorna a raiz quadrada de um número.

    Args:
        n: Número do qual se deseja calcular a raiz quadrada.

    Returns:
        Raiz quadrada de n.

    Raises:
        ValueError: Se n for negativo.
    """
    if n < 0:
        raise ValueError("Raiz de número negativo não é definida nos reais")
    return math.sqrt(n)

def porcentagem(valor, percentual):
    """Retorna o valor correspondente a uma porcentagem.

    Args:
        valor: Valor base sobre o qual a porcentagem será calculada.
        percentual: Percentual a ser aplicado sobre o valor.

    Returns:
        Resultado do percentual aplicado ao valor.
    """
    return valor * percentual / 100
