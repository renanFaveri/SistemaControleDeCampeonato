from abc import ABC, abstractmethod

class Rigidez(ABC):

    @abstractmethod
    def __init__(self, rigidez: str):
        self.__rigidez = rigidez
    
    @property
    def rigidez(self):
        return self.__rigidez
    
    @rigidez.setter
    def rigidez(self, rigidez: str):
        if isinstance(rigidez, str):
            self.__rigidez = rigidez
            
    def __str__(self):
        return self.__rigidez 
