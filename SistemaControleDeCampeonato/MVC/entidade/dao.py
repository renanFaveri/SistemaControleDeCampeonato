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
        with open(self.__datasource, 'wb') as source:
            pickle.dump(self.__cache, source)
        
    def __load(self):
        with open(self.__datasource,'rb') as source:
            self.__cache = pickle.load(source)

    def add(self, obj):
        self.__cache.append(obj)
        self.__dump()
        
    def get(self, obj):
        for i in range(len(self.__cache)):
            if self.__cache[i].id_ == obj.id_:
                return self.__cache[i]

    def remover_e_retornar(self, obj):
        objeto = self.get(obj)
        self.__cache.remove(objeto)
        self.__dump()
        return objeto
    
    def carregar(self):
        return self.__load()

    def atualizar_objeto(self, obj):
        for i in range(len(self.__cache)):
            if self.__cache[i].id_ == obj.id_:
                self.__cache[i] = obj
                self.__dump()
                return
  



