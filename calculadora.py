"""Módulo de operações matemáticas básicas.

Fornece funções para soma, subtração, multiplicação, divisão, raiz quadrada
e cálculo de porcentagem. As funções não validam tipos: entradas não
numéricas (por exemplo ``None`` ou ``str``) provocam ``TypeError`` nativo
do Python, e valores como ``nan`` e ``inf`` seguem a aritmética de ponto
flutuante do IEEE 754.

Example:
    >>> from calculadora import somar
    >>> somar(2, 3)
    5
"""

import math


def somar(a: float, b: float) -> float:
    """Soma dois números.

    Args:
        a: Primeira parcela.
        b: Segunda parcela.

    Returns:
        A soma de ``a`` e ``b``.

    Example:
        >>> somar(2, 3)
        5
    """
    return a + b


def subtrair(a: float, b: float) -> float:
    """Subtrai um número de outro.

    Args:
        a: Minuendo.
        b: Subtraendo.

    Returns:
        A diferença ``a - b``.

    Example:
        >>> subtrair(10, 4)
        6
    """
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Multiplica dois números.

    Args:
        a: Primeiro fator.
        b: Segundo fator.

    Returns:
        O produto de ``a`` e ``b``.

    Example:
        >>> multiplicar(3, 4)
        12
    """
    return a * b


def dividir(a: float, b: float) -> float:
    """Divide um número por outro.

    Args:
        a: Dividendo.
        b: Divisor. Não pode ser zero.

    Returns:
        O quociente ``a / b`` como ``float``.

    Raises:
        ValueError: Se ``b`` for zero.

    Example:
        >>> dividir(7, 2)
        3.5
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


def raiz_quadrada(n: float) -> float:
    """Calcula a raiz quadrada de um número.

    Args:
        n: Número não negativo.

    Returns:
        A raiz quadrada de ``n`` como ``float``.

    Raises:
        ValueError: Se ``n`` for negativo.

    Example:
        >>> raiz_quadrada(9)
        3.0
    """
    if n < 0:
        raise ValueError("Raiz de número negativo não é definida nos reais")
    return math.sqrt(n)


def porcentagem(valor: float, percentual: float) -> float:
    """Calcula uma porcentagem de um valor.

    Args:
        valor: Valor base.
        percentual: Percentual a aplicar, em pontos percentuais (``10``
            representa 10%). Pode ser negativo ou maior que 100.

    Returns:
        O resultado de ``valor * percentual / 100``.

    Example:
        >>> porcentagem(200, 10)
        20.0
    """
    return valor * percentual / 100
