class CSVFile():
	def __init__(self,name):
		self.name = name;
	
	def get_data(self,name):
		try:
			my_file = open(name,'r')
		except Exception as error:
			print('Errore: "{}"'.format(error));
			import sys
			sys.exit()

		lista = []
		for line in my_file:
			print('Riga: {}'.format(line))
			elementi_riga = line.split(',')
			print('Elemento importante:{}'.format(elementi_riga[1]))
			if elementi_riga[1] != "Sales\n":
				lista.append(float(elementi_riga[1]))
		print('Lista di elementi: {}'.format(lista))
		
		sum = 0;
		for i in lista:
			sum = sum + i;
		print('Somma: {}'.format(sum))
		
		my_file.close()

file = CSVFile('shampoo_finto.csv')
print(file.name)
file.get_data('shampoo_finto.csv')