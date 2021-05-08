from .time import Time
from .dao import DAO

class TimeDAO(DAO):
    def __init__(self):
        super().__init__('times.pkl')

    def add(self, time: Time):
        if isinstance(time, Time):
            super().add(time)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)

    def atualizar (self, time: Time):
        if isinstance(time, Time):
            super().atualiza(time)