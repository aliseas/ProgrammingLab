"""
Estendere la classe CSVFile che avete creato la scorsa lezione, aggiungendo
i seguenti metodi
"""

class CSVFile():
	def __init__(self,name):
		self.name = name;
	
	def get_data(self,name,start,end):
		if start>end:
			raise Exception('Start value cannot be > end value')
		my_file = open(name,'r')
		with open(name, "r") as file:
			my_file = file.readlines()[start:end]
		lista = []
		for line in my_file:
			print('Riga: {}'.format(line))
			elementi_riga = line.split(',')
			if elementi_riga[1] != "Sales\n":
				lista.append(float(elementi_riga[1]))
		print('Lista di elementi: {}'.format(lista))
		
		diff_data = [];
		for i in range(len(lista)-1):
			diff_data.append(abs(lista[i+1]-lista[i]))
		
		file.close()
		return lista,diff_data
	
	def get_date_vendite(self,name):
		from datetime import datetime
		my_file = open(name,'r')
		lista_date = []
		
		for line in my_file:
			elementi_riga = line.split(',')
			if elementi_riga[0] != "Date":
				my_date = datetime.strptime(elementi_riga[0],'%d-%m-%Y')
				lista_date.append(my_date.strftime('%d−%m−%Y'))
		print('Lista di elementi: {}'.format(lista_date))
		my_file.close()
	
	def __str__(self,name):
		my_file = open(name,'r')
		for line in my_file:
			elementi_riga = line.split(',')
			if elementi_riga[0] == "Date":
				print('Intestazione file: {}'.format(line))
				break
		my_file.close()

class Model():
	def __init__(self,name):
		self.name = name
	def fit(self):
		raise NotImplementedError('This model does not have a fit')
	def predict(self,prev_months):
		file = CSVFile(self.name)
		data,differences = file.get_data(self.name,0,prev_months)
		prediction = (sum(differences)/len(differences))+data[-1]
		return prediction

file = CSVFile('WEEK7/shampoo_sales.csv')
print(file.name)
lista_dati,lista_diff = file.get_data('WEEK7/shampoo_sales.csv',0,30)
print('\nLista dati: {}'.format(lista_dati))
print('\nLista differenze: {}'.format(lista_diff))

modello_shampoo = Model(file.name)
prediction = modello_shampoo.predict(20)
print(prediction)

#Visualising the data
from matplotlib import pyplot
pyplot.plot(lista_dati,color="tab:blue")
pyplot.plot(lista_dati + [prediction],color="tab:red")
pyplot.show()