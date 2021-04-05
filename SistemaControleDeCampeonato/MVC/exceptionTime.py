class TimeIncompletoError(ValueError):
    
    def __init__(self, mensagem = 'O time não possui o número mínimo de jogadores.'):
        super().__init__(mensagem)
