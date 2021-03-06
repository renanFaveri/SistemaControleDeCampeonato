import PySimpleGUI as sgui
from .tela import Tela

class TelaDeTime(Tela):

    def __init__(self, controlador):
        super().__init__(controlador)

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
        self.janela = window
        return

    def menu_cadastrar(self):
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
                                layout=[[sgui.Text('Escolha no bot??o a cor prim??ria do time:', size=(40,1), background_color='#06470F', font=('Candara', 12,'bold')),
                                sgui.ColorChooserButton('Bot??o cor prim??ria', font=('Candara', 12, 'bold'), pad=(0,10), 
                                button_color=button_color, size=(10,3), target='cor1', key='cor_p'), 
                                sgui.InputText(size=(40,1), font=(16), pad=(20,20), key=('cor1'), disabled=True)],
                                [sgui.Text('Escolha no bot??o a cor secund??ria do time:', size=(40,1), background_color='#06470F', font=('Candara', 12,'bold')),
                                sgui.ColorChooserButton('Bot??o cor secund??ria', font=('Candara', 12, 'bold'), pad=(0,10), 
                                button_color=button_color, size=(10,3), target='cor2', key='cor_s'), 
                                sgui.InputText(size=(40,1), font=(16), pad=(20,20), key=('cor2'), disabled=True)]])]])],
                  [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))),
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]]
        window = sgui.Window('', layout, background_color=background, element_justification='left', finalize=True, keep_on_top = True)
        self.janela = window
        return

    def menu_buscar(self, lista_nome_times):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Buscar times', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Digite o nome do time a ser visualizado ou escolha um da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Time', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_time')), 
                                sgui.Combo(sorted([time_nome for time_nome in lista_nome_times]), font=(16), size=(40,1), 
                                    readonly=True, default_value=('Escolha um time da lista'), key=('lst_time'))]])],
                  [sgui.Text('ou marque a op????o abaixo para listar todos os times cadastrados:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Listar times', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Visualizar todos os times cadastrados', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), 
                        sgui.Cancel('Voltar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Buscar times', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.janela = window
        return

    def menu_listar(self, lista_nome_legenda_times):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        times = lista_nome_legenda_times
        layout = [[sgui.Column(layout=[[sgui.Text('Times cadastrados', text_color='#FAE98E', background_color=background, font=('Candara', 25), justification='center')],
                        [sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', background_color=background)]]
        layer2 = []
        for i in range(len(times)):
            texto = [sgui.Text(times[i][0], font=('Candara', 14,'bold'), size=(30,0), text_color=text, background_color=background, justification='left')]
            coluna_texto = [sgui.Column([texto], background_color=background)]
            botao = [sgui.Button('Ver cadastro do time', size=(20,3), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, key=times[i][0])] 
            coluna_botao = [sgui.Column([botao], background_color=background, element_justification='r')]    
            legenda = [sgui.Text(times[i][1], font=('Candara', 12), text_color=text, background_color=background, size=(80,0), justification='left')]
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
        self.janela = window
        return

    def menu_alterar(self, time_dict_dados):
        def ordenacao(lista_jogadores):
            g = []
            d = []
            m = []
            a = []
            for jogador in lista_jogadores:
                if jogador[1] == 'Goleiro':
                    g.append(jogador)
                elif jogador[1] == 'Defensor':
                    d.append(jogador)
                elif jogador[1] == 'Meio campista':
                    m.append(jogador)
                else:
                    a.append(jogador)
            g = sorted(g, key=lambda jogador: jogador[0])
            d = sorted(d, key=lambda jogador: jogador[0])
            m = sorted(m, key=lambda jogador: jogador[0])
            a = sorted(a, key=lambda jogador: jogador[0])
            return g + d + m + a

        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        txt_jogadores = 'Nome' + '\t' * 2 + 'Posi????o' + '\t' * 2 + 'Gols marcados' + '\n'

        for jogador in ordenacao(time_dict_dados['jogadores']):
            txt_jogadores += jogador[0] + '\t' * 2 + jogador[1] + '\t' * 2 + f'{jogador[2]}' + '\n'

        stats = f"""T??cnico\t\t{time_dict_dados['tecnico']}
Partidas jogadas:\t\t{time_dict_dados['vitorias'] + time_dict_dados['empates'] + time_dict_dados['derrotas']}
Vit??rias:\t\t{time_dict_dados['vitorias']}
Empates:\t\t{time_dict_dados['empates']}
Derrotas:\t\t{time_dict_dados['derrotas']}
Gols marcados:\t\t{time_dict_dados['gols_m']}
Gols sofridos:\t\t{time_dict_dados['gols_s']}
Jogadores no time:\t\t{len(time_dict_dados['jogadores'])}"""

        header = [[sgui.Column(layout=[[sgui.Text(time_dict_dados['nome'].upper(), text_color=time_dict_dados['cor_s'], background_color=time_dict_dados['cor_p'], 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Voltar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]
        nome = [sgui.Frame('Alterar nome do time', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F',
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,40), 
                                layout=[[sgui.Text('Nome:', size=(50,0), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(default_text=time_dict_dados['nome'], size=(40,1), font=(16), pad=((25,20),0), key=('time_nome'))]])]])]
        cores = [sgui.Frame('Alterar cores do time', font=('Candara', 12,'bold'), title_color='#FAE98E', background_color='#06470F', vertical_alignment='top',
                        layout=[[sgui.Column(vertical_alignment='b', background_color='#06470F', size=(1000,200), 
                                layout=[[sgui.Text('Escolha no bot??o a cor prim??ria do time:', size=(40,1), background_color='#06470F', font=('Candara', 12,'bold')),
                                sgui.ColorChooserButton('Bot??o cor prim??ria', font=('Candara', 12, 'bold'), pad=(0,10), 
                                    button_color=button_color, size=(10,3), target='cor1', key='cor_p'), 
                                sgui.InputText(default_text=time_dict_dados['cor_p'], size=(40,1), font=(16), pad=(20,20), key=('cor1'), disabled=True)],
                                [sgui.Text('Escolha no bot??o a cor secund??ria do time:', size=(40,1), background_color='#06470F', font=('Candara', 12,'bold')),
                                sgui.ColorChooserButton('Bot??o cor secund??ria', font=('Candara', 12, 'bold'), pad=(0,10), 
                                    button_color=button_color, size=(10,3), target='cor2', key='cor_s'), 
                                sgui.InputText(default_text=time_dict_dados['cor_s'], size=(40,1), font=(16), pad=(20,20), key=('cor2'), disabled=True)]])]])]

        lista_jogadores = [sgui.Multiline(txt_jogadores, text_color='white', font=(12) , background_color=background, size=(50,11), disabled=True)]
        estatisticas = [sgui.Multiline(stats, text_color='white', font=(12), background_color=background, size=(30,11), no_scrollbar=True, disabled=True)]
        frame_jogadores = [sgui.Frame('Jogadores', layout = [lista_jogadores], title_color='#FAE98E', background_color='#06470F')]
        frame_estatisticas = [sgui.Frame('Informa????es', layout = [estatisticas], title_color='#FAE98E', background_color='#06470F')]
        botao_ctecnico = [sgui.Button('Contratar t??cnico', size=(15,3), font=('Candara', 14,'bold'), border_width=6, focus=True, button_color=('white', '#5161F9'), key='contratar_tecnico')]
        botao_dtecnico = [sgui.Button('Demitir t??cnico', size=(15,3), font=('Candara', 14,'bold'), border_width=6, focus=True, button_color=('white', '#D351F9'), key='demitir_tecnico')]
        botao_contratar = [sgui.Button('Contratar jogador', size=(15,3), font=('Candara', 14,'bold'), border_width=6, focus=True, button_color=('white', '#01c906'), key='contratar')]
        botao_vender = [sgui.Button('Vender jogador', size=(15,3), font=('Candara', 14,'bold'), border_width=6, focus=True, button_color=('white', '#ff9f11'), key='vender')]
        col_botoes1 = [sgui.Column([botao_contratar, botao_vender], background_color='#06470F')]
        col_botoes2 = [sgui.Column([botao_ctecnico, botao_dtecnico], background_color='#06470F')]
        frame_dados = [sgui.Frame('', layout = [col_botoes2 + frame_estatisticas + frame_jogadores + col_botoes1], background_color='#06470F')]
        botao_excluir = [sgui.Button('Declarar fal??ncia', size=(10,2), font=('Candara', 14), border_width=2, focus=True, button_color=('white', 'dark red'), key='excluir')]
        coluna = [sgui.Column(layout = [nome] + [cores] + [frame_dados] + [botao_excluir], element_justification='center', background_color=background, 
                scrollable=True, vertical_scroll_only=True)]
        layout = header +  [coluna]
        window = sgui.Window('Cadastro de time', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.janela = window
        return

    def tela_vender_jogador(self, lista_dados_jogadores):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        header = [[sgui.Column(layout=[[sgui.Text(f'Vender jogador'.upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Cancelar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                  element_justification='center', vertical_alignment='c', background_color=background)]]
        linha1 = [sgui.Text('Selecione os jogadores que deseja vender:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background, size=(90,1), justification='left')]
        lista_jogadores = [sgui.Listbox([f'{dados_jogador[0]}'.ljust(30-len(dados_jogador[0]), ' ') + '---' + f'{" "*4}{dados_jogador[1]}' for dados_jogador in lista_dados_jogadores], select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', 
                            font=(12), background_color=background, size=(110,11), key='lstbox')]
        frame_jogadores = [sgui.Frame('Jogadores', layout = [lista_jogadores], title_color='#FAE98E', background_color='#06470F')]
        layout = header + [linha1] + [frame_jogadores]
        window = sgui.Window('Janela de mercado aberta', layout, background_color=background, finalize=True, element_padding=(10,10), element_justification='center')
        self.janela = window
        return

    def tela_contratar_jogador(self, lista_goleiro, lista_defensores, lista_meio_campistas, lista_atacantes):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        header = [[sgui.Column(layout=[[sgui.Text(f'Contratar jogador'.upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(50,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Cancelar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                    element_justification='center', vertical_alignment='c', background_color=background)]]
        linha1 = [sgui.Text('Selecione os jogadores que deseja contratar:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background, size=(90,1), justification='left')]
        lista_goleiros = [sgui.Listbox([goleiro for goleiro in lista_goleiro],
                            select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', font=(12), background_color=background, size=(40,13), key='box_goleiros')]
        lista_defensores = [sgui.Listbox([defensor for defensor in lista_defensores], 
                            select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', font=(12), background_color=background, size=(40,13), key='box_defensores')]
        lista_meio_campistas = [sgui.Listbox([meio_campista for meio_campista in lista_meio_campistas],
                            select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', font=(12), background_color=background, size=(40,13), key='box_meio_campistas')]
        lista_atacantes = [sgui.Listbox([atacante for atacante in lista_atacantes],
                            select_mode=sgui.LISTBOX_SELECT_MODE_MULTIPLE, text_color='white', font=(12), background_color=background, size=(40,13), key='box_atacantes')]
        frame_goleiros = [sgui.Frame('Goleiros', layout=[lista_goleiros], title_color='#FAE98E', pad=((60,20),(20,10)), background_color='#06470F')]
        frame_defensores = [sgui.Frame('Defensores', layout=[lista_defensores], title_color='#FAE98E', pad=((20,60),(20,10)), background_color='#06470F')]
        frame_meio_campistas = [sgui.Frame('Meio campistas', layout=[lista_meio_campistas], title_color='#FAE98E', pad=((60,20),(10,20)), background_color='#06470F')]
        frame_atacantes = [sgui.Frame('Atacantes', layout=[lista_atacantes], title_color='#FAE98E', pad=((20,60),(10,20)), background_color='#06470F')]
        frame_jogadores = [sgui.Frame('Jogadores', layout = [frame_goleiros + frame_defensores, frame_meio_campistas + frame_atacantes], title_color='#FAE98E', background_color='#06470F')]
        layout = header + [linha1] + [frame_jogadores]
        window = sgui.Window('Janela de mercado aberta', layout, background_color=background, finalize=True, element_padding=(20,10), element_justification='center')
        self.janela = window
        return

    def tela_contratar_tecnico(self, lista_tecnicos):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        header = [[sgui.Column(layout=[[sgui.Text(f'Contratar t??cnico'.upper(), text_color=text, background_color=background, 
                        font=('Candara', 25, 'bold'), size=(30,1), justification='center')],
                        [sgui.Button('Confirmar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30))), 
                        sgui.Button('Cancelar', size=(15,2), font=('Candara', 12, 'bold'), button_color=button_color, pad=((15,15), (30,30)))]], 
                    element_justification='center', vertical_alignment='c', background_color=background)]]
        linha1 = [sgui.Text('Selecione o t??cnico que deseja contratar:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background, size=(70,1), justification='left')]
        tecnicos = [sgui.Listbox([tecnico for tecnico in lista_tecnicos],
                            select_mode=sgui.LISTBOX_SELECT_MODE_SINGLE, text_color='white', font=(12), background_color=background, size=(60,13), key='box_tecnicos')]
        frame_tecnicos = [sgui.Frame('T??cnicos', layout=[tecnicos], title_color='#FAE98E', pad=(80,20), background_color='#06470F')]
        frame = [sgui.Frame('', layout = [frame_tecnicos], title_color='#FAE98E', background_color='#06470F')]
        layout = header + [linha1] + [frame]
        window = sgui.Window('Chama o mister', layout, background_color=background, finalize=True, element_padding=(20,10), element_justification='center')
        self.janela = window
        return

    def popup_confirmar_demissao(self, nome_tecnico):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Confirmar a demiss??o de {nome_tecnico}?', size=(30,1), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Goodbye, mister', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def popup_confirmar_venda(self, len_lista):
        n_jogadores = len_lista
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

    def popup_confirmar_compra(self, len_lista):
        n_jogadores = len_lista
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
