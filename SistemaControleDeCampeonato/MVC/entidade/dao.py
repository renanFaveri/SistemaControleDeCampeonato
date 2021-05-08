import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    @property
    def cache(self):
        return self.__cache

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, obj):
        self.__cache.append(obj)
        self.__dump()

    def get(self, key):
        while self.__cache.index(g) != key:
            g =+ 1
        return self.__cache(g)

    def remove(self, key):
        while self.__cache.index(r) != key:
            r =+ 1
        self.__cache.pop(r)
        self.__dump()

    def get_all(self):
        return self.__cache.values()

    def atualiza(self, obj):
        self.__dump()
