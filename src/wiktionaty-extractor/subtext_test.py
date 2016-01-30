# -*- coding: UTF-8 -*-
import subtext as sub
import unittest

test_text = u"=== forma verbal y algo === \n ;1: {{forma verbo|regular|p=3p|t=pret ind|m=indicativo|nopron=|leng=esss}}. === {{verbo intransitivo|esss}} ===  \n;1: Desplazarse rápidamente sobre el suelo mediante el movimiento alternado de las piernas o de las patas. \n ;2: Desplazarse rápidamente de cualquier otra forma, un vehículo, cosa o ser. \n:*'''Ejemplos:''' \n ::Mi auto ''corre'' a 290 km por hora. \n::Unas nubecillas ''corrían'' por el cielo. \n;3: Apresurarse en hacer algo. \n:*'''Ejemplo:''' ''Corrió'' a saludar a su madre. \n;4: Tener prisa, estar muy ocupado en una actividad. \n {{sinónimos|ajetrearse|darse prisa}}. \n{{antónimo|relajarse}}. \n === FIN ==="

#test_text = ur" Precontenido === Forma verbal y algo ===  {{fomrma verbal|verbo|tiempo|persona}}   === {{verbo intransitivo|es}} === algo acerca del sustantivo === FIN ==="


#print test_text
 
class TestSubTextProcess(unittest.TestCase) :
    def test1(self) :
	#self.fail(sub.get_contents(test_text))
	print repr(sub.get_contents(test_text))


if __name__ == '__main__':
    unittest.main()

      