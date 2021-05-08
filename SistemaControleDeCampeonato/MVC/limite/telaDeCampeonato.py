import PySimpleGUI as sgui


class TelaDeCampeonatos:
    
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
                  [sgui.Text('Cadastro de campeonatos', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Frame('', background_color='#06470F', 
                        layout = [[sgui.Radio('Cadastrar novo campeonato', 'r1', text_color='#FAE98E',background_color='#06470F', size=(25,10), font=('Candara', 16), default=True, key=1),
                  sgui.Radio('Buscar campeonatos cadastrados', 'r1', text_color='#FAE98E', background_color='#06470F', size=(30,10), font=('Candara', 16), key=2)]])],
                  [sgui.Button('Confirmar', size=(15,2), font=('Candara', 14), button_color=button_color, pad=((10,10), (30,60))),
                        sgui.Button('Voltar', size=(15, 2), font=('Candara', 14), button_color=button_color, pad=((10,10), (30,60)))]]
        window = sgui.Window('UFSC Programmers League', layout, background_color=background, element_justification='Center', finalize=True, keep_on_top = True)
        self.__janela = window
        return


    def tela_cadastrar(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]
        layout = [[sgui.Menu(menu)],
                  [sgui.Text('Cadastrar campeonato', text_color='#FAE98E', background_color=background, size=(55,2), font=('Candara', 25), justification='center')],
                  [sgui.Frame('Informe o nome do campeonato', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Text('Nome do campeonato:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), pad=((25,20),0), key=('campeonato_nome'))]])]])],
                  [sgui.Frame('Informe o número de times competidos', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Slider(range=(2,20), size=(100,30), orientation='horizontal', background_color='#06470F', trough_color=background, 
                                font=('Candara', 12, 'bold'), key='n_times')]])],
                  [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))),
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]]
        window = sgui.Window('', layout, background_color=background, element_justification='left', finalize=True, keep_on_top = True)
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


    def menu_buscar_campeonatos(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Buscar campeonatos', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Digite o nome do campeonato a ser visualizado ou escolha um da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_campeonato')), 
                                sgui.Combo(sorted([f'{campeonato.nome}' for campeonato in self.ctrl.cm.cc.campeonatos_registrados]), font=(16), size=(40,1), 
                                    readonly=True, default_value=('Escolha um campeonato da lista'), key=('lst_campeonato'))]])],
                  [sgui.Text('ou marque a opção abaixo para listar todos os campeonatos cadastrados:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Listar campeonatos', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Visualizar todos os campeonatos cadastrados', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), 
                        sgui.Cancel('Voltar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Buscar campeonatos', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.__janela = window
        return


    def listar_campeonatos(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Column(layout=[[sgui.Text('Campeonatos cadastrados', text_color='#FAE98E', background_color=background, font=('Candara', 25), justification='center')],
                        [sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', background_color=background)]]
        layer2 = []
        campeonatos = self.ctrl.cm.cc.campeonatos_registrados
        campeonatos = sorted(campeonatos, key=lambda campeonato: campeonato.nome)
        for i in range(len(campeonatos)):
            texto = [sgui.Text(f'{campeonatos[i].nome}', font=('Candara', 14,'bold'), size=(30,0), text_color=text, background_color=background, justification='left')]
            coluna_texto = [sgui.Column([texto], background_color=background)]
            botao = [sgui.Button('Ver cadastro do campeonato', size=(20,3), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, key=campeonatos[i])]
            coluna_botao = [sgui.Column([botao], background_color=background, element_justification='r')]
            legenda = [sgui.Text(f'{campeonatos[i]}', font=('Candara', 12), text_color=text, background_color=background, size=(80,0), justification='left')]
            coluna = [sgui.Column([coluna_texto + coluna_botao, legenda], background_color=background, element_justification='c')]
            frame = sgui.Frame(f'Campeonato {i+1}', font=('Candara', 12,'bold'), pad=(80,10), title_color=text, background_color='#06470F', title_location='nw', 
                    layout=[coluna])
            linha = []            
            linha.append(frame)
            layer2.append(linha)
        layer2 = [sgui.Frame('', layout=layer2, vertical_alignment='t', pad=((30),0), background_color='#06470F')]
        layer2 = [[sgui.Column([layer2], scrollable=True, vertical_scroll_only=True, background_color=background, element_justification='center', size=(1000,600))]]
        layout.append(layer2)          
        window = sgui.Window('Buscar campeonatos', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
        return



    def janela_campeonato(self, campeonato):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        tabela = campeonato.gerar_estatisticas()


        header = [[sgui.Column(layout=[[sgui.Text(f'{campeonato.nome}'.upper(), text_color='#FAE98E', background_color=background, font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]

        nome = [sgui.Frame('Alterar nome do campeonato', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F',
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Text('Nome:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(default_text=f'{campeonato.nome}', size=(40,1), font=(16), pad=((25,20),0), key=('campeonato_nome'))]])]])]
        n_times = [sgui.Frame('Alterar o número de times competidos', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', pad=(20,15),
                        layout=[[sgui.Slider(range=(2,20), size=(100,30), orientation='horizontal', background_color='#06470F', trough_color=background, 
                                font=('Candara', 12, 'bold'), default_value=campeonato.n_times, key='n_times')]])]
        
        

        classificacao = [sgui.Multiline(tabela, text_color='white', font=(12), background_color=background, size=(60,11), disabled=True)]


        # estatisticas = [sgui.Multiline(stats, text_color='white', font=(12), background_color=background, size=(30,11), no_scrollbar=True, disabled=True)]



        # frame_jogadores = [sgui.Frame('Jogadores', layout = [lista_jogadores], title_color='#FAE98E', background_color='#06470F')]
        frame_classificacao = [sgui.Frame('Tabela', layout=[classificacao], title_color='#FAE98E', background_color='#06470F')]
        
        botao_adicionar = [sgui.Button('Adicionar times', size=(15,3), font=('Candara', 14,'bold'), border_width=6, focus=True, button_color=('white', '#01c906'), key='adicionar')]
        botao_remover = [sgui.Button('Remover times', size=(15,3), font=('Candara', 14,'bold'), border_width=6, focus=True, button_color=('white', '#ff9f11'), key='remover')]
        col_botoes = [sgui.Column([botao_adicionar, botao_remover], background_color='#06470F')]
        frame_dados = [sgui.Frame('', layout = [frame_classificacao + col_botoes], background_color='#06470F')]

        botao_excluir = [sgui.Button('Cancelar campeonato', size=(10,2), font=('Candara', 14), border_width=2, focus=True, button_color=('white', 'dark red'), key='excluir')]

        layout = header + [nome] + [n_times] + [frame_dados] + [botao_excluir]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
        return

    def tela_remover_times(self, time):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        header = [[sgui.Column(layout=[[sgui.Text(f'Remover times'.upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Cancelar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]
        linha1 = [sgui.Text('Selecione os times que deseja remover:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background, size=(90,1), justification='left')]
        lista_times = [sgui.Listbox([f'{time.nome}' for time in campeonato.times], select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', 
                            font=(12), background_color=background, size=(110,11), key='lstbox')]
        frame_times = [sgui.Frame('Times', layout = [lista_times], title_color='#FAE98E', background_color='#06470F')]
        layout = header + [linha1] + [frame_times]
        window = sgui.Window('Janela de mercado aberta', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
        return

    def tela_adicionar_times(self, time):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        header = [[sgui.Column(layout=[[sgui.Text(f'Adicionar times'.upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Cancelar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                    element_justification='center', vertical_alignment='c', background_color=background)]]
        linha1 = [sgui.Text('Selecione os times que deseja adicionar ao campeonanto:'.upper(), font=('Candara', 16,'bold'), text_color=text, 
                background_color=background, size=(90,1), justification='left')]
        lista_times = [sgui.Listbox(sorted([f'{time.nome}' for time in self.ctrl.cm.ct.times_registrados]), select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', 
                            font=(12), background_color=background, size=(110,11), key='competidores')]
        
        frame_atacantes = [sgui.Frame('Atacantes', layout=[lista_times], title_color='#FAE98E', pad=((20,60),(10,20)), background_color='#06470F')]
        frame_jogadores = [sgui.Frame('Jogadores', layout = [frame_atacantes], title_color='#FAE98E', background_color='#06470F')]
        layout = header + [linha1] + [frame_jogadores]
        window = sgui.Window('Organizar campeonato', layout, background_color=background, finalize=True, element_padding=(20,10), element_justification='center')
        self.__janela = window
        return

    def popup_confirmar_compra(self, lista):
        n_jogadores = len(lista)
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Confirmar a compra de {n_jogadores} jogadores?', size=(30,1), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Esvaziar os cofres', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao
        
    def popup_confirmar_alteracao(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Foram feitas alterações no cadastro do time.\n Confirmar essas alterações?', size=(35,3), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Confirmar alterações', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
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


