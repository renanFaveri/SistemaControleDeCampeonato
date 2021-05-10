from .ControleDePessoa import ControladorDePessoas
from .controleDeTime import ControladorDeTimes
from .controleDeCampeonato import ControladorDeCampeonatos
from .controleJogarCampeonato import JogarCampeonato
from MVC.limite.telaInicial import TelaInicio
from MVC.limite.tela import Tela


class ControladorDeSistemas:

    def __init__(self):
        self.__controlador_pessoas = ControladorDePessoas(self)    
        self.__controlador_times = ControladorDeTimes(self)            
        self.__controlador_campeonatos = ControladorDeCampeonatos(self)
        self.__jogar_campeonato = JogarCampeonato(self)
        self.__tela = TelaInicio(self)
        
    def iniciar(self):
        while True:
            opcoes = {'cp': self.cp.abre_tela, 'ct': self.ct.abre_tela, 'cc': self.cc.abre_tela, 'jpc': self.jc.abre_tela}
            self.tela.exibir_menu()
            botao, valores = self.tela.abreTela()
            self.tela.fechaTela()
            if botao in opcoes:
                opcoes[botao]()
            else:
                return
        
    @property
    def tela(self):
        return self.__tela
    
    @tela.setter
    def tela(self, tela):
        if isinstance(tela, Tela):
            self.__tela = tela
    
    @property
    def cp(self):
        return self.__controlador_pessoas
    
    @property
    def ct(self):
        return self.__controlador_times
    
    @property
    def cc(self):
        return self.__controlador_campeonatos
    
    @property
    def jc(self):
        return self.__jogar_campeonato
        
    