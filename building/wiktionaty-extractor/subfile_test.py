# -*- coding: UTF-8 -*-
import subfile as sub
import unittest

test_text = ur"=== Forma verbal === \n ;1: {{forma verbo|reguilar|p=3p|t=pret ind|m=indicativo|nopron=|leng=es}}. \n === {{verbo intransitivo|es}} ===  \n;1: Desplazarse rápidamente sobre el suelo mediante el movimiento alternado de las piernas o de las patas. \n ;2: Desplazarse rápidamente de cualquier otra forma, un vehículo, cosa o ser. \n:*'''Ejemplos:''' \n ::Mi auto ''corre'' a 290 km por hora. \n::Unas nubecillas ''corrían'' por el cielo. \n;3: Apresurarse en hacer algo. \n:*'''Ejemplo:''' ''Corrió'' a saludar a su madre. \n;4: Tener prisa, estar muy ocupado en una actividad. \n {{sinónimos|ajetrearse|darse prisa}}. \n{{antónimo|relajarse}}. \n === FIN ==="

#test_text = " "

#print test_text
 
class TestSubTextProcess(unittest.TestCase) :
    def test1(self) :
	self.assertEqual(sub.get_contents(test_text),u"<title>aléman</title>")


if __name__ == '__main__':
    unittest.main()

      