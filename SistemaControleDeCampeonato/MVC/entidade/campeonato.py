class Campeonato:
    
    def __init__(self, nome, times: list, calendario):
        self.__id = id(self)
        self.__nome = nome
        self.__times = []
        self.__calendario
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
    def calendario(self):
        return self.__calendario
    
    @calendario.setter
    def calendario(self, calendario):
        if isinstance(calendario, Calendario):
            self.__calendario = calendario
    
    @property
    def times(self):
        return self.__times
    
    @property
    def partidas(self):
        return self.__partidas
    
    @property
    def estatisticas(self):
        return self.__estatisticas
    
