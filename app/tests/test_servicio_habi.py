import unittest
from app.services.prueba_habi_service import ValidarString,ConsultarPropiedades

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
        codigo,mensaje=ConsultarPropiedades(5,2021,'')
        self.assertEqual(codigo,422)
        self.assertEqual(mensaje,"no encuentro informacion con esos criterios de busqueda")

    def test_trae_datos(self):
        codigo,datos=ConsultarPropiedades('',2011,'')
        self.assertEqual(codigo,200)
        diccionario_prueba=[
    {
        "property_id": 2,
        "description": "Amplio apartamento en conjunto cerrado",
        "address": "carrera 100 #15-90",
        "city": "bogota",
        "price": 350000000,
        "status_name": "en_venta"
    },
    {
        "property_id": 5,
        "description": "Amplio apartamento en conjunto cerrado",
        "address": "carrera 100 #15-90",
        "city": "medellin",
        "price": 325000000,
        "status_name": "en_venta"
    },
    {
        "property_id": 57,
        "description": "Amplio apartamento en conjunto cerrado",
        "address": "carrera 100 #15-90e",
        "city": "medellin",
        "price": 325000000,
        "status_name": "en_venta"
    },
    {
        "property_id": 54,
        "description": "Amplio apartamento en conjunto cerrado",
        "address": "carrera 100 #15-90w",
        "city": "bogota",
        "price": 350000000,
        "status_name": "pre_venta"
    }   
    ]
        self.assertDictEqual(datos,diccionario_prueba)
if __name__ == '__main__':
    unittest.main()
