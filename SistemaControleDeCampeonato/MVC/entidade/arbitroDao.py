from .arbitro import Arbitro
from .dao import DAO

class ArbitroDAO(DAO):

    def __init__(self):
        super().__init__('arbitro.pkl')

    def add(self, arbitro: Arbitro):
        if isinstance(arbitro, Arbitro):
            super().add(arbitro)
