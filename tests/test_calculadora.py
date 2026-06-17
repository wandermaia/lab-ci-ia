"""Testes unitários para o módulo calculadora."""

import pytest
from calculadora import somar, subtrair, multiplicar, dividir, raiz_quadrada

def test_somar():
    """Verifica a soma de dois números, incluindo negativos e zero."""
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0

def test_subtrair():
    """Verifica a subtração de dois números, incluindo resultado negativo."""
    assert subtrair(10, 4) == 6
    assert subtrair(0, 5) == -5

def test_multiplicar():
    """Verifica a multiplicação de dois números, incluindo negativos e zero."""
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10
    assert multiplicar(0, 100) == 0

def test_dividir():
    """Verifica a divisão de dois números com resultado inteiro e decimal."""
    assert dividir(10, 2) == 5.0
    assert dividir(7, 2) == 3.5

def test_dividir_por_zero():
    """Verifica que divisão por zero levanta ValueError."""
    with pytest.raises(ValueError):
        dividir(5, 0)

def test_raiz_quadrada():
    """Verifica a raiz quadrada de números positivos e zero."""
    assert raiz_quadrada(9) == 3.0
    assert raiz_quadrada(0) == 0.0

def test_raiz_negativa():
    """Verifica que raiz de número negativo levanta ValueError."""
    with pytest.raises(ValueError):
        raiz_quadrada(-4)
