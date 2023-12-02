from funkcje.bfunkcje import *

class CDane:
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik
        
    def czytajl(self):
        return czytaj_liste(self.lista)
    
    def czytajs(self):
        return czytajslownik(self.slownik)
