from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x = x

    def msg(self):
        print("to jest wynik działania metody nieabstrakcyjnej!")

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*7


class Regular(Prototyp):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return self.y-0.06*self.x

    def policz_x(self):
        return super().policz_x() + 21*self.y


reg = Regular(1,5)
print(f'funkcja policz: {reg.policz()}')
print(f'funkcja policz_x: {reg.policz_x()}')

