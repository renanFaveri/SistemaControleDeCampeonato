class ListaError(Exception):
    
    def __init__(self, mensagem = 'O parâmetro deve ser uma lista.'):
        super().__init__(mensagem)
