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
			#print(''.format(my_file))
		lista = []
		for line in my_file:
			print('Riga: {}'.format(line))
			elementi_riga = line.split(',')
			if elementi_riga[1] != "Sales\n":
				lista.append(float(elementi_riga[1]))
		print('Lista di elementi: {}'.format(lista))
		
		sum = 0;
		for i in lista:
			sum = sum + i;
		
		print('Somma: {}'.format(sum))
		file.close()
	
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


file = CSVFile('WEEK7/shampoo_sales.csv')
print(file.name)
file.get_data('WEEK7/shampoo_sales.csv',50,60)
#file.get_date_vendite('WEEK7/shampoo_sales.csv')
#file.__str__('WEEK7/shampoo_sales.csv')