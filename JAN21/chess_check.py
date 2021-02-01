"""
esercizio 2:
Volete implementare un’ IA che giochi a scacchi.
"""
import re

pattern = '^[RDTAC]?x?[a-h][1-8]$'

#FUNZIONE CHE CONTROLLA CHE LE MOSSE SIANO SINTATTICAMENTE VALIDE
def check_chess_syntax(text):
    #l'input deve essere una stringa
    if(isinstance(text,str)):
        #l'input è esattamente "0-0" o "0-0-0"
        if((text=='0-0') or (text=='0-0-0')):
            print('Input valido')
            return
         #l'input è scritto nel modo corretto
        elif(re.match(pattern,text) is not None):
            print('Input valido')
            return
        else:
            raise Exception("Invalid input")
    #se non si supera una di queste condizioni, funzione raise Exception
    else:
        raise Exception("Problem encountered: The input is not a string")

text = "Rxc7"
check_chess_syntax(text)