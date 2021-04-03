from abc import ABC, abstractmethod

class Mentalidade(ABC):

    @abstractmethod
    def __init__(self, mentalidade: str):
        self.__mentalidade = mentalidade
    
    @property
    def mentalidade(self):
        return self.__mentalidade

    @mentalidade.setter
    def mentalidade(self, mentalidade: str):
        if isinstance(mentalidade, str):
            self.__mentalidade = mentalidade

    def __str__(self):
        return self.__mentalidade
