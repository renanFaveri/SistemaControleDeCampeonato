class CapacidadeMaximaError(Exception):

   def __init__(self, mensagem = 'O cadastro já está com sua capacidade máxima.'):
        super().__init__(mensagem)      
