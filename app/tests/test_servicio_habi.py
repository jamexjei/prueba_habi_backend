import unittest
from app.services.prueba_habi_service import ValidarString,ConsultarPropiedades,ValidarNumero

#test par probar datos vacios
class TestValidarString(unittest.TestCase):
    
    def test_palabra_prohibida(self):
        codigo, mensaje = ValidarString("SELECT something")
        self.assertEqual(codigo, 422)
        self.assertEqual(mensaje, "La palabra SELECT no debe usarse en la solicitud")

    def test_palabra_permitida(self):
        resultado = ValidarString("Esto es un texto válido")
        self.assertTrue(resultado)

    def test_variantes_de_palabras_prohibidas(self):
        for palabra in ["UPDATE", "DELETE", "DROP", "USE"]:
            codigo, mensaje = ValidarString(f"Contiene {palabra} aquí")
            self.assertEqual(codigo, 422)
            self.assertEqual(mensaje, f"La palabra {palabra} no debe usarse en la solicitud")

class TestConsultarPropiedades(unittest.TestCase):
    def test_no_trae_datos(self):
        codigo,mensaje=ConsultarPropiedades(5,2011,'')
        self.assertEqual(codigo,422)
        self.assertEqual(mensaje,"no encuentro informacion con esos criterios de busqueda")

    def test_trae_datos(self):
        codigo,datos=ConsultarPropiedades('',2011,'')
        self.assertEqual(codigo,200)



class TestValidarNumero(unittest.TestCase):
    def test_numero_valido(self):
        codigo,mensaje=ValidarNumero(2023)
        self.assertEqual(codigo,1)
        self.assertEqual(mensaje,'success')  
    def test_numero_no_valido(self):
        codigo,mensaje=ValidarNumero('12ww')
        self.assertEqual(codigo,422)
        self.assertEqual(mensaje,"por favor ingrese un numero valido")      
if __name__ == '__main__':
    unittest.main()
