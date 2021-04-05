from .tela import Tela

class TelaDePartidas(Tela):
    
    def __init__(self, controlador):
        super().__init__(controlador, 'Cadastro de campeonatos')
        
        
    def mostrar_tela_partida(self, partida):
        print(f'{partida}'.center(40,'*'))
