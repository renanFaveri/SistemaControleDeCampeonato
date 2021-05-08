from .time import Time
from MVC.exceptionLista import ListaError

class Campeonato:

    def __init__(self, nome, n_times: int, times: list = []):
        self.__id = id(self)
        self.__nome = nome
        self.__n_times = n_times
        self.__times = times
        self.__partidas = []
        self.__estatatisticas = None

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
    def times(self):
        return self.__times
    
    def adicionar_times(self, times: list):
        if isinstance(times, list):
            if (len(times) + len(self.times)) > self.n_times:
                    raise ValueError
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

    @property
    def estatisticas(self):
        return self.__estatisticas

    def gerar_estatisticas(self):
        tabela = """Posição\tTime\t\tPontos | Vitórias | Empates | Derrotas\n"""
        for time in self.times:
            tabela += f"""      {self.times.index(time)+1}\t{time.nome}\t\t{' '*5}{(time.vitorias*3)+(time.empates*1)}{('|'.center(13,' '))}{time.vitorias}\
{('|'.center(16,' '))}{time.empates}{('|'.center(17,' '))}{time.derrotas}\n"""
        self.__estatisticas = tabela
        return self.__estatisticas
    
    def __str__(self):
        return f'Nome: {self.nome}; ID: {self.id_}; Número de times competidores: {len(self.times)}; Capacidade do campeonato: {self.n_times} times'
    