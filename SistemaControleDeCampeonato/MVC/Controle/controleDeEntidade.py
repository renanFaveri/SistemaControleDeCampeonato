from abc import ABC, abstractmethod

class ControladorDeEntidade(ABC):
    
    @abstractmethod
    def __init__(self):
        self.__tela = None
    
    @property
    @abstractmethod
    def tela(self):
        pass     

    @tela.setter
    @abstractmethod
    def tela(self, tela):
        pass
        
    @abstractmethod
    def cadastrar(self):
        pass
    
    @abstractmethod
    def buscar_nome(self):
        pass
    
    @abstractmethod
    def buscar_id(self):
        pass    
    
    @abstractmethod
    def buscar(self):
        pass
    
    @abstractmethod
    def alterar(self):
        pass
    
    @abstractmethod
    def listar(self):
        pass
    
    @abstractmethod
    def excluir(self):
        pass
    
    @abstractmethod
    def mostrar_informacoes(self):
        pass
    
    @abstractmethod
    def abre_tela(self):
        pass
