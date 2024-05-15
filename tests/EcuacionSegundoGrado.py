import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):

    def setUp(self):
        self.calculoraices = EcuacionSegundoGrado

    def tearDown(self):
        self.calculoraices = None

    def test_calculoECS_dosnumeros_retornaResolucion(self):
        # Arrange
        a= 1
        b= 2
        c= 1
        resultadoEsperadoRaiz1 = -1
        resultadoEsperadoRaiz2 = -1
        # Do
        resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoraices.calculoECS(a,b,c)

        # Assert
        self.assertEqual(resultadoEsperadoRaiz1, resultadoActualRaiz1)
        self.assertEqual(resultadoEsperadoRaiz2, resultadoActualRaiz2)




if __name__ == '__main__':
    unittest.main()
