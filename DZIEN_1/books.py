class Book:
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def create_book(self)->float:
        print("utworzono nowy obiekt klasy Book...")

    def print_book(self):
        print(f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena}, oprawa: {self.oprawa}")

    def rabat(self,procent):
        return self.cena*procent/100

    def setoprawa(self,nowaoprawa):
        self.oprawa = nowaoprawa

    @property
    def cena(self):
        return self._cena

    @cena.setter
    def cena(self,nowacena):
        self._cena = nowacena


b1 = Book(32,"Wiedźmin","Andrzej Sapkowski",38)
#b1.oprawa = "twarda"
print(b1.cena)
b1.setoprawa("twarda")
b1.cena=45
b1.print_book()
print(f'rabat: {b1.rabat(12)}zł')

b2 = Book(47,"Hobbit","J.R.R. Tolkien",40)
b2.print_book()

class Encyklopedia(Book):
    def __init__(self, id, tytul, autor, wydawnictwo, nazwa, cena=30):
        super().__init__(id, tytul, autor, cena)
        self.wydawnictwo = wydawnictwo
        self.nazwa = nazwa

    def liczbatomow(self,n):
        print(f'liczba towmów encykopedii -> {n}')

    def rabat(self, procent):
        return super().rabat(procent*1.5)


print("_"*50)
e1 = Encyklopedia(67,"Encykopedia wiedzy technicznej","Janek Nowak","ABC",
                "Encyklopedia Informatyki",156)

e1.cena = 188

e1.print_book()
e1.liczbatomow(6)
print(f'rabat: {e1.rabat(10)}zł')
