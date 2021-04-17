class PecasCubo:
    def __converte_peca(self, peca):
        posicoes = list(map(lambda x: int(x),peca[0].split()))
        cores = peca[1].split()
        return [posicoes, cores]

    def get_pecas(self):
        pecas = []
        for atributo, valor in self.__dict__.items():
            pecas.append(self.__converte_peca(valor))
        return pecas

class QuinasCubo(PecasCubo):
    def __init__(self):
        self.__quina1 = ("0 9 38", "W O B")
        self.__quina2 = ("2 29 36", "W R B")
        self.__quina3 = ("8 27 20", "W R G")
        self.__quina4 = ("6 11 18", "W O G")
        self.__quina5 = ("51 15 44", "Y O B")
        self.__quina6 = ("53 35 42", "Y R B")
        self.__quina7 = ("47 33 26", "Y R G")
        self.__quina8 = ("45 17 24", "Y O G")
    
    

class LadosCubo(PecasCubo):
    def __init__(self):
        self.__lado1 = ("3 10", "W O")
        self.__lado2 = ("1 37", "W B")
        self.__lado3 = ("5 28", "W R")
        self.__lado4 = ("7 19", "W G")
        self.__lado5 = ("12 41", "O B")
        self.__lado6 = ("39 32", "B R")
        self.__lado7 = ("30 23", "R G")
        self.__lado8 = ("21 14", "G O")
        self.__lado9 = ("48 16","Y O")
        self.__lado10 = ("52 43", "Y B")
        self.__lado11 = ("50 34", "Y R")
        self.__lado12 = ("46 25", "Y G")

class CentroCubo(PecasCubo):
    def __init__(self):
        self.__white = ("4", "W")
        self.__orange = ("13", "O")
        self.__green = ("22", "G")
        self.__red = ("31", "R")
        self.__blue = ("40", "B")
        self.__yellow = ("49", "Y")

    

quinas = QuinasCubo()
print(quinas.get_pecas())
lados  = CentroCubo()
print(lados.get_pecas())
#print(quinas.converte_quina(quinas.quina1))