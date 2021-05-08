import PySimpleGUI as sgui

class TelaDePessoas:
    
    def __init__(self, controlador):
        self.__controlador: controlador
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
                  [sgui.Text('Cadastro de pessoas', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Frame('', background_color='#06470F', 
                        layout = [[sgui.Radio('Cadastrar pessoa', 'r1', text_color='#FAE98E',background_color='#06470F', size=(25,10), font=('Candara', 16), default=True, key=1),
                  sgui.Radio('Buscar pessoas cadastradas', 'r1', text_color='#FAE98E', background_color='#06470F', size=(30,10), font=('Candara', 16), key=2)]])],
                  [sgui.Button('Confirmar', size=(15,2), font=('Candara', 14), button_color=button_color, pad=((10,10), (30,60))),
                        sgui.Button('Voltar', size=(15, 2), font=('Candara', 14), button_color=button_color, pad=((10,10), (30,60)))]]
        window = sgui.Window('UFSC Programmers League', layout, background_color=background, element_justification='Center', finalize=True, keep_on_top = True)
        self.__janela = window
        return

    def tela_cadastrar_pessoas(self, pessoas_dict_dados):
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
        self.__janela = window
        return

    def menu_buscar_pessoas(self, lista_jogadores, lista_tenicos, lista_arbitros):
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
        self.__janela = window
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
        frame_estatisticas = [sgui.Frame('Estatísticas', layout = [estatisticas], title_color='#FAE98E', background_color='#06470F')]
        frame_cadastro = [sgui.Frame('', layout = [nome, posicao], background_color=background)]
        frame_dados = [sgui.Frame('', layout = [frame_estatisticas], background_color='#06470F')]
        botao_excluir = [sgui.Button('Aposentar-se', size=(14,2), font=('Candara', 14), pad=(0,30), border_width=2, focus=True, button_color=('white', 'dark red'), key='excluir')]
        layout = header +  [frame_cadastro] + [frame_dados] + [botao_excluir]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
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
        layout = header +  [frame_cadastro] + [botao_excluir]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
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
        layout = header +  [frame_cadastro] + [botao_excluir]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
        return

    def popup_msg_erro_cadastro(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Preencha os campos corretamente.', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Text('Escolha novamente.', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Button('OK', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, pad=(0,20))]]
        window = sgui.Window('Cartão Amarelo!'.upper(), layout, titlebar_font=('Candara', 14, 'bold'), background_color='#F3EE44', element_justification='Center', force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return

    def popup_confirmar_cadastro(self, dados):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Confirmar a criação do seguinte cadastro: {dados[1]} {dados[2]} {dados[0]}?', size=(0,1), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Confirmar cadastro', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def popup_cadastro_criado(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Cadastro criado!', size=(40,1), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')]]
        window = sgui.Window('ok', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, 
                keep_on_top=True, auto_close=True, auto_close_duration=1)
        botao, valores = window.Read()
        window.Close()
        return botao

    def popup_confirmar_alteracao(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Foram feitas alterações no cadastro.\n Confirmar essas alterações?', size=(35,3), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Confirmar alterações', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao


    def popup_msg_excluir(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Você tem certeza que deseja excluir esse cadastro?', text_color='white', background_color='#ce221e', font=('Candara', 16, 'bold'))],
                  [sgui.Text('A exclusão será irreversível!', text_color='white', background_color='#ce221e', font=('Candara', 16, 'bold'))],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=('white', 'black'), pad=(10,20)),
                    sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=('white', 'black'), pad=(10,20))]] 
        window = sgui.Window('Cartão Vermelho!'.upper(), layout, titlebar_font=('Candara', 14, 'bold'), background_color='#ce221e', element_justification='Center', force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def popup_cadastro_excluido(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Cadastro excluído!', size=(40,1), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')]]
        window = sgui.Window('ok', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, 
                keep_on_top=True, auto_close=True, auto_close_duration=1)
        botao, valores = window.Read()
        window.Close()
        return botao


    def selecionar_entradas(self, tupla: tuple):
            if isinstance(tupla, tuple):
                entrada1 = self.strip_str(tupla[0])
                entrada2 = self.strip_str(tupla[1])
                if entrada1 == entrada2:
                    if entrada1 != '':
                        return entrada1
                else:
                    if entrada1 != '':
                        return entrada1
                    else:
                        return entrada2
            else:
                return

    def strip_str(self, resposta):
        aux = ''
        resposta = resposta.split()
        for n in resposta:
            aux += n + ' '
        resposta = aux.strip().title()
        return resposta
