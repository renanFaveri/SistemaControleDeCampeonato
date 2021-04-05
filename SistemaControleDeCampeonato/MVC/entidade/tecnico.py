from .pessoa import Pessoa
from .mentalidade import Mentalidade


class Tecnico(Pessoa):

    
    def __init__(self, nome, mentalidade: Mentalidade, funcao = 'Técnico', disponivel = True):
        super().__init__(nome, funcao)
        self.__disponivel = disponivel
        self.__time = None
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
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        if isinstance(time, Time):
            self.__time = time
            
    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel
            
    def __str__(self):
        if self.time:
            return super().__str__() + f'; mentalidade: {self.mentalidade}; time atual: {self.time.nome}'
        else:
            return super().__str__() + f'; mentalidade: {self.mentalidade}; Dosponível: {self.disponivel}'


