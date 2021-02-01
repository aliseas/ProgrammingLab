"""
Esercizio 5:
Modelli
"""

import statistics
import numpy as np
from scipy.stats import pearsonr

#3 studenti
#percorso di 2500km complessivamente
#vogliono stimare quanto spenderanno a testa in benzina

class LinearModel():
    #ATTRIBUTI
    def __init__(self):
        self.angular_coeff = None
        self.intercept = None
        self.train_data = None
    #METODI
    def fit(self,train_data):
        self.train_data = train_data
        P = pearsonr(train_data[0],train_data[1])
        Pxy = P[0]
        print("Pxy = {}".format(Pxy))#correlazione di Pearson
        sx = np.std(train_data[0],ddof=1)
        print("sx = {}".format(sx))
        sy = np.std(train_data[1],ddof=1)
        print("sy = {}".format(sy))
        self.angular_coeff = Pxy*((sy/sx))
        print("sy/sx: {}".format(sy/sx))
        print("Angular coeff: {}".format(self.angular_coeff))
        if(self.angular_coeff is None):
            raise Exception("Angular coefficient not yet defined")
        elif(self.train_data is None):
            raise Exception("Train Dataset not yet defined")
        else:
            print("Mean km: {}".format(np.mean(train_data[0])))
            print("Mean lt: {}".format(np.mean(train_data[1])))
            self.intercept = np.mean(train_data[1]) - (self.angular_coeff*np.mean(train_data[0]))
            print("intercept = {}".format(self.intercept))
    
    def predict(self,xp):
        y = (self.angular_coeff*xp) + self.intercept
        return y

km_percorsi = np.array([833,987,883,378,84,483,835,646,508,90])
lt_benzina = np.array([37,41.6,37.2,15.2,3.4,19.6,35.1,28.9,22.6,3.7])
dataset = np.array([[833,987,883,378,84,483,835,646,508,90],[37,41.6,37.2,15.2,3.4,19.6,35.1,28.9,22.6,3.7]])

data_model = LinearModel()
data_model.fit(dataset)
benzina = data_model.predict(2500)
print("Consumo benzina predetto: {}".format(benzina))
costo_persona = (benzina * 1.4)/3.00
print("Costo a persona: {}".format(costo_persona))