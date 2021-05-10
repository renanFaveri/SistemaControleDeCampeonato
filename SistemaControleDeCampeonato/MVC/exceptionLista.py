class ListaError(Exception):
    
    def __init__(self):
        super().__init__('O parâmetro deve conter uma lista.')
