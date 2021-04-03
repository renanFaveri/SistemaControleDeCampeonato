from abc import ABC, abstractmethod

class Posicao(ABC):

    @abstractmethod
    def __init__(self, posicao: str):
        self.__posicao = posicao

    @property
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, posicao):
        if isinstance(posicao, str):
            self.__posicao = posicao
            
    def __str__(self):
        return self.__posicao
    


