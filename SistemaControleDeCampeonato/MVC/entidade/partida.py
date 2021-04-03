from .time import Time
from .arbitro import Arbitro

class Partida:
    
    def __init__(self, time_anfitriao, time_visitante, arbitro_designado, data_do_jogo, relatorio = None):
        self.__id = id(self)
        self.__time_anfitriao = time_anfitriao
        self.__time_visitante = time_visitante
        self.__arbitro_designado = arbitro_designado
        self.__data_do_jogo = data_do_jogo
        self.__relatorio = relatorio
        
    @property
    def id_(self):
        return self.__id
    
    @property
    def time_anfitriao(self):
        return self.__time_anfitriao
    
    @time_anfitriao.setter
    def time_anfitriao(self, time_anfitriao):
        if isinstance(time_anfitriao, Time):
            self.__time_anfitriao = time_anfitriao
    
    @property
    def time_visitante(self):
        return self.time_visitante
    
    @time_visitante.setter
    def time_visitante(self, time_visitante):
        if isinstance(time_visitante, Time):
            self.__time_visitante = time_visitante
            
    @property
    def arbitro_designado(self):
        return self.__arbitro_designado
    
    @arbitro_designado.setter
    def arbitro_designado(self, arbitro_designado):
        if isinstance(arbitro_designado, Arbitro):
            self.__arbitro_designado = arbitro
            
    @property
    def data_do_jogo(self):
        return self.__data_do_jogo
    
    @data_do_jogo.setter
    def data_do_jogo(self, data_do_jogo):
        ######## fazer conferencia
        self.__data_do_jogo = data_do_jogo
        
    @property
    def relatorio(self):
        return self.__relatorio
    
    def criar_relatorio(self):
        pass
    