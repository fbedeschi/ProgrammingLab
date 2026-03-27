class Poligono():
    def __init__(self,lati):
        self.lati = lati

    def __str__(self):
        return f"sono un poligono di {self.lati} lati"

class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)
    def __str__(self):
        return f"Sono un quadrilatero"
class Rettangolo(Quadrilatero):
    def __init__(self,base,altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza
    def __str__(self):
        return f"sono un rettangolo di base {self.base}, e di altezza {self.altezza}"

    def perimetro(self):
        return (2*self.base)+(2*self.altezza)
    def area (self):
        return self.base*self.altezza
class Triangolo(Poligono):
    def __init__(self,lato1,lato2,lato3):
        super().__init__(3)
        self.lato1=lato1
        self.lato2=lato2
        self.lato3=lato3

    def __str__(self):
        return f"sono un triangolo e i miei lati sono {self.lato1,self.lato2,self.lato3}"

    def perimetro(self):
        return self.lato3+self.lato2+self.lato1
    
    def is_equilatero(self):
        if self.lato1==self.lato2 and self.lato2==self.lato3:
            return True
        return False
