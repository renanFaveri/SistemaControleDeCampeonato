from .time import Time
from .arbitro import Arbitro
#from MVC.exceptionVazia import EntradaVaziaError
#from MVC.exceptionTime import TimeIncompletoError

class Partida:
    
    def __init__(self, time_anfitriao, time_visitante, arbitro_designado, data_do_jogo = None, sumula = None):
        self.__id = id(self)
        self.__time_anfitriao = time_anfitriao
        self.__time_visitante = time_visitante
        self.__arbitro_designado = arbitro_designado
        self.__data_do_jogo = data_do_jogo
        self.__jogada = False
        self.__sumula = sumula
        self.__placar = None
        self.__relatorio = None
        self.__tela_final = None

        
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
    def data_do_jogo(self):
        return self.__data_do_jogo
    
    @data_do_jogo.setter
    def data_do_jogo(self, data_do_jogo):
        self.__data_do_jogo = data_do_jogo
        
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
    def tela_final(self):
        return self.__tela_final

    @tela_final.setter
    def tela_final(self, tela_final):
        from MVC.limite.telaDePartidas import TelaDePartidas
        if isinstance(tela_final, TelaDePartidas):
            self.__tela_final = tela_final
    
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
        