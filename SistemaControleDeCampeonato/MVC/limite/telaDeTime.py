import PySimpleGUI as sgui

class TelaDeTimes:

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
                  [sgui.Text('Cadastro de times', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Frame('', background_color='#06470F', 
                        layout = [[sgui.Radio('Cadastrar novo time', 'r1', text_color='#FAE98E',background_color='#06470F', size=(25,10), font=('Candara', 16), default=True, key=1),
                  sgui.Radio('Buscar times cadastrados', 'r1', text_color='#FAE98E', background_color='#06470F', size=(25,10), font=('Candara', 16), key=2)]])],
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
                  [sgui.Text('Cadastrar time', text_color='#FAE98E', background_color=background, size=(55,2), font=('Candara', 25), justification='center')],
                  [sgui.Frame('Informe o nome do time', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F',
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Text('Nome do time:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), pad=((25,20),0), key=('time_nome'))]])]])],
                  [sgui.Frame('Informe as cores do time', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', vertical_alignment='top',
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,200), 
                                layout=[[sgui.Text('Escolha no botão a cor primária do time:', size=(40,1), background_color='#06470F', font=('Candara', 12,'bold')),
                                sgui.ColorChooserButton('Botão cor primária', font=('Candara', 12, 'bold'), pad=(0,10), 
                                button_color=button_color, size=(10,3), target='cor1', key='cor_p'), 
                                sgui.InputText(size=(40,1), font=(16), pad=(20,20), key=('cor1'), disabled=True)],
                                [sgui.Text('Escolha no botão a cor secundária do time:', size=(40,1), background_color='#06470F', font=('Candara', 12,'bold')),
                                sgui.ColorChooserButton('Botão cor secundária', font=('Candara', 12, 'bold'), pad=(0,10), 
                                button_color=button_color, size=(10,3), target='cor2', key='cor_s'), 
                                sgui.InputText(size=(40,1), font=(16), pad=(20,20), key=('cor2'), disabled=True)]])]])],
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



    def menu_buscar_times(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Buscar times', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Digite o nome do time a ser visualizado ou escolha um da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Time', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_time')), 
                                sgui.Combo(sorted([f'{time.nome}' for time in self.ctrl.cm.ct.times_registrados]), font=(16), size=(40,1), 
                                    readonly=True, default_value=('Escolha um time da lista'), key=('lst_time'))]])],
                  [sgui.Text('ou marque a opção abaixo para listar todos os times cadastrados:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Listar times', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Visualizar todos os times cadastrados', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), 
                        sgui.Cancel('Voltar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Buscar times', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.__janela = window
        return

    def listar_times(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Column(layout=[[sgui.Text('Times cadastrados', text_color='#FAE98E', background_color=background, font=('Candara', 25), justification='center')],
                        [sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', background_color=background)]]
        layer2 = []
        times = self.ctrl.cm.ct.times_registrados
        times = sorted(times, key=lambda time: time.nome)
        for i in range(len(times)):
            texto = [sgui.Text(f'{times[i].nome}', font=('Candara', 14,'bold'), size=(30,0), text_color=text, background_color=background, justification='left')]
            coluna_texto = [sgui.Column([texto], background_color=background)]
            botao = [sgui.Button('Ver cadastro do time', size=(20,3), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, key=times[i])]
            coluna_botao = [sgui.Column([botao], background_color=background, element_justification='r')]
            legenda = [sgui.Text(f'{times[i]}', font=('Candara', 12), text_color=text, background_color=background, size=(80,0), justification='left')]
            coluna = [sgui.Column([coluna_texto + coluna_botao, legenda], background_color=background, element_justification='c')]
            frame = sgui.Frame(f'Time {i+1}', font=('Candara', 12,'bold'), pad=(80,10), title_color=text, background_color='#06470F', title_location='nw', 
                    layout=[coluna])
            linha = []            
            linha.append(frame)
            layer2.append(linha)
        layer2 = [sgui.Frame('', layout=layer2, vertical_alignment='t', pad=((30),0), background_color='#06470F')]
        layer2 = [[sgui.Column([layer2], scrollable=True, vertical_scroll_only=True, background_color=background, element_justification='center', size=(1000,600))]]
        layout.append(layer2)          
        window = sgui.Window('Buscar times', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
        return

    def janela_time(self, time):
        def ordenacao(lista_jogadores):
            g = []
            d = []
            m = []
            a = []
            for jogador in lista_jogadores:
                if jogador.posicao.posicao == 'Goleiro':
                    g.append(jogador)
                elif jogador.posicao.posicao == 'Defensor':
                    d.append(jogador)
                elif jogador.posicao.posicao == 'Meio campista':
                    m.append(jogador)
                else:
                    a.append(jogador)
            return g + d + m + a

        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        txt_jogadores = 'Nome' + '\t' * 2 + 'Posição' + '\t' * 2 + 'Gols marcados' + '\n'
        for jogador in ordenacao(time.jogadores):
            txt_jogadores += jogador.nome + '\t' * 2 + f'{jogador.posicao.posicao}' + '\t' * 2 + f'{jogador.gols_marcados}' + '\n'

        stats = f"""Partidas jogadas:\t\t{time.vitorias + time.empates + time.derrotas}
Vitórias:\t\t{time.vitorias}
Empates:\t\t{time.empates}
Derrotas:\t\t{time.derrotas}
Gols marcados:\t\t{time.gols_marcados}
Gols sofridos:\t\t{time.gols_sofridos}
Jogadores no time:\t\t{len(time.jogadores)}"""


        header = [[sgui.Column(layout=[[sgui.Text(f'{time.nome}'.upper(), text_color=time.cor_secundaria, background_color=time.cor_primaria, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]

        nome = [sgui.Frame('Alterar nome do time', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F',
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Text('Nome:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(default_text=f'{time.nome}', size=(40,1), font=(16), pad=((25,20),0), key=('time_nome'))]])]])]
        
        cores = [sgui.Frame('Alterar cores do time', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', vertical_alignment='top',
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,200), 
                                layout=[[sgui.Text('Escolha no botão a cor primária do time:', size=(40,1), background_color='#06470F', font=('Candara', 12,'bold')),
                                sgui.ColorChooserButton('Botão cor primária', font=('Candara', 12, 'bold'), pad=(0,10), 
                                    button_color=button_color, size=(10,3), target='cor1', key='cor_p'), 
                                sgui.InputText(default_text=f'{time.cor_primaria}', size=(40,1), font=(16), pad=(20,20), key=('cor1'), disabled=True)],
                                [sgui.Text('Escolha no botão a cor secundária do time:', size=(40,1), background_color='#06470F', font=('Candara', 12,'bold')),
                                sgui.ColorChooserButton('Botão cor secundária', font=('Candara', 12, 'bold'), pad=(0,10), 
                                    button_color=button_color, size=(10,3), target='cor2', key='cor_s'), 
                                sgui.InputText(default_text=f'{time.cor_secundaria}', size=(40,1), font=(16), pad=(20,20), key=('cor2'), disabled=True)]])]])]

        lista_jogadores = [sgui.Multiline(txt_jogadores, text_color='white', font=(12) , background_color=background, size=(50,11), disabled=True)]
        estatisticas = [sgui.Multiline(stats, text_color='white', font=(12), background_color=background, size=(30,11), no_scrollbar=True, disabled=True)]
        frame_jogadores = [sgui.Frame('Jogadores', layout = [lista_jogadores], title_color='#FAE98E', background_color='#06470F')]
        frame_estatisticas = [sgui.Frame('Estatísticas', layout = [estatisticas], title_color='#FAE98E', background_color='#06470F')]
        
        botao_contratar = [sgui.Button('Contratar jogador', size=(15,3), font=('Candara', 14,'bold'), border_width=6, focus=True, button_color=('white', '#01c906'), key='Contratar')]
        botao_vender = [sgui.Button('Vender jogador', size=(15,3), font=('Candara', 14,'bold'), border_width=6, focus=True, button_color=('white', '#ff9f11'), key='Vender')]
        col_botoes = [sgui.Column([botao_contratar, botao_vender], background_color='#06470F')]
        frame_dados = [sgui.Frame('', layout = [frame_estatisticas + frame_jogadores + col_botoes], background_color='#06470F')]
        botao_excluir = [sgui.Button('Declarar falência', size=(10,2), font=('Candara', 14), border_width=2, focus=True, button_color=('white', 'dark red'), key='excluir')]
        layout = header +  [nome] + [cores] + [frame_dados] + [botao_excluir]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
        return


    def tela_vender_jogador(self, time):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        header = [[sgui.Column(layout=[[sgui.Text(f'Vender jogador'.upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Cancelar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]
        linha1 = [sgui.Text('Selecione os jogadores que deseja vender:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background, size=(90,1), justification='left')]
        lista_jogadores = [sgui.Listbox([f'{jogador.nome}' for jogador in time.jogadores], select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', 
                            font=(12), background_color=background, size=(110,11), key='lstbox')]
        frame_jogadores = [sgui.Frame('Jogadores', layout = [lista_jogadores], title_color='#FAE98E', background_color='#06470F')]
        layout = header + [linha1] + [frame_jogadores]
        window = sgui.Window('Janela de mercado aberta', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.__janela = window
        return

    def tela_contratar_jogador(self, time):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        header = [[sgui.Column(layout=[[sgui.Text(f'Contratar jogador'.upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Cancelar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                    element_justification='center', vertical_alignment='c', background_color=background)]]
        linha1 = [sgui.Text('Selecione os jogadores que deseja contratar:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background, size=(90,1), justification='left')]
        lista_goleiros = [sgui.Listbox(sorted([f'{jogador.nome}' for jogador in self.ctrl.cm.cp.jogadores_registrados if jogador.posicao.posicao == 'Goleiro' and not jogador.time]),
                            select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', font=(12), background_color=background, size=(40,13), key='box_goleiros')]
        lista_defensores = [sgui.Listbox(sorted([f'{jogador.nome}' for jogador in self.ctrl.cm.cp.jogadores_registrados if jogador.posicao.posicao == 'Defensor' and not jogador.time]), 
                            select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', font=(12), background_color=background, size=(40,13), key='box_defensores')]
        lista_meio_campistas = [sgui.Listbox(sorted([f'{jogador.nome}' for jogador in self.ctrl.cm.cp.jogadores_registrados if jogador.posicao.posicao == 'Meio campista' and not jogador.time]),
                            select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', font=(12), background_color=background, size=(40,13), key='box_meio_campistas')]
        lista_atacantes = [sgui.Listbox(sorted([f'{jogador.nome}' for jogador in self.ctrl.cm.cp.jogadores_registrados if jogador.posicao.posicao == 'Atacante' and not jogador.time]),
                            select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', font=(12), background_color=background, size=(40,13), key='box_atacantes')]
        frame_goleiros = [sgui.Frame('Goleiros', layout=[lista_goleiros], title_color='#FAE98E', pad=((60,20),(20,10)), background_color='#06470F')]
        frame_defensores = [sgui.Frame('Defensores', layout=[lista_defensores], title_color='#FAE98E', pad=((20,60),(20,10)), background_color='#06470F')]
        frame_meio_campistas = [sgui.Frame('Meio campistas', layout=[lista_meio_campistas], title_color='#FAE98E', pad=((60,20),(10,20)), background_color='#06470F')]
        frame_atacantes = [sgui.Frame('Atacantes', layout=[lista_atacantes], title_color='#FAE98E', pad=((20,60),(10,20)), background_color='#06470F')]
        frame_jogadores = [sgui.Frame('Jogadores', layout = [frame_goleiros + frame_defensores, frame_meio_campistas + frame_atacantes], title_color='#FAE98E', background_color='#06470F')]
        layout = header + [linha1] + [frame_jogadores]
        window = sgui.Window('Janela de mercado aberta', layout, background_color=background, finalize=True, element_padding=(20,10), element_justification='center')
        self.__janela = window
        return


    def popup_confirmar_venda(self, lista):
        n_jogadores = len(lista)
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Confirmar a venda de {n_jogadores} jogadores?', size=(30,1), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Encher os cofres', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao


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
