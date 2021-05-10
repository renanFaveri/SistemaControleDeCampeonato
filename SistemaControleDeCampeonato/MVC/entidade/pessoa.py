from abc import ABC, abstractmethod
from MVC.exceptionVazia import EntradaVaziaError

class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome, funcao):
        self.__id = id(self)
        self.__nome = nome
        self.__funcao = funcao

    @property
    def id_(self):
        return self.__id        
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            if len(nome) > 0:
                self.__nome = nome
            else:
                raise EntradaVaziaError()
        else:
            raise TypeError
    
    @property
    def funcao(self):
        return self.__funcao
    
    @funcao.setter
    def funcao(self, funcao):
        if isinstance(funcao, str):
            self.__funcao =  funcao       
    
    def __str__(self):
        return f"""Nome: {self.nome}; ID: {self.__id}; função: {self.funcao}"""

