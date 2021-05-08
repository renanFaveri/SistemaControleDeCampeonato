from .tecnico import Tecnico
from .dao import DAO

class TecnicoDAO(DAO):
    def __init__(self):
        super().__init__('tecnico.pkl')

    def add(self, tecnico: Tecnico):
        if isinstance(tecnico, Tecnico):
            super().add(tecnico)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)

    def atualizar (self, tecnico: Tecnico):
        if isinstance(tecnico, Tecnico):
            super().atualiza(tecnico)
