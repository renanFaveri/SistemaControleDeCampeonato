from .tela import Tela

class TelaDePessoas(Tela):
    
    def __init__(self, controlador):
        super().__init__(controlador, 'Cadastro de pessoas')
