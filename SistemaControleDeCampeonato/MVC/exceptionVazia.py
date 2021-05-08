class EntradaVaziaError(Exception):
    
    def __init__(self, mensagem = 'Não foi passado valor.'):
        super().__init__(mensagem)
