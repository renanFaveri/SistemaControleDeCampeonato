from .partida import Partida
from .dao import DAO

class PartidasDAO(DAO):

    def __init__(self):
        super().__init__('partidas.pkl')

    def add(self, partida: Partida):
        if isinstance(partida, Partida):
            super().add(partida)
    
    def extend(self, lista):
        for partida in lista:
            self.add(partida)
