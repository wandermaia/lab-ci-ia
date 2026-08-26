import pytest
from calculadora import somar, subtrair, multiplicar, dividir, raiz_quadrada

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0

def test_subtrair():
    assert subtrair(10, 4) == 6
    assert subtrair(0, 5) == -5

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10
    assert multiplicar(0, 100) == 0

def test_dividir():
    assert dividir(10, 2) == 5.0
    assert dividir(7, 2) == 3.5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)

def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3.0
    assert raiz_quadrada(0) == 0.0

def test_raiz_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)
