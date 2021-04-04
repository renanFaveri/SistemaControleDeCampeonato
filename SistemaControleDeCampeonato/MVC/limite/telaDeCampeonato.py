from .tela import Tela

class TelaDeCampeonatos(Tela):
    
    def __init__(self, controlador):
        super().__init__(controlador, 'Cadastro de campeonatos')
