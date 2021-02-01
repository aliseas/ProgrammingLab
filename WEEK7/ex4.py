"""
Implementare una classe Automobile che presenta i seguenti attributi:
casa auto, modello, numero posti, numero portiere, kw, targa. Inoltre, la
presente classe deve comprendere i seguenti metodi
"""
class Automobile():
	#ATTRIBUTI
	def __init__(self,casa_auto,modello,numero_posti,numero_portiere,kw,targa,categoria):
		self.casa_auto = casa_auto
		self.modello = modello
		self.numero_posti = numero_posti
		self.numero_portiere = numero_portiere
		self.kw = kw
		self.targa = targa 
		self.categoria = categoria

	#METODI
	def __str__(self):
		print("INFORMAZIONI AUTO:")
		print("\nCasa:{},".format(self.casa_auto))
		print("\nModello:{},".format(self.modello))
		print("\nN_posti:{},".format(self.numero_posti))
		print("\nN_portiere:{},".format(self.numero_portiere))
		print("\nKw:{},".format(self.kw))
		print("\nTarga:{}".format(self.targa))

	def parla(self):
		print("\nBroom broom")
	
	def bollo(self):
		if (self.categoria == 'Euro0') and (self.kw<=100):
			prezzo = 3;
		elif (self.categoria == 'Euro0') and (self.kw>100):
			prezzo = 4.5;
		elif (self.categoria == 'Euro1') and (self.kw<=100):
			prezzo = 2.5;
		elif (self.categoria == 'Euro1') and (self.kw>100):
			prezzo = 4.35;
		elif (self.categoria == 'Euro2'):
			prezzo = 3;
		
		b = self.kw * prezzo;
		print("\nBollo auto: {}".format(b))
	
	def confronta(self,another_auto):
		if(self.casa_auto == another_auto.casa_auto) and (self.modello == another_auto.modello) and (self.numero_posti == another_auto.numero_posti) and (self.numero_portiere == another_auto.numero_portiere) and(self.kw == another_auto.kw):
			print("\nLe automobili hanno le stesse informazioni")
		else:
			print("\nLe automobili NON hanno le stesse informazioni")

auto = Automobile('Fiat','500',4,2,500,'FM32056','Euro1')
auto.__str__()
auto.parla()
auto.bollo()
auto2 = Automobile('Fiat','Panda',4,2,500,'FM32058','Euro1')
Automobile.confronta(auto,auto2);

