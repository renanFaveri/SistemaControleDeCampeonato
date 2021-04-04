from .ControleDePessoa import ControladorDePessoas
from .controleDeTime import ControladorDeTimes
from .controleDeCampeonato import ControladorDeCampeonatos
from MVC.limite.telaInicial import TelaInicial


class ControladorDeSistemas():
    
    def __init__(self):
        self.__controlador_pessoas = ControladorDePessoas(self)
        self.__controlador_times = ControladorDeTimes(self)
        self.__controlador_campeonatos = ControladorDeCampeonatos(self)
        self.__tela = TelaInicial(self)
        
    def iniciar(self):
        #jogando = True
        while True:
            menu = ['1 - Cadastro de pessoas', '2 - Cadastro de times','3 - Cadastro de campeonatos', '0 - Sair']
            opcoes = {1: self.cp.abre_tela, 2: self.ct.abre_tela, 3: self.cc.abre_tela}
            opcao = self.tela.exibir_menu(menu, range(4))
            if opcao != 0:
                opcoes[opcao]()
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
        
    
