from .time import Time
from .dao import DAO

class TimeDAO(DAO):

    def __init__(self):
        super().__init__('time.pkl')

    def add(self, time: Time):
        if isinstance(time, Time):
            super().add(time)