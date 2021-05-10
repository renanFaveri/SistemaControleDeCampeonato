from .pessoa import Pessoa
from .posicao import Posicao

class Jogador(Pessoa):

    def __init__(self, nome, posicao: Posicao, funcao = 'Jogador', time = None):
        super().__init__(nome, funcao)
        self.__gols_marcados = 0
        self.__gols_concedidos = 0
        self.__time = time
        if isinstance(posicao, Posicao):
            self.__posicao = posicao
        else:
            raise TypeError
                  
    @property
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, posicao):
        if isinstance(posicao, Posicao):
            self.__posicao = posicao
        else:
            raise TypeError
    
    @property
    def gols_marcados(self):
        return self.__gols_marcados
    
    @gols_marcados.setter
    def gols_marcados(self, gols_marcados):
        if isinstance(gols_marcados, int):
            self.__gols_marcados = gols_marcados
    
    @property
    def gols_concedidos(self):
        return self.__gols_concedidos
    
    @gols_concedidos.setter
    def gols_concedidos(self, gols_concedidos):
        if isinstance(gols_concedidos, int):
            self.__gols_concedidos = gols_concedidos

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
            return super().__str__() + f"""; posição: {self.posicao}; time atual: {self.time.nome}; gols marcados: {self.__gols_marcados}; gols concedidos: {self.gols_concedidos}"""
        else:
            return super().__str__() + f"""; posição: {self.posicao}; time atual: sem time; gols marcados: {self.__gols_marcados}; gols concedidos: {self.gols_concedidos}"""


