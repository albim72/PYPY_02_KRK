import math
from figura import Figura

class Kolo(Figura):
    """
    to jest klasa opisująca figurę: Koło
    metody: policz_pole
    """
    def __init__(self,a):
        super().__init__(a, 0)

    def policz_pole(self):
        """
        metoda policz_pole
        :return: pi*r**2
        """
        return math.pi*self.a**2
        
    
