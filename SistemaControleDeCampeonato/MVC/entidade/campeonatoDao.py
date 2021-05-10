from .campeonato import Campeonato
from .dao import DAO

class CampeonatoDAO(DAO):

    def __init__(self):
        super().__init__('campeonato.pkl')

    def add(self, campeonato: Campeonato):
        if isinstance(campeonato, Campeonato):
            super().add(campeonato)