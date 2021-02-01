list1 = [1,5,4,6,10];
list2 = [3,6,3,8,10];

"""
una funzione che stampa il contenuto di una lista passata come
argomento
"""
def stampa(a_list):
	print('List:{}'.format(a_list))

stampa(list1)

"""
 una funzione che riceve una lista e, se `e una lista di interi, ne determina la somma, la media, il minimo ed il massimo degli elementi
"""

def statistiche(a_list):
	ii = 0;
	len_list = len(a_list);
	for i in a_list:
		if isinstance(i,int):
			ii = ii+1;
	if ii == len_list:
		max_list = max(a_list)
		min_list = min(a_list);
		mean_list = sum(a_list)/5;
		print("Max value: {}".format(max_list))
		print("Min value: {}".format(min_list))
		print("Mean value: {}".format(mean_list))
	else:
		print('Not an integer list')

statistiche(list1)

"""
una funzione che riceve in ingresso due liste, determina se sono due liste di interi, se hanno la stessa dimensione e ne
calcola la somma vettoriale, poi ritornata come lista, altrimenti ritorna
una lista vuota;
"""
def somma_vettoriale(a_list,a_list2):
	count = 0; count2 = 0;
	sum_vec = [0,0,0,0,0]
	len_list = len(a_list);
	len_list2 = len(a_list2);
	for i in a_list:
		if isinstance(i,int):
			count = count+1;
	for i2 in a_list2:
		if isinstance(i2,int):
			count2 = count2+1;
	if (count == len_list) and (count2==len_list2) and (count==count2):
		for num,el in enumerate(a_list):
			sum_vec[num] = a_list[num] + a_list2[num];
		print("Vector sum:{}".format(sum_vec))
	else:
		print("Vector sum: []")

somma_vettoriale(list1,list2)

"""
una funzione che riceve in ingresso due liste, determina se sono due liste di interi, se hanno la stessa dimensione, in
caso ne calcola e ne ritorna il prodotto vettoriale, altrimenti ritorna una stringa di avviso ”ATTENZIONE: non sono riuscito a calcolare il prodotto vettoriale”.
"""

def prodotto_vettoriale(a_list,a_list2):
	count = 0; count2 = 0;
	sum_vec = [0,0,0,0,0]
	len_list = len(a_list);
	len_list2 = len(a_list2);
	for i in a_list:
		if isinstance(i,int):
			count = count+1;
	for i2 in a_list2:
		if isinstance(i2,int):
			count2 = count2+1;
	if (count == len_list) and (count2==len_list2) and (count==count2):
		for num,el in enumerate(a_list):
			sum_vec[num] = a_list[num] * a_list2[num];
		print("Vector product:{}".format(sum_vec))
	else:
		print("ATTENZIONE: non sono riuscito a calcolare il prodotto vettoriale")
	
prodotto_vettoriale(list1,list2)





