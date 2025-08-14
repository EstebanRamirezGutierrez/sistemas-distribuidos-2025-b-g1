import pytest
from src.palindrome import es_palindromo_basico, es_palindromo, normalizar_texto

def test_basico_verdadero():
    assert es_palindromo_basico("Anita lava la tina") is True

def test_basico_falso():
    assert es_palindromo_basico("palabra") is False

def test_unicode_acentos():
    assert es_palindromo("Ánita   lava, la tíná!") is True

def test_unicode_conservar_todo():
    s = "Ánita   lava, la tíná!"
    assert es_palindromo(s, sensible_mayus=True, conservar_espacios=True, conservar_signos=True, quitar_acentos_flag=False) is False

def test_normalizacion_nfkd():
    t = normalizar_texto("Å", forma_normalizacion="NFKD", quitar_acentos_flag=True)
    assert t == "a"
