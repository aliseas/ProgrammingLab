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
	def fit(self,start,end):
		file = CSVFile(self.name)
		data,differences = file.get_data(self.name,start,end)
		overall_average_increment = (sum(differences)/len(differences))
		return overall_average_increment
		#raise NotImplementedError('This model does not have a fit')
	def predict(self,predict_start,predict_end,fit_start,fit_end):
		file = CSVFile(self.name)
		file_model = Model(file.name)
		overall_parameter = file_model.fit(fit_start,fit_end)
		data,differences = file.get_data(self.name,predict_start,predict_end)
		end_parameter = (sum(differences)/len(differences))
		prediction = data[-1] + ((end_parameter+overall_parameter)/2)
		return prediction

file = CSVFile('WEEK7/shampoo_sales.csv')
lista_dati,lista_diff = file.get_data('WEEK7/shampoo_sales.csv',0,36)
print('\nLista dati: {}'.format(lista_dati))
print('\nLista differenze: {}'.format(lista_diff))

modello_shampoo = Model(file.name)

"""
#Visualising the data
from matplotlib import pyplot
#visualising model with fit predictions
pyplot.plot(lista_dati + [prediction_with_fit],color="tab:red")

pyplot.show()
"""

#Training and testing dataset and visualisation
training_model = Model('WEEK7/shampoo_sales.csv')
prediction_testing = training_model.predict(25,35,0,24)
print("Actual data: {}".format(lista_dati[-1]))
print("Predicted data: {}".format(prediction_testing))
error = abs(lista_dati[-1]-prediction_testing)
print("Error: {}".format(error))

""""
pyplot.plot(lista_dati + [prediction_testing],color="tab:green")
pyplot.plot(lista_dati,color="tab:blue")
pyplot.show()

"""