import PySimpleGUI as sgui


class TelaInicial:
    
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__janela = None

    @property
    def janela(self):
        return self.__janela

    @janela.setter
    def janela(self, janela):
        if isinstance(janela, sgui.Window):
            self.__janela = janela
        else:
            raise TypeError

    @property
    def ctrl(self):
        return self.__controlador


    def abreTela(self):
        return self.__janela.Read()


    def fechaTela(self):
        return self.__janela.Close()


    def exibir_menu(self):
        background = '#20660C'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]

        layout = [[sgui.Menu(menu)],
                  [sgui.Text('UFSC Programmers League', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Button('Cadastro de pessoas', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('cp')),
                        sgui.Button('Cadastro de times', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('ct')),
                        sgui.Button('Cadastro de campeonato', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('cc'))],
                  [sgui.Button('Jogar partidas e campeonatos', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((0,0), (30,0)), key=('jpc'))],
                  [sgui.Image(r'Img\\sem_titulo.png', pad=((0,0), (30,0)))],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('UFSC Programmers League', layout, background_color=background, element_justification='Center', finalize=True, size=(994, 800), keep_on_top = True)
        self.__janela = window
        return