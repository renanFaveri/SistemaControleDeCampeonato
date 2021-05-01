from .pessoa import Pessoa
from .posicao import Posicao
from .time import Time

class Jogador(Pessoa):
    
    def __init__(self, nome, posicao: Posicao, funcao = 'Jogador', time = None, gols_marcados = 0, gols_concedidos = 0, disponivel = True):
        super().__init__(nome, funcao)
        self.__gols_marcados = gols_marcados
        self.__gols_concedidos = gols_concedidos
        self.__disponivel = disponivel
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
            return super().__str__() + f"""; posição: {self.posicao}; time atual: {self.time.nome}; gols marcados: {self.__gols_marcados}; gols concedidos: {self.gols_concedidos}"""
        else:
            return super().__str__() + f"""; posição: {self.posicao}; Disponível: {self.disponivel}; gols marcados: {self.__gols_marcados}; gols concedidos: {self.gols_concedidos}"""

