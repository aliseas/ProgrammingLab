"""
exercise one: 
Eccezioni e sanitizzazione:
Un androide deve simulare il comportamento umano dell’atto di vestirsi
"""
#INIZIO
print("Starting to run your script")

import random

#Funzione per una generica azione di indossare un indumento
def indossare(capo_vestiario):
    #value = 1
    value = random.randint(0,1)
    if(round(value) == 1):
        #capo_vestiario = True
        print("L'automa dice: 'Sono riuscito a indossare un capo'")
        return(1)
    else:
        print("L'automa dice: 'Non riesco a indossarlo!'")
        raise Exception("L'automa non è riuscito a vestirsi")
        return(0)


#Funzione per vestire l'automa
def esegui(automa,capo):
    automa_list = dir(automa)
    if(capo in automa_list):
        attribute = getattr(automa,capo)
        if(attribute == True ):#controllo che non sia già addosso
            print("Stai già indossando {}".format(capo))
            return
        else:#altrimenti glielo faccio indossare
            if(capo == 'biancheria'):
                automa.biancheria_on()
            elif(capo == 'calzini'):
                automa.calzini_on()
            elif(capo == 'maglia'):
                automa.maglia_on()
            elif(capo == 'pantaloni'):
                automa.pantaloni_on()
            else:
                automa.calzatura_on()

#Creo l'androide con i suoi attributi e metodi
class Automa():
    """
    Questa classe rappresenta un androide, i suoi capi di vestiario (attributi) e le azioni che gli permettono di indossare ciascuno di essi (metodi)
    """
    #ATTRIBUTI
    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None

    #METODI
    #indossare la biancheria
    def biancheria_on(self):
        indossare(self.biancheria)
    #indossare i calzini
    def calzini_on(self):
        indossare(self.calzini)
    #indossare la maglia
    def maglia_on(self):
        indossare(self.maglia)
    #indossare i pantaloni
    def pantaloni_on(self):
        indossare(self.pantaloni)
    #indossare la calzatura
    def calzatura_on(self):
        indossare(self.calzatura)

un_automa = Automa() #abbiamo un automa di nome un_automa
capi_vestiario_ordinati = ['biancheria','calzini','maglia','pantaloni','calzatura']
vestito = True

#Vestiamo l'automa:
indice_precedente = -1
while(vestito):
    print("L'automa dice: 'Sto scegliendo un capo...'")
    capo_scelto = random.choice(capi_vestiario_ordinati)
    indice_capo = capi_vestiario_ordinati.index(capo_scelto)
    #print("L'indice è {}".format(indice_capo))
    if(indice_capo == indice_precedente + 1):
        print("Mi sto mettendo {}".format(capo_scelto))
        esegui(un_automa,capo_scelto)
        indice_precedente += 1
        if(indice_capo == 4):
            print("L'automa dice: 'Finalmente ho finito, mi sono vestito!''")
            vestito = False
        else:
            pass
    else:
        print("L'automa dice: 'Ho scelto il capo sbagliato'")
        continue

print("Automa vestito correttamente")

#THE END
print("I ran your script successfully")
