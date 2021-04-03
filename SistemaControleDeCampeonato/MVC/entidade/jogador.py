from .pessoa import Pessoa
from .posicao import Posicao

class Jogador(Pessoa):
    
    def __init__(self, nome, posicao: Posicao, funcao = 'Jogador', gols_marcados = 0, gols_cedidos = 0, disponivel = True):
        super().__init__(nome, funcao)
        self.__gols_marcados = gols_marcados
        self.__gols_cedidos = gols_cedidos
        self.__disponivel = disponivel
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
    def gols_cedidos(self):
        return self.__gols_cedidos
    
    @gols_cedidos.setter
    def gols_cedidos(self, gols_cedidos):
        if isinstance(gols_cedidos, int):
            self.__gols_cedidos = gols_cedidos
    
    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        if isinstance(disponivel, bool):
            self.__disponivel = disponivel
            
    def __str__(self):
        return super().__str__() + f"""; posição: {self.posicao}; gols marcados: {self.__gols_marcados}; gols concedidos: {self.gols_cedidos}; disponibilidade: {self.disponivel}"""

