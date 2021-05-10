import PySimpleGUI as sgui
from .tela import Tela


class TelaDePessoa(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)
    
    def exibir_menu(self):
        background = '#20660C'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]
        layout = [[sgui.Menu(menu)],
                  [sgui.Text('Cadastro de pessoas', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Frame('', background_color='#06470F', 
                        layout = [[sgui.Radio('Cadastrar pessoa', 'r1', text_color='#FAE98E',background_color='#06470F', size=(25,10), font=('Candara', 16), default=True, key=1),
                  sgui.Radio('Buscar pessoas cadastradas', 'r1', text_color='#FAE98E', background_color='#06470F', size=(30,10), font=('Candara', 16), key=2)]])],
                  [sgui.Button('Confirmar', size=(15,2), font=('Candara', 14), button_color=button_color, pad=((10,10), (30,60))),
                        sgui.Button('Voltar', size=(15, 2), font=('Candara', 14), button_color=button_color, pad=((10,10), (30,60)))]]
        window = sgui.Window('UFSC Programmers League', layout, background_color=background, element_justification='Center', finalize=True, keep_on_top = True)
        self.janela = window
        return

    def menu_cadastrar(self, pessoas_dict_dados):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]
        layout = [[sgui.Menu(menu)],
                  [sgui.Text('Cadastrar pessoa', text_color='#FAE98E', background_color=background, size=(55,2), font=('Candara', 25), justification='center')],
                  [sgui.Text('Marque a caixa da opcao que deseja cadastrar:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Cadastrar jogador', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Column(vertical_alignment='t', background_color='#06470F', size=(1000,40),
                                layout=[[sgui.Radio('Informe o nome do jogador:', 'r1', text_color='white', background_color='#06470F', size=(25,10), font=('Candara', 14), key='jogador'), 
                                sgui.InputText(size=(35,1), font=(16), pad=((25,20),0), key='jogador_nome'),
                                sgui.Combo(pessoas_dict_dados['posicoes'], default_value='Escolha a posição do jogador', font=(12), size=(30,1), readonly=True, key='posicao')]])]])],
                  [sgui.Frame('Cadastrar técnico', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Radio('Informe o nome do técnico:', 'r1', text_color='white',background_color='#06470F', size=(25,10), font=('Candara', 14), key='tecnico'), 
                                sgui.InputText(size=(35,1), font=(16), pad=((25,20),0), key=('tecnico_nome')),
                                sgui.Combo(pessoas_dict_dados['mentalidades'], default_value='Escolha a mentalidade do técnico', font=(12), size=(30,1), readonly=True, key='mentalidade')]])]])],
                  [sgui.Frame('Cadastrar árbitro', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Radio('Informe o nome do árbitro:', 'r1', text_color='white',background_color='#06470F', size=(25,10), font=('Candara', 14), key='arbitro'), 
                                sgui.InputText(size=(35,1), font=(16), pad=((25,20),0), key=('arbitro_nome')),
                                sgui.Combo(pessoas_dict_dados['rigidez'], default_value='Escolha a rigidez do árbitro', font=(12), size=(30,1), readonly=True, key='rigidez')]])]])],
                  [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))),
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]]
        window = sgui.Window('', layout, background_color=background, element_justification='left', finalize=True, keep_on_top = True)
        self.janela = window
        return

    def menu_buscar(self, lista_jogadores, lista_tenicos, lista_arbitros):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]
        layout = [[sgui.Menu(menu)],
                  [sgui.Text('Buscar pessoa', text_color='#FAE98E', background_color=background, size=(55,2), font=('Candara', 25), justification='center')],
                  [sgui.Text('Marque a opcao que deseja buscar, digite o nome ou escolha uma pessoa da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Buscar jogador', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Column(vertical_alignment='t', background_color='#06470F', size=(1000,40),
                                layout=[[sgui.Radio('Informe o nome do jogador:', 'r1', text_color='white', background_color='#06470F', size=(25,10), font=('Candara', 14), key='jogador'), 
                                sgui.InputText(size=(35,1), font=(16), pad=((25,20),0), key='in_jnome'),
                                sgui.Combo(sorted(lista_jogadores), default_value='Escolha um jogador da lista', font=(12), size=(30,1), readonly=True, key='lst_jnome')]])]])],
                  [sgui.Frame('Cadastrar técnico', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Radio('Informe o nome do técnico:', 'r1', text_color='white',background_color='#06470F', size=(25,10), font=('Candara', 14), key='tecnico'), 
                                sgui.InputText(size=(35,1), font=(16), pad=((25,20),0), key=('in_tnome')),
                                sgui.Combo(sorted(lista_tenicos), default_value='Escolha um técnico da lista', font=(12), size=(30,1), readonly=True, key='lst_tnome')]])]])],
                  [sgui.Frame('Cadastrar árbitro', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Radio('Informe o nome do árbitro:', 'r1', text_color='white',background_color='#06470F', size=(25,10), font=('Candara', 14), key='arbitro'), 
                                sgui.InputText(size=(35,1), font=(16), pad=((25,20),0), key=('in_anome')),
                                sgui.Combo(sorted(lista_arbitros), default_value='Escolha um árbitro da lista', font=(12), size=(30,1), readonly=True, key='lst_anome')]])]])],
                  [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))),
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]]
        window = sgui.Window('', layout, background_color=background, element_justification='left', finalize=True, keep_on_top = True)
        self.janela = window
        return

    def janela_jogador(self, jogador_dict_dados, lista_posicoes):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')

        stats = f"""Nome:\t\t\t{jogador_dict_dados['nome']}
Função:\t\t\t{jogador_dict_dados['funcao']}
Posição:\t\t\t{jogador_dict_dados['posicao']}
Time:\t\t\t{jogador_dict_dados['time']}
Gols marcados:\t\t\t{jogador_dict_dados['gols_m']}
Gols concedidos:\t\t\t{jogador_dict_dados['gols_c']}"""

        header = [[sgui.Column(layout=[[sgui.Text(jogador_dict_dados['nome'].upper(), text_color=text, background_color='#06470F', 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]
        nome = [sgui.Frame('Alterar nome do jogador', font=('Candara', 12,'bold'), pad=(40,(30,10)),
                        layout=[[sgui.Column(vertical_alignment='c', background_color='#06470F', size=(1000,60), 
                                layout=[[sgui.Text('Nome:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(default_text=jogador_dict_dados['nome'], size=(40,1), font=(16), pad=((25,20),0), key=('nome_jogador'))]])]],
                        title_color='#FAE98E', background_color='#06470F')]
        posicao = [sgui.Frame('Alterar posição do jogador', font=('Candara', 12,'bold'), pad=(40,(10,30)),
                        layout=[[sgui.Column(vertical_alignment='c', background_color='#06470F', size=(1000,60), 
                                layout=[[sgui.Text('Posição:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.Combo(lista_posicoes, default_value=jogador_dict_dados['posicao'], font=(16), pad=((25,20),0), size=(40,1), readonly=True, key='posicao')]])]],
                        title_color='#FAE98E', background_color='#06470F')]
        estatisticas = [sgui.Multiline(stats, text_color='white', font=(14), background_color=background, size=(50,11), no_scrollbar=True, disabled=True)]
        frame_estatisticas = [sgui.Frame('Estatísticas', layout = [estatisticas], pad=(60,20), title_color='#FAE98E', background_color='#06470F')]
        frame_cadastro = [sgui.Frame('', layout = [nome, posicao], background_color=background)]
        frame_dados = [sgui.Frame('', layout = [frame_estatisticas], background_color='#06470F')]
        botao_excluir = [sgui.Button('Aposentar-se', size=(14,2), font=('Candara', 14), pad=(0,30), border_width=2, focus=True, button_color=('white', 'dark red'), key='excluir')]

        coluna = [sgui.Column(layout = [frame_cadastro] + [frame_dados] + [botao_excluir], element_justification='center', background_color=background, 
                scrollable=True, vertical_scroll_only=True)]

        layout = header +  [coluna]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.janela = window
        return

    def janela_tecnico(self, tecnico_dict_dados, lista_mentalidades):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')

        header = [[sgui.Column(layout=[[sgui.Text(tecnico_dict_dados['nome'].upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]

        nome = [sgui.Frame('Alterar nome do técnico', font=('Candara', 12,'bold'), pad=(40,(30,5)),
                        layout=[[sgui.Column(vertical_alignment='c', background_color='#06470F', size=(1000,60), 
                                layout=[[sgui.Text('Nome:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(default_text=tecnico_dict_dados['nome'], size=(40,1), font=(16), key=('nome_tecnico'))]])]],
                        title_color='#FAE98E', background_color='#06470F')]

        mentalidade = [sgui.Frame('Alterar mentalidade do técnico', font=('Candara', 12,'bold'), pad=(40,(5,30)),
                        layout=[[sgui.Column(vertical_alignment='c', background_color='#06470F', size=(1000,60), 
                                layout=[[sgui.Text('Mentalidade:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.Combo(lista_mentalidades, default_value=tecnico_dict_dados['mentalidade'], font=(16), size=(40,1), readonly=True, key='mentalidade')]])]],
                        title_color='#FAE98E', background_color='#06470F')]   
        frame_cadastro = [sgui.Frame('', layout = [nome, mentalidade], background_color=background)] 
        botao_excluir = [sgui.Button('Aposentar-se', size=(14,2), font=('Candara', 14), pad=(0,30), border_width=2, focus=True, button_color=('white', 'dark red'), key='excluir')]
        coluna = [sgui.Column(layout = [frame_cadastro] + [botao_excluir], element_justification='center', background_color=background, 
                scrollable=True, vertical_scroll_only=True)]
        layout = header +  [coluna]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.janela = window
        return

    def janela_arbitro(self, arbitro_dict_dados, lista_rigidez):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        header = [[sgui.Column(layout=[[sgui.Text(arbitro_dict_dados['nome'].upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]
        nome = [sgui.Frame('Alterar nome do árbitro', font=('Candara', 12,'bold'), pad=(40,(30,5)),
                        layout=[[sgui.Column(vertical_alignment='c', background_color='#06470F', size=(1000,60), 
                                layout=[[sgui.Text('Nome:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(default_text=arbitro_dict_dados['nome'], size=(40,1), font=(16), key=('nome_arbitro'))]])]],
                        title_color='#FAE98E', background_color='#06470F')]

        rigidez = [sgui.Frame('Alterar rigidez do árbitro', font=('Candara', 12,'bold'), pad=(40,(5,30)),
                        layout=[[sgui.Column(vertical_alignment='c', background_color='#06470F', size=(1000,60), 
                                layout=[[sgui.Text('Rigidez:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.Combo(lista_rigidez, default_value=arbitro_dict_dados['rigidez'], font=(16), size=(40,1), readonly=True, key='rigidez')]])]], 
                        title_color='#FAE98E', background_color='#06470F')]
        frame_cadastro = [sgui.Frame('', layout = [nome, rigidez], background_color=background)]
        botao_excluir = [sgui.Button('Aposentar-se', size=(14,2), font=('Candara', 14), pad=(0,30), border_width=2, focus=True, button_color=('white', 'dark red'), key='excluir')]
        coluna = [sgui.Column(layout = [frame_cadastro] + [botao_excluir], element_justification='center', background_color=background, 
                scrollable=True, vertical_scroll_only=True)]
        layout = header +  [coluna]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.janela = window
        return
