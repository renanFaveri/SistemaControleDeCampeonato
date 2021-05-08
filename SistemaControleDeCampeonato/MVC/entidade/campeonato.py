from .time import Time
from MVC.exceptionLista import ListaError
from MVC.exceptionCampeonatoCompleto import CampeonatoCompletoError

class Campeonato:

    def __init__(self, nome, n_times: int, times: list = []):
        self.__id = id(self)
        self.__nome = nome
        self.__n_times = n_times
        self.__times = times
        self.__partidas = []
        self.__tabela = None

    def dict_dados(self):
        return {'id': self.__id, 'nome': self.__nome, 'n_times': self.__n_times, 'times': [time.nome for time in self.__times], 'tabela': self.gerar_tabela()}

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
            raise TypeError

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
    def times(self):
        return self.__times
    
    def adicionar_times(self, times: list):
        if isinstance(times, list):
            if (len(times) + len(self.times)) > self.n_times:
                    raise CampeonatoCompletoError()
            for time in times:                
                if not isinstance(time, Time):
                    raise TypeError
            self.times.extend(times)
            return True
        else:
            raise ListaError()

    def remover_times(self, times: list):
        if isinstance(times, list):
            for time in times:
                if not isinstance(time, Time):
                    raise TypeError
                elif time not in self.times:
                    raise ValueError
                else:
                    self.times.remove(time)
            return True
        else:
            raise ListaError()

    @property
    def partidas(self):
        return self.__partidas

    def gerar_tabela(self):
        lista = sorted(self.times, key=lambda time: time.vitorias*3+time.empates, reverse=True)
        tabela = 'Posição'.center(10, ' ') + '\t' + 'Time'.center(20, ' ') + '\t' + '\t' + '\t' + 'Pts      |      V      |      E      |      D      ' + '\n' + '-'*105 + '\n'
        for i in range(len(lista)):
            tabela += f'{i+1}'.center(16, ' ') + '\t' + f'{lista[i].nome}'.center(16, ' ') + '\t' + '\t' + '\t' +\
                f'  {lista[i].vitorias*3 + lista[i].empates}       |      {lista[i].vitorias}      |      {lista[i].empates}      |      {lista[i].derrotas}      ' + '\n'
        self.__tabela = tabela
        return self.__tabela
    
    def __str__(self):
        return f'Nome: {self.nome}; ID: {self.id_}; Número de times competidores: {len(self.times)}; Capacidade do campeonato: {self.n_times} times'
    