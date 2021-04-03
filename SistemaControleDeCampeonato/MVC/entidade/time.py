from .tecnico import Tecnico

class Time:
    
    def __init__(self, nome):
        self.__id = id(self)
        self.__nome = nome
        self.__classificacao = None
        self.__jogadores = []
        self.__tecnico = None
        self.__vitorias = 0
        self.__empates = 0
        self.__derrotas = 0
        self.__gols_marcados = 0
        self.__gols_sofridos = 0
    
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
    def classificacao(self):
        return self.__classificacao
    
    @classificacao.setter
    def classificacao(self, classificacao):
        if isinstance(classificacao, int):
            self.__classificacao = classificacao
    
    @property
    def jogadores(self):
        return self.__jogadores
    
    @property
    def tecnico(self):
        return self.__tecnico
    
    @tecnico.setter
    def tecnico(self, tecnico: Tecnico):
        if isinstance(tecnico, Tecnico):
            self.__tecnico = tecnico
            
    @property
    def vitorias(self):
        return self.__vitorias
    
    @vitorias.setter
    def vitorias(self, vitorias: int):
        if isinstance(vitorias, int):
            self.__vitorias = vitorias
            
    @property
    def empates(self):
        return self.__empates
    
    @empates.setter
    def empates(self, empates):
        if isinstance(empates, int):
            self.__empates = empates
    
    @property
    def derrotas(self):
        return self.__derrotas
    
    @derrotas.setter
    def derrotas(self, derrotas):
        if isinstance(derrotas, int):
            self.__derrotas = derrotas
    
    @property
    def gols_marcados(self):
        return gols_marcados
    
    @gols_marcados.setter
    def gols_marcados(self, gols_marcados):
        if isinstance(gols_marcados, int):
            self.__gols_marcados = gols_marcados
            
    @property
    def gols_sofridos(self):
        return self.__gols_sofridos
    
    @gols_sofridos.setter
    def gols_sofridos(self, gols_sofridos):
        if isinstance(gols_sofridos, int):
            self.__gols_sofridos = gols_sofridos
