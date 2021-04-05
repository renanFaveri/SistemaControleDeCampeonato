from abc import ABC, abstractmethod
from MVC.exceptionCaracter import CaracterEspecialError

 
class Tela(ABC):
    
    @abstractmethod
    def __init__(self, controlador, titulo_tela = ''):
        self.__controlador = controlador
        self.__titulo_tela = titulo_tela.center(40, '_')
        
    @property
    def titulo_tela(self):
        return self.__titulo_tela
    
    @titulo_tela.setter
    def titulo_tela(self, titulo_tela):
        if isinstance(titulo_tela, str):
            self.__titulo_tela = titulo_tela
            
    def exibir_menu(self, menu, opcoes_validas):
        print('\n' + self.titulo_tela + '\n')
        print("Escolha o número da opção desejada:")
        for op in menu:
            print(op)
        opcao = self.recebe_int('Opção: ', opcoes_validas)
        return opcao
            
    def recebe_int(self, mensagem, opcoes_validas = None):
        while True:
            resposta = input(f'\n{mensagem}: ')
            try:
                resposta = int(resposta)
                if opcoes_validas and resposta not in opcoes_validas:
                        raise ValueError
                return resposta
            except ValueError:
                print('»»»» Escolha uma opção válida!\n')
                
    def recebe_str(self, mensagem, tamanho_valido = 3):
        while True:
            resposta = input(f'{mensagem}: ')
            try:
                aux = ''
                resposta = resposta.split()
                for n in resposta:
                    aux += n + ' '
                resposta = aux.strip().title()
                for char in resposta.upper():
                    if not (65 <= ord(char) <= 90 or ord(char) == 32):
                        raise CaracterEspecialError
                if tamanho_valido and len(resposta) < tamanho_valido:
                        raise ValueError
                print('Entrada:', resposta)
                return resposta
            except ValueError:
                print(f'»»»» O nome completo deve ter ao menos {tamanho_valido} caracteres!\n')
            except CaracterEspecialError:
                print(f'»»»» O nome não deve conter caracteres especiais!\n')
                
    def mostrar_mensagem(self, mensagem):
        print(mensagem)
    
