# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import div

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación div
    def test_div(self):
        assert div(4,5) == 0.8
        assert div(-1,-2) == 0.5
        assert div(-7,5) == 1.4
        assert div(-7,9) == -0.77