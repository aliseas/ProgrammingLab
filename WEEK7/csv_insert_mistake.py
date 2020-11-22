my_file = open('WEEK7/shampoo_sales.csv', 'a');
my_file.write('01-01-2015, ');
my_file.write('01-02-2015,ciao');
my_file.close()

class CSVFile():
	def __init__(self,name):
		self.name = name;
	
	def get_data(self,name):
		my_file = open(name,'r')
		lista = []
		for line in my_file:
			print('Riga: {}'.format(line))
			elementi_riga = line.split(',')
			print('Elemento importante:{}'.format(elementi_riga[1]))
			try:
				float(elementi_riga[1])
			except Exception as e:
				print('Ho trovato un errore: "{}"'.format(e))
				print('Salterò questa riga!')
				continue

			lista.append(float(elementi_riga[1]))
		print('Lista di elementi: {}'.format(lista))
		
		sum = 0;
		for i in lista:
			sum = sum + i;
		print('Somma: {}'.format(sum))
		
		my_file.close()

file = CSVFile('WEEK7/shampoo_sales.csv')
print(file.name)
file.get_data('WEEK7/shampoo_sales.csv')