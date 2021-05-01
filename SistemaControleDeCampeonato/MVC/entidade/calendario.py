class Calendario:
    
    def __init__(self, data_inicial, data_final):
        self.__data_inicial = data_inicial
        self.__data_final = data_final
        self.__calendario_jogos = None
        
    @property
    def data_inicial(self):
        return self.__data_inicial
    
    @data_inicial.setter
    def data_inicial(self, data_inicial):

        self.__data_inicial = data_inicial
        
    @property
    def data_final(self):
        return self.__data_final
    
    @data_final.setter
    def data_final(self, data_final):

        self.__data_final = data_final
        
    @property
    def calendario(self):
        return self.__calendario
    
    def definir_calendario(self, data_inicial, data_final):
        pass

    