"""Testes unitários do módulo calculadora."""

import math
import sys

import pytest

from calculadora import (
    dividir,
    multiplicar,
    porcentagem,
    raiz_quadrada,
    somar,
    subtrair,
)

INVALIDOS = [
    pytest.param(None, id="none"),
    pytest.param("texto", id="str"),
]


class TestSomar:
    @pytest.mark.parametrize(
        "a, b, esperado",
        [
            pytest.param(2, 3, 5, id="positivos"),
            pytest.param(-1, 1, 0, id="negativo-e-positivo"),
            pytest.param(-2, -3, -5, id="negativos"),
            pytest.param(0, 0, 0, id="zeros"),
            pytest.param(2.5, 0.5, 3.0, id="floats"),
        ],
    )
    def test_casos_felizes(self, a, b, esperado):
        assert somar(a, b) == esperado

    def test_precisao_de_ponto_flutuante(self):
        assert somar(0.1, 0.2) == pytest.approx(0.3)

    def test_inteiros_muito_grandes(self):
        assert somar(10**308, 10**308) == 2 * 10**308

    def test_overflow_de_float_resulta_em_inf(self):
        assert somar(sys.float_info.max, sys.float_info.max) == math.inf

    def test_infinito(self):
        assert somar(math.inf, 1) == math.inf

    def test_nan_se_propaga(self):
        assert math.isnan(somar(math.nan, 1))

    def test_inf_menos_inf_gera_nan(self):
        assert math.isnan(somar(math.inf, -math.inf))

    @pytest.mark.parametrize("invalido", INVALIDOS)
    def test_entrada_invalida_levanta_type_error(self, invalido):
        with pytest.raises(TypeError):
            somar(invalido, 1)


class TestSubtrair:
    @pytest.mark.parametrize(
        "a, b, esperado",
        [
            pytest.param(10, 4, 6, id="positivos"),
            pytest.param(0, 5, -5, id="zero-menos-positivo"),
            pytest.param(-3, -3, 0, id="negativos-iguais"),
            pytest.param(5.5, 0.5, 5.0, id="floats"),
        ],
    )
    def test_casos_felizes(self, a, b, esperado):
        assert subtrair(a, b) == esperado

    def test_precisao_de_ponto_flutuante(self):
        assert subtrair(0.3, 0.1) == pytest.approx(0.2)

    def test_valores_extremos(self):
        assert subtrair(-sys.float_info.max, sys.float_info.max) == -math.inf

    def test_nan_se_propaga(self):
        assert math.isnan(subtrair(math.nan, 1))

    @pytest.mark.parametrize("invalido", INVALIDOS)
    def test_entrada_invalida_levanta_type_error(self, invalido):
        with pytest.raises(TypeError):
            subtrair(invalido, 1)


class TestMultiplicar:
    @pytest.mark.parametrize(
        "a, b, esperado",
        [
            pytest.param(3, 4, 12, id="positivos"),
            pytest.param(-2, 5, -10, id="negativo-e-positivo"),
            pytest.param(-2, -5, 10, id="negativos"),
            pytest.param(0, 100, 0, id="zero"),
            pytest.param(1.5, 2, 3.0, id="float"),
        ],
    )
    def test_casos_felizes(self, a, b, esperado):
        assert multiplicar(a, b) == esperado

    def test_zero_negativo(self):
        assert multiplicar(-0.0, 5) == 0.0

    def test_inteiros_muito_grandes(self):
        assert multiplicar(10**200, 10**200) == 10**400

    def test_overflow_de_float_resulta_em_inf(self):
        assert multiplicar(sys.float_info.max, 2) == math.inf

    def test_zero_vezes_inf_gera_nan(self):
        assert math.isnan(multiplicar(0, math.inf))

    def test_nan_se_propaga(self):
        assert math.isnan(multiplicar(math.nan, 2))

    def test_none_levanta_type_error(self):
        with pytest.raises(TypeError):
            multiplicar(None, 2)

    def test_str_por_str_levanta_type_error(self):
        with pytest.raises(TypeError):
            multiplicar("a", "b")

    def test_str_por_int_repete_a_string(self):
        """Documenta o comportamento nativo do Python, sem validação de tipo."""
        assert multiplicar("ab", 2) == "abab"


