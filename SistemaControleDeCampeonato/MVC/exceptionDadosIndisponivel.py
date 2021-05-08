class DadoIndisponivelError(Exception):

    def __init__(self):
        super().__init__('Já existe um cadastro com essas informações')