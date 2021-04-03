from .pessoa import Pessoa
from .mentalidade import Mentalidade

class Tecnico(Pessoa):

    def __init__(self, nome, mentalidade: Mentalidade, funcao = 'Técnico', disponivel = True):
        super().__init__(nome, funcao)
        self.__disponivel = disponivel
        if isinstance(mentalidade, Mentalidade):
            self.__mentalidade = mentalidade
        else:
            raise TypeError

    @property
    def mentalidade(self):
        return self.__mentalidade
    
    @mentalidade.setter
    def mentalidade(self, mentalidade):
        if isinstance(mentalidade, Mentalidade):
            self.__mentalidade = mentalidade
            
    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel
            
    def __str__(self):
        return super().__str__() + f'; mentalidade: {self.mentalidade}; disponibilidade: {self.disponivel}'


