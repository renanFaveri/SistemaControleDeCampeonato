from .pessoa import Pessoa
from .rigidez import Rigidez

class Arbitro(Pessoa):
    
    def __init__(self, nome, rigidez: Rigidez, funcao = 'Árbitro'):
        super().__init__(nome, funcao)
        if isinstance(rigidez, Rigidez):
            self.__rigidez = rigidez
        else:
            raise TypeError

    @property
    def id(self):
        return self.__id
        
    @property
    def rigidez(self):
        return self.__rigidez
    
    @rigidez.setter
    def rigidez(self, rigidez: Rigidez):
        if isinstance(rigidez, Rigidez):
            self.__rigidez = rigidez
            
    def __str__(self):
        return super().__str__() + f'; rigidez: {self.rigidez}'