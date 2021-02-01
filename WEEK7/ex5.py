"""
Estendere l’esercizio 04 realizzando la sottoclasse Transformer della classe
Automobile. La sottoclasse `e caratterizzata dai seguenti attributi e metodi.
"""
#SUPERCLASSE
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

#SOTTOCLASSE
class Transformer(Automobile):
	#ATTRIBUTI
	def __init__(self,nome,generazione,grado,fazione,reparto):
		self.nome = nome
		self.generazione = generazione
		self.grado = grado
		self.fazione = fazione
		self.reparto = reparto

	#METODI
	def parla(self):
		if self.fazione == 'Autobot':
			print("Noi siamo Autobots, proteggeremo ogni essere vivente")
		else:
			 print('Noi siamo Decepticons e l’AllSpark sarà nostro!')
	
	def scheda_militare(self):
		print("INFORMAZONI TRANSFORMER:")
		print("Nome:{}".format(self.nome))
		print("Generazione:{}".format(self.generazione))
		print("Grado:{}".format(self.grado))
		print("Fazione:{}".format(self.fazione))
		print("Reparto:{}".format(self.reparto))


trans1 = Transformer('Jerry','1','soldato_semplice','Autobot','artiglieria pesante');
trans1.parla()
trans1.scheda_militare()

if issubclass(Transformer, Automobile):
	print("Automobile is superclass")
print("{}".format(type(trans1)))
if isinstance(trans1, Transformer):
	print("trans1 is of class Transformer")