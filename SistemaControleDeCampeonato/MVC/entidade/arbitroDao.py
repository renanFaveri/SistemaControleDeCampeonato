from .arbitro import Arbitro
from .dao import DAO

class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__('arbitro.pkl')

    def add(self, arbitro: Arbitro):
        if isinstance(arbitro, Arbitro):
            super().add(arbitro)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)

    def atualizar (self, arbitro: Arbitro):
        if isinstance(arbitro, Arbitro):
            super().atualiza(arbitro)
