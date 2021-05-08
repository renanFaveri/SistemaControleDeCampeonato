from .time import Time
from .arbitro import Arbitro



class Partida:
    
    def __init__(self, time_anfitriao, time_visitante, arbitro_designado, sumula = None):
        self.__id = id(self)
        self.__time_anfitriao = time_anfitriao
        self.__time_visitante = time_visitante
        self.__arbitro_designado = arbitro_designado
        self.__jogada = False
        self.__sumula = sumula
        self.__placar = None
        self.__relatorio = None

    
    def dict_dados(self):
        return {'id': self.__id, 'ta': self.__time_anfitriao.nome, 'tv': self.__time_visitante.nome, 'arb': self.__arbitro_designado.nome, 'jogada': self.__jogada, 'sumula': self.__sumula,
                    'placar': self.placar, 'relatorio': self.__relatorio, 'txt_relatorio': self.txt_relatorio() if self.__relatorio != None else ''}


    def txt_relatorio(self):
        relatorio_anf = [tupla for tupla in self.__relatorio if tupla[0].time is self.__time_anfitriao]
        text_anf = ""
        for tupla in relatorio_anf:
            text_anf += f"{tupla[0].nome} - gol aos {tupla[1]}'\n"
        relatorio_vis = [tupla for tupla in self.__relatorio if tupla[0].time is self.__time_visitante]
        text_vis = ""
        for tupla in relatorio_vis:
            text_vis += f"{tupla[0].nome} - gol aos {tupla[1]}'\n"
        return text_anf, text_vis


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
            return True
        else:
            raise TypeError
    
    @property
    def time_visitante(self):
        return self.__time_visitante
    
    @time_visitante.setter
    def time_visitante(self, time_visitante):
        if isinstance(time_visitante, Time):
            self.__time_visitante = time_visitante
            return True
        else:
            raise TypeError

    @property
    def placar(self):
        if self.__placar == None:
            return '0 x 0'
        else:
            return self.__placar
    
    @placar.setter
    def placar(self, placar):
        self.__placar = placar
            
    @property
    def arbitro_designado(self):
        return self.__arbitro_designado
    
    @arbitro_designado.setter
    def arbitro_designado(self, arbitro_designado):
        if isinstance(arbitro_designado, Arbitro):
            self.__arbitro_designado = arbitro_designado
            return True
        else:
            raise TypeError
     
    @property
    def jogada(self):
        return self.__jogada
    
    @jogada.setter
    def jogada(self, jogada):
        if isinstance(jogada, bool):
            self.__jogada = jogada

    @property
    def relatorio(self):
        return self.__relatorio
    
    @relatorio.setter
    def relatorio(self, relatorio):
        if isinstance(relatorio, list):
            self.__relatorio = relatorio
    
    @property
    def sumula(self):
        return self.__sumula
    
    def gerar_sumula(self, relatorio_jog_gols):
        sumula = f"""
        {self.__str__()} 
        Início da partida:       
        """
        for tupla in relatorio_jog_gols:
            txt = f"""
            Gol marcado por {tupla[0].nome} a favor de {tupla[0].time.nome} aos {tupla[1]}'
            """
            sumula += txt
        sumula += """
        Fim da partida."""
        self.__sumula = sumula
        return sumula 
    
    def __str__(self):
        return f"""Partida: id {self.id_}: 
{self.time_anfitriao.nome.upper()} {self.placar} {self.time_visitante.nome.upper()}
Árbitro: {self.arbitro_designado.nome}"""
            