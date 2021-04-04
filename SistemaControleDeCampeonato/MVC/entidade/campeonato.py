from .time import Time
from .calendario import Calendario


class Campeonato:
    
    def __init__(self, nome, n_times: int, times: list = [], calendario: Calendario = None):
        self.__id = id(self)
        self.__nome = nome
        self.__n_time = n_times
        self.__times = times
        self.__partidas = []
        self.__calendario = calendario
        self.__estatatisticas = estatisticas
        
    @property
    def id_(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
            
    @property
    def n_times(self):
        return self.__n_times
    
    @n_times.setter
    def n_times(self, n_times):
        if isinstance(n_times, int):
            if n_times > 1:
                self.__n_times = n_times
            else:
                raise ValueError
            
    @property
    def calendario(self):
        return self.__calendario
    
    @calendario.setter
    def calendario(self, calendario):
        if isinstance(calendario, Calendario):
            self.__calendario = calendario
    
    @property
    def times(self):
        return self.__times
    
    def adicionar_times(self, times: list):
        if isinstance(times, list):
            for time in times:
                if not isinstance(time, Time):
                    raise TypeError
            if (len(times) + len(self.times)) > self.n_times:
                raise ValueError
            else:
                self.times.extend(times)
        else:
            raise ListaError
                    
    def remover_times(self, times: list):
        if isinstance(times, list):
            for time in times:
                if not isinstance(time, Time):
                    raise TypeError
                elif time not in self.times:
                    raise ValueError
                else:
                    self.times.remove(time)
        else:
            raise ListaError
    
    @property
    def partidas(self):
        return self.__partidas
    
    @property
    def estatisticas(self):
        return self.__estatisticas
    
    
    def __str__(self):
        return f'Nome: {self.nome}; Número de times competidores: {len(self.times)}; Capacidade do campeonato: {self.n_times} times'
    
    
