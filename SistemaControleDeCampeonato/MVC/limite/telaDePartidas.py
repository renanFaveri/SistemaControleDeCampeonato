import PySimpleGUI as sgui
from .tela import Tela

class TelaDePartida(Tela):
    
    def __init__(self, controlador):
        super().__init__(controlador)

    def exibir_menu(self):
        background = '#20660C'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]

        layout = [[sgui.Menu(menu)],
                  [sgui.Text('UFSC Programmers League', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Button('Jogar amistoso', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('cp')),
                        sgui.Button('Criar partidas de campeonato', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('cps')),
                        sgui.Button('Jogar campeonato', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('camp'))],
                  [sgui.Button('Ver partidas jogadas', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (30,0)), key=('vpj')), 
                    sgui.Button('Voltar', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (30,0)))],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('UFSC Programmers League', layout, background_color=background, element_justification='Center', finalize=True, keep_on_top = True)
        self.janela = window
        return

    def janela_inicio_partida(self, dict_partida, dict_time_anf, dict_time_vis):
        background = '#20660C'
        button_color=('#F3EE44', '#06470F')
        text = '#FAE98E'
        col1x1 = [[sgui.Text(f"{dict_time_anf['nome']}".upper(), text_color=dict_time_anf['cor_s'],
                        background_color=dict_time_anf['cor_p'], size=(30,1), font=('Candara', 14,'bold'), justification='center')]]
        col1x2 = [[sgui.Text(f"{dict_partida['placar']}", font=('Candara', 20,'bold'), text_color=text, background_color='#06470F', size=(20,1), justification='center')], 
                    [sgui.Button('Jogar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color, pad=((0,(20,0))))]]
        col1x3 = [[sgui.Text(f"{dict_time_vis['nome']}".upper(), text_color=dict_time_vis['cor_s'], 
                        background_color=dict_time_vis['cor_p'], size=(30,1), font=('Candara', 14,'bold'), justification='center')]]
        layout =[[sgui.Menu([['Arquivo', ['Sair']]])],
                 [sgui.Text(f"Partida id {dict_partida['id']}", font=('Candara', 12,'bold'), text_color=text, background_color=background, size=(20,1), justification='left')],
                 [sgui.Text(f"??rbitro: {dict_partida['arb']}", font=('Candara', 12,'bold'), text_color=text, background_color=background, size=(20,2), justification='left')],
                 [sgui.Column(col1x1, vertical_alignment='t', background_color=background), sgui.Column(col1x2, background_color=background, element_justification='center'), 
                    sgui.Column(col1x3, vertical_alignment='t', background_color=background, element_justification='right')]]
        window = sgui.Window('Teste', layout, background_color=background, size=(994, 314))
        self.janela = window
        return

    def janela_final_partida(self, dict_partida, dict_time_anf, dict_time_vis):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        col1x1 = [[sgui.Text(f"{dict_time_anf['nome']}".upper(), text_color=dict_time_anf['cor_s'], background_color=dict_time_anf['cor_p'], 
                    size=(30,1), font=('Candara', 14,'bold'), justification='center')]]
        col1x2 = [[sgui.Text(f"{dict_partida['placar']}", font=('Candara', 20,'bold'), text_color=text, background_color='#06470F', size=(20,1), justification='center')]]
        col1x3 = [[sgui.Text(f"{dict_time_vis['nome']}".upper(), text_color=dict_time_vis['cor_s'], background_color=dict_time_vis['cor_p'], 
                    size=(30,1), font=('Candara', 14,'bold'), justification='center')]]
        col2x1 = [[sgui.Frame('Time anfitri??o', background_color=background, title_location='nw', key='rel_anf', 
                    layout = [[sgui.Multiline(default_text=f"{dict_partida['txt_relatorio'][0]}", text_color='white', font=(12) , background_color=background, 
                    size=(48,8), disabled=True, no_scrollbar=True)]])]]
        col2x2 = [[sgui.Frame('Time visitante', background_color=background, title_location='ne', key='rel_vis', 
                    layout = [[sgui.Multiline(default_text=f"{dict_partida['txt_relatorio'][1]}", text_color='white', font=(12) , background_color=background, 
                    size=(48,8), disabled=True, no_scrollbar=True)]])]]  
        col3 = [[sgui.Button('Voltar ao menu principal', size=(20,3), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, pad=((0,(20,0))), key = 'voltar')]]
        layout =[[sgui.Menu([['Arquivo', ['Sair']]])],
                [sgui.Text(f"Partida id {dict_partida['id']}", font=('Candara', 12,'bold'), text_color=text, background_color=background, size=(20,1), justification='left')],
                [sgui.Text(f"??rbitro: {dict_partida['arb']}", font=('Candara', 12,'bold'), text_color=text, background_color=background, size=(20,2), justification='left')],
                [sgui.Column(col1x1, vertical_alignment='t', background_color=background), sgui.Column(col1x2, element_justification='center', background_color=background), 
                    sgui.Column(col1x3, vertical_alignment='t', background_color=background)],
                [sgui.Column(col2x1, vertical_alignment='t', background_color=background), sgui.Column(col2x2, vertical_alignment='t', background_color=background, justification='center')],
                [sgui.Column(col3, background_color=background, justification='center')]]
        window = sgui.Window('Teste', layout, background_color=background)
        self.janela = window
        return

    def menu_cadastrar(self, lista_times, lista_arbitros):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]

        layout = [[sgui.Menu(menu)],
                  [sgui.Text('Cria????o de partida', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Digite o nome dos times e do ??rbitro ou escolha um da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Time anfitri??o', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_anf')), 
                                sgui.Combo(sorted([time_nome for time_nome in lista_times]), font=(16) , size=(40,1), 
                                readonly=True, default_value=('Escolha um time da lista'), key=('lst_anf'))]])],
                  [sgui.Frame('Time visitante', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_vis')), 
                                sgui.Combo(sorted([time_nome for time_nome in lista_times]), font=(16) , size=(40,1), 
                                readonly=True, default_value=('Escolha um time da lista'), key=('lst_vis'))]])],
                  [sgui.Frame('??rbitro', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_arb')), 
                                sgui.Combo(sorted([arbitro_nome for arbitro_nome in lista_arbitros]), 
                                font=(16) , size=(40,1), readonly=True, default_value=('Escolha um ??rbitro da lista'), key=('lst_arb'))]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), sgui.Cancel('Voltar', size=(10,2), 
                        font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Hora da pelada!', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.janela = window
        return

    def menu_cadastrar_partidas(self, lista_campeonatos):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]

        layout = [[sgui.Menu(menu)],
                  [sgui.Text('Cria????o de partidas de campeonato', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Digite o nome do campeonato cujas partidas deseja criar ou escolha um da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_camp')), 
                                sgui.Combo(sorted([campeonato_nome for campeonato_nome in lista_campeonatos]), font=(16), 
                                size=(40,1), readonly=True, default_value=('Escolha um campeonato da lista'), key=('lst_camp'))]])],
                  [sgui.Text('ou marque a op????o abaixo para criar partidas para todos os times cadastrados:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Sem campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Criar partidas desvinculadas de campeonato', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), sgui.Cancel('Voltar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Quem ganhar n??o paga o churrasco!', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.janela = window
        return

    def popup_confirmar_cadastro(self, str_partida):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(str_partida, text_color=text, background_color='#06470F', font=('Candara', 14), size=(50,3), justification='c')],
                  [sgui.Text('Confirmar cria????o da partida?', text_color='#F3EE44', background_color=background, font=('Candara', 14, 'bold'))],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Fechou time?', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def popup_confirmar_partidas(self, len_lista_times, nome_campeonato):
        if nome_campeonato == '':
            nome_camp = '?'
        else:
            nome_camp = f' referentes ao campeonato {nome_campeonato}?'
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Confirmar cria????o de {len_lista_times * (len_lista_times - 1)} partidas{nome_camp}', size=(30,2), pad=((20,20)), text_color='#F3EE44', 
                        background_color='#06470F', border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Fechou time?', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def popup_msg_erro_cadastro(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('A partida deve ser composta por dois times diferentes e um ??rbitro.', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Text('Tente novamente.', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Button('OK', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, pad=(0,20))]]
        window = sgui.Window('Cart??o Amarelo!'.upper(), layout, titlebar_font=('Candara', 14, 'bold'), background_color='#F3EE44', element_justification='Center', force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return

    def popup_erro_time_incompleto(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Os times devem possuir ao menos 1 goleiro e outro jogador para jogarem uma partida.', text_color='#20660C', 
                        background_color='#F3EE44', font=('Candara', 16, 'bold'), justification='Center')],
                  [sgui.Text('Escolha novamente.', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'), justification='Center')],
                  [sgui.Button('OK', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, pad=(0,20))]]
        window = sgui.Window('Cart??o Amarelo!'.upper(), layout, titlebar_font=('Candara', 14, 'bold'), background_color='#F3EE44', element_justification='Center', force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return

    def popup_msg_erro_partidas(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('N??o foi informado um campeonato v??lido!', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Text('Escolha novamente ou marque a op????o "sem campeonato".', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Button('OK', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, pad=(0,20))]]
        window = sgui.Window('Cart??o Amarelo!'.upper(), layout, titlebar_font=('Candara', 14, 'bold'), background_color='#F3EE44', element_justification='Center', force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return

    def menu_jogar_camp(self, lista_campeonatos):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Jogar partidas de campeonato', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Digite o nome do campeonato a ser jogado ou escolha um da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_camp')), 
                                sgui.Combo(sorted([campeonato_nome for campeonato_nome in lista_campeonatos]), font=(16) , size=(40,1), 
                                readonly=True, default_value=('Escolha um campeonato da lista'), key=('lst_camp'))]])],
                  [sgui.Text('ou marque a op????o abaixo para jogar partidas fora de campeonato:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Sem campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Jogar partidas desvinculadas de campeonato', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), sgui.Cancel('Voltar', 
                        size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Jogar partidas', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.janela = window
        return

    def popup_jogar_camp(self, len_lista_partidas, nome_campeonato):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Jogar campeonato?', size=(30,2), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', 
                        border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Fechou time?', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def menu_listar(self, lista_str_partidas):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layer = [[sgui.Text('Resultados das partidas', text_color='#FAE98E', background_color=background, font=('Candara', 25), size= (50,2), justification='center')],
                  [sgui.Button('Voltar', size=(10,2), font=('Candara', 12,'bold'), pad=(0,20), border_width=2, focus=True, button_color=button_color)]]
        layer2 = []
        for i in range(len(lista_str_partidas)):
            texto = [sgui.Text(f'{lista_str_partidas[i]}', font=('Candara', 14,'bold'), size=(30,0), text_color=text, background_color=background, justification='center')]
            botao = [sgui.Button('Ver tela da partida', size=(10,2), font=('Candara', 12,'bold'), pad=(0,20), border_width=2, focus=True, button_color=button_color, key=i+1)]
            coluna = [sgui.Column([texto, botao], background_color=background, element_justification='center')]
            if i % 2 == 0:
                linha = []
                frame = sgui.Frame(f'Partida {i+1}', font=('Candara', 12,'bold'), pad=((80,20),10), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[coluna])
                linha.append(frame)
                layer2.append(linha)                        
            else:
                frame = sgui.Frame(f'Partida {i+1}', font=('Candara', 12,'bold'), pad=((20,80),10), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[coluna])
                linha.append(frame)
        frame_todos_resultados = [sgui.Frame(title='', background_color='#06470F', layout = layer2)]  
        layer.append(frame_todos_resultados)
        layout = [[sgui.Column(layer, scrollable=True, vertical_scroll_only=True, background_color=background, element_justification='center', size=(950,600))]]
        window = sgui.Window('teste', layout, background_color=background, finalize=True)
        self.janela = window
        return

    def menu_buscar(self, lista_campeonatos):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Ver partidas jogadas', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Digite o nome do campeonato a ser visualizado ou escolha um da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_camp')), 
                                sgui.Combo(sorted([campeonato_nome for campeonato_nome in lista_campeonatos]), font=(16) , size=(40,1), 
                                        readonly=True, default_value=('Escolha um campeonato da lista'), key=('lst_camp'))]])],
                  [sgui.Text('ou marque a op????o abaixo para ver todas as partidas j?? jogadas:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Sem campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Visualizar todas as partidas jogadas', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), sgui.Cancel('Voltar', 
                        size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Jogar partidas', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.janela = window
        return