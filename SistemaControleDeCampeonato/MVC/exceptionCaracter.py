class CaracterEspecialError(Exception):
    
    def __init__(self, mensagem = 'Comando inválido. Apenas caracteres de A a Z disponíveis.'):
        super().__init__(mensagem)
