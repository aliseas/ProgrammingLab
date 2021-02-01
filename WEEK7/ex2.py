"""
Implementare una funzione (simile a quella creata le lezioni precedenti) che
ritorni una lista i cui elementi saranno le date delle vendite del file shampoo sales.csv
"""
from datetime import datetime

my_file = open('WEEK7/shampoo_sales.csv','r')
lista_date = []

for line in my_file:
	print('Riga: {}'.format(line))
	elementi_riga = line.split(',')
	print('Elemento importante:{}'.format(elementi_riga[0]))
	if elementi_riga[0] != "Date":
		my_date = datetime.strptime(elementi_riga[0],'%d-%m-%Y')
		lista_date.append(my_date.strftime('%d−%m−%Y'))
print('Lista di elementi: {}'.format(lista_date))

