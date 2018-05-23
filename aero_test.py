import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):

	def test_aerolinea_1(self):
		"""CE0: Ejemplo
		Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 4, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1540.00)

	def test_aerolinea_2(self):
		"""Vuelo internacional,Sudamerica,2 adultos y 1 nino , Enero,economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 1, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 1, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Sudamerica', 1, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total=calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,997.5)

	def test_aerolinea_3(self):
		"""Vuelo internacional,Sudamerica,2 adultos y 1 nino , Mayo,economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 5, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 5, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Sudamerica', 5, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total=calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,1045)

	def test_aerolinea_4(self):
		"""Vuelo internacional,Sudamerica,2 adultos y 1 nino , Septiembre,economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 9, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 9, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Sudamerica', 9, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total=calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,1064)
	
	def test_aerolinea_5(self):
		"""Vuelo internacional,Sudamerica,2 adultos y 1 nino , Septiembre,economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Oceania', 9, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Oceania', 9, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Oceania', 9, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total=calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,1000)

if __name__ == '__main__':
	unittest.main()
