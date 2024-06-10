# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import div

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación div
    def test_div(self):
        assert div(5,5) == 1
        assert div(6,2) == 3
        assert div(10,5) == 2
        assert div(12,6) == 2