from .pessoa import Pessoa
from .mentalidade import Mentalidade

class Tecnico(Pessoa):

    
    def __init__(self, nome, mentalidade: Mentalidade, funcao = 'Técnico'):
        super().__init__(nome, funcao)
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
        if self.__time == None:
            return ''
        else:
            return self.__time

    @time.setter
    def time(self, time):
        from .time import Time
        if isinstance(time, Time) or time == None:
            self.__time = time
            
    def __str__(self):
        if self.__time:
            return super().__str__() + f'; mentalidade: {self.mentalidade}; time atual: {self.time.nome}'
        else:
            return super().__str__() + f'; mentalidade: {self.mentalidade}; time atual: sem time'

           