class TestDividir:
    @pytest.mark.parametrize(
        "a, b, esperado",
        [
            pytest.param(10, 2, 5.0, id="exata"),
            pytest.param(7, 2, 3.5, id="fracionaria"),
            pytest.param(-9, 3, -3.0, id="dividendo-negativo"),
            pytest.param(-9, -3, 3.0, id="ambos-negativos"),
            pytest.param(0, 5, 0.0, id="zero-dividido"),
        ],
    )
    def test_casos_felizes(self, a, b, esperado):
        assert dividir(a, b) == esperado

    def test_precisao_de_ponto_flutuante(self):
        assert dividir(1, 3) == pytest.approx(0.333333333333)

    def test_divisor_muito_pequeno(self):
        assert dividir(1, sys.float_info.min) > 1e300

    def test_infinito_dividido_por_numero(self):
        assert dividir(math.inf, 2) == math.inf

    def test_nan_se_propaga(self):
        assert math.isnan(dividir(math.nan, 2))

    @pytest.mark.parametrize(
        "divisor",
        [
            pytest.param(0, id="zero-int"),
            pytest.param(0.0, id="zero-float"),
            pytest.param(-0.0, id="zero-negativo"),
        ],
    )
    def test_divisao_por_zero(self, divisor):
        with pytest.raises(ValueError, match="Divisão por zero"):
            dividir(5, divisor)

    def test_zero_dividido_por_zero(self):
        with pytest.raises(ValueError, match="Divisão por zero"):
            dividir(0, 0)

    @pytest.mark.parametrize("invalido", INVALIDOS)
    def test_entrada_invalida_levanta_type_error(self, invalido):
        with pytest.raises(TypeError):
            dividir(invalido, 2)


class TestRaizQuadrada:
    @pytest.mark.parametrize(
        "n, esperado",
        [
            pytest.param(9, 3.0, id="quadrado-perfeito"),
            pytest.param(0, 0.0, id="zero"),
            pytest.param(1, 1.0, id="um"),
            pytest.param(0.25, 0.5, id="fracao"),
        ],
    )
    def test_casos_felizes(self, n, esperado):
        assert raiz_quadrada(n) == esperado

    def test_raiz_irracional(self):
        assert raiz_quadrada(2) == pytest.approx(1.41421356237)

    def test_numero_muito_grande(self):
        assert raiz_quadrada(10**300) == pytest.approx(1e150)

    def test_infinito(self):
        assert raiz_quadrada(math.inf) == math.inf

    def test_zero_negativo(self):
        assert raiz_quadrada(-0.0) == 0.0

    def test_nan_se_propaga(self):
        assert math.isnan(raiz_quadrada(math.nan))

    @pytest.mark.parametrize(
        "n",
        [
            pytest.param(-4, id="inteiro-negativo"),
            pytest.param(-1, id="menos-um"),
            pytest.param(-0.0001, id="float-negativo-pequeno"),
            pytest.param(-math.inf, id="menos-infinito"),
        ],
    )
    def test_numero_negativo(self, n):
        with pytest.raises(ValueError, match="número negativo"):
            raiz_quadrada(n)

    @pytest.mark.parametrize("invalido", INVALIDOS)
    def test_entrada_invalida_levanta_type_error(self, invalido):
        with pytest.raises(TypeError):
            raiz_quadrada(invalido)


class TestPorcentagem:
    @pytest.mark.parametrize(
        "valor, percentual, esperado",
        [
            pytest.param(200, 10, 20.0, id="dez-por-cento"),
            pytest.param(50, 100, 50.0, id="cem-por-cento"),
            pytest.param(80, 0, 0.0, id="zero-por-cento"),
            pytest.param(0, 50, 0.0, id="valor-zero"),
            pytest.param(80, 12.5, 10.0, id="percentual-fracionario"),
        ],
    )
    def test_casos_felizes(self, valor, percentual, esperado):
        assert porcentagem(valor, percentual) == esperado

    def test_percentual_maior_que_100(self):
        assert porcentagem(50, 200) == 100.0

    def test_percentual_negativo(self):
        assert porcentagem(200, -10) == -20.0

    def test_valor_negativo(self):
        assert porcentagem(-200, 10) == -20.0

    def test_precisao_de_ponto_flutuante(self):
        assert porcentagem(0.1, 3) == pytest.approx(0.003)

    def test_overflow_de_float_resulta_em_inf(self):
        assert porcentagem(sys.float_info.max, 200) == math.inf

    def test_nan_se_propaga(self):
        assert math.isnan(porcentagem(math.nan, 10))

    @pytest.mark.parametrize("invalido", INVALIDOS)
    def test_entrada_invalida_levanta_type_error(self, invalido):
        with pytest.raises(TypeError):
            porcentagem(invalido, 10)
