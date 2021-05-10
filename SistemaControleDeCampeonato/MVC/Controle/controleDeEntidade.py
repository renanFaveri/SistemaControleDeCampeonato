from abc import ABC, abstractmethod

class ControladorDeEntidade(ABC):

    @abstractmethod
    def __init__(self, controlador_master):
        self.__tela = None
        self.__controlador = controlador_master
    
    @property
    @abstractmethod
    def tela(self):
        pass

    @property
    def cm(self):
        return self.__controlador

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
    def abre_tela(self):
        pass
    