"""
MOVING AVERAGE COMPITO
"""
import numpy as np

class ExamException(Exception):
    pass

class MovingAverage():
    #ATTRIBUTI
    def __init__(self,n_finestra):
        self.finestra = n_finestra

    #METODI
    def compute(self,lista_valori):
        means = []
        #eccezione 1: lista valori è stringa
        if(isinstance(lista_valori,str)):
            raise ExamException("Invalid input: Lista is not a list or array but a string")
        #eccezione 3: lista valori è vuota
        elif(len(lista_valori)==0):
            raise ExamException("Invalid input: Lista vuota")
        #eccezione 2: lunghezza lista minore della finestra
        elif(len(lista_valori)<self.finestra):
            raise ExamException("Invalid input: Lista is shorter than window")
        else:
            window_means = 0
            for i in range(len(lista_valori)-(self.finestra-1)):
                #print(len(lista_valori))
                temp_mean = np.mean(lista_valori[i:i+(self.finestra)])
                #print(temp_mean)
                means.append(temp_mean)
                #print(window_means)
            temp_mean = [] #resetting mean to empty
        
        #total_average = window_means/i
        return means

moving_average = MovingAverage(4)
#result = moving_average.compute([])
#result = moving_average.compute([2,4,8,16])
result = moving_average.compute([2,4,8,16,32])
print(result)