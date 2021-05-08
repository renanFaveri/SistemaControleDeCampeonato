from MVC.exceptionLista import ListaError
from MVC.exceptionVazia import EntradaVaziaError
from .jogador import Jogador
from .tecnico import Tecnico

class Time:
  
    def __init__(self, nome, cor_primaria = None, cor_secundaria = None): 
        self.__id = id(self)
        self.__nome = nome
        self.__cor_primaria = cor_primaria
        self.__cor_secundaria = cor_secundaria
        self.__classificacao = None
        self.__jogadores = []
        self.__max_jogadores = 11
        self.__min_jogadores = 2
        self.__tem_goleiro = False
        self.__tecnico = None
        self.__vitorias = 0
        self.__empates = 0
        self.__derrotas = 0
        self.__gols_marcados = 0
        self.__gols_sofridos = 0


    def dict_dados(self):
        return {'id': self.__id, 'nome': self.__nome, 'cor_p': self.__cor_primaria, 'cor_s': self.__cor_secundaria, 'classificacao': self.__classificacao, 
                    'jogadores': [(jogador.nome, jogador.posicao.posicao, jogador.gols_marcados) for jogador in self.__jogadores], 'tecnico': self.__tecnico.nome if self.__tecnico != None else '', 
                    'vitorias': self.__vitorias, 'empates': self.__empates, 'derrotas': self.__derrotas, 'gols_m': self.__gols_marcados, 'gols_s': self.__gols_sofridos}
    
    @property
    def id_(self):
        return self.__id   
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            if len(nome) > 0:
                self.__nome = nome
            else:
                raise EntradaVaziaError()
        else:
            raise TypeError()
    
    @property
    def cor_primaria(self):
        return self.__cor_primaria

    @cor_primaria.setter
    def cor_primaria(self, cor):
        if isinstance(cor, str):
            self.__cor_primaria = cor

    @property
    def cor_secundaria(self):
        return self.__cor_secundaria

    @cor_secundaria.setter
    def cor_secundaria(self, cor):
        if isinstance(cor, str):
            self.__cor_secundaria = cor

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
    def max_jogadores(self):
        return self.__max_jogadores
    
    @property
    def min_jogadores(self):
        return self.__min_jogadores
    
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
        return self.__gols_marcados
    
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
            
    def adicionar_jogadores(self, jogadores: list):
        if isinstance(jogadores, list):
            if (len(jogadores) + len(self.jogadores)) > self.max_jogadores:
                raise ValueError
            else:
                for jogador in jogadores:
                    if not isinstance(jogador, Jogador):
                        raise TypeError
                    else:
                        self.jogadores.append(jogador)
                        jogador.time = self
                        jogador.disponivel = False
                return True
        else:
            raise ListaError()
                    
    def remover_jogadores(self, jogadores: list):
        if isinstance(jogadores, list):
            for jogador in jogadores:
                if not isinstance(jogador, Jogador):
                    raise TypeError
                elif jogador not in self.jogadores:
                    raise ValueError
                else:
                    jogador.time = None
                    jogador.disponivel = True
                    self.jogadores.remove(jogador)
            return True
        else:
            raise ListaError()
    
    def __str__(self):
        if self.tecnico:
            return f'Nome: {self.nome}; ID: {self.id_}; técnico: {self.tecnico.nome}; classificação: {self.classificacao}; Número de jogadores no time: {len(self.jogadores)}'
        else:
            return f'Nome: {self.nome}; ID: {self.id_}; técnico: {self.tecnico}; classificação: {self.classificacao}; Número de jogadores no time: {len(self.jogadores)}'

        