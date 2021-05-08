from .jogador import Jogador
from .dao import DAO

class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogador.pkl')

    def add(self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            super().add(jogador)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)

    def atualizar (self, jogador: Jogador):
        if isinstance(jogador, Jogador):
            super().atualiza(jogador)
