from .tecnico import Tecnico
from .dao import DAO

class TecnicoDAO(DAO):

    def __init__(self):
        super().__init__('tecnico.pkl')

    def add(self, tecnico: Tecnico):
        if isinstance(tecnico, Tecnico):
            super().add(tecnico)