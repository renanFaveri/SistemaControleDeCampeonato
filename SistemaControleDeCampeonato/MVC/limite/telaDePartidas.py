import PySimpleGUI as sgui
from .tela import Tela
from MVC.entidade.partida import Partida
from MVC.entidade.campeonato import Campeonato




class TelaDePartidas(Tela):
    
    def __init__(self, controlador_de_tela):
        self.__janela = None
        self.__controlador = controlador_de_tela

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
                  [sgui.Button('Jogar amistoso', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('cp')),
                        sgui.Button('Criar partidas de campeonato', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('cps')),
                        sgui.Button('Jogar campeonato', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((10,10), (0,0)), key=('camp'))],
                  [sgui.Button('Ver partidas jogadas', size=(20,3), font=('Candara', 14), button_color=button_color, pad=((0,0), (30,0)), key=('vpj'))],
                  [sgui.Image(r'Img//sem_titulo.png', pad=((0,0), (30,0)))],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('UFSC Programmers League', layout, background_color=background, element_justification='Center', finalize=True, size=(994, 800), keep_on_top = True)
        self.__janela = window
        return


    def janela_inicio_partida(self, partida):
        background = '#20660C'
        button_color=('#F3EE44', '#06470F')
        text = '#FAE98E'
        col1x1 = [[sgui.Text(f'{partida.time_anfitriao.nome}'.upper(), text_color='white', background_color='red', size=(30,1), font=('Candara', 14,'bold'), justification='center')]]
        col1x2 = [[sgui.Text(f'0 x 0', font=('Candara', 20,'bold'), text_color=text, background_color='#06470F', size=(20,1), justification='center')], 
                    [sgui.Button('Jogar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color, pad=((0,(20,0))))]]
        col1x3 = [[sgui.Text(f'{partida.time_visitante.nome}'.upper(), text_color='white', background_color='light blue', size=(30,1), font=('Candara', 14,'bold'), justification='center')]]
        layout =[[sgui.Menu([['Arquivo', ['Sair']]])],
                 [sgui.Text(f'Partida id {partida.id_}', font=('Candara', 12,'bold'), text_color=text, background_color=background, size=(20,1), justification='left')],
                 [sgui.Text(f'Árbitro: {partida.arbitro_designado.nome}', font=('Candara', 12,'bold'), text_color=text, background_color=background, size=(20,2), justification='left')],
                 [sgui.Column(col1x1, vertical_alignment='t', background_color=background), sgui.Column(col1x2, background_color=background, element_justification='center'), 
                    sgui.Column(col1x3, vertical_alignment='t', background_color=background, element_justification='right')]]
        window = sgui.Window('Teste', layout, background_color=background, size=(994, 314))
        self.__janela = window
        return


    def janela_final_partida(self, partida):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        relatorio_partida = partida.relatorio
        relatorio_anf = [tupla for tupla in relatorio_partida if tupla[0].time is partida.time_anfitriao]
        text_anf = ""
        for tupla in relatorio_anf:
            text_anf += f"{tupla[0].nome} - gol aos {tupla[1]}'\n"
        relatorio_vis = [tupla for tupla in relatorio_partida if tupla[0].time is partida.time_visitante]
        text_vis = ""
        for tupla in relatorio_vis:
            text_vis += f"{tupla[0].nome} - gol aos {tupla[1]}'\n"
        col1x1 = [[sgui.Text(f'{partida.time_anfitriao.nome}'.upper(), text_color='white', background_color='red', size=(30,1), font=('Candara', 14,'bold'), justification='center')]]
        col1x2 = [[sgui.Text(f'{partida.placar}', font=('Candara', 20,'bold'), text_color=text, background_color='#06470F', size=(20,1), justification='center')]]
        col1x3 = [[sgui.Text(f'{partida.time_visitante.nome}'.upper(), text_color='white', background_color='light blue', size=(30,1), font=('Candara', 14,'bold'), justification='center')]]
        col2x1 = [[sgui.Frame('Time anfitrião', background_color=background, title_location='nw', key='rel_anf', 
                    layout = [[sgui.Multiline(default_text=f'{text_anf}', text_color='white', font=(12) , background_color=background, size=(48,8), disabled=True)]])]]
        col2x2 = [[sgui.Frame('Time visitante', background_color=background, title_location='ne', key='rel_vis', 
                layout = [[sgui.Multiline(default_text=f'{text_vis}', text_color='white', font=(12) , background_color=background, size=(48,8), disabled=True)]])]]
        
        col4 = [[sgui.Button('Voltar ao menu principal', size=(20,3), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, pad=((0,(20,0))), key = 'voltar')]]

        layout =[[sgui.Menu([['Arquivo', ['Sair']]])],
                [sgui.Text(f'Partida id {partida.id_}', font=('Candara', 12,'bold'), text_color=text, background_color=background, size=(20,1), justification='left')],
                [sgui.Text(f'Árbitro: {partida.arbitro_designado.nome}', font=('Candara', 12,'bold'), text_color=text, background_color=background, size=(20,2), justification='left')],
                [sgui.Column(col1x1, vertical_alignment='t', background_color=background), sgui.Column(col1x2, element_justification='center', background_color=background), 
                    sgui.Column(col1x3, vertical_alignment='t', background_color=background)],
                [sgui.Column(col2x1, vertical_alignment='t', background_color=background), sgui.Column(col2x2, vertical_alignment='t', background_color=background, justification='center')],
                [sgui.Column(col4, background_color=background, justification='center')]]
        window = sgui.Window('Teste', layout, background_color=background)
        self.__janela = window
        return
 
    def menu_criar_partida(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]

        layout = [[sgui.Menu(menu)],
                  [sgui.Text('Criação de partida', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Informe o nome dos times e do árbitro ou escolha um da lista:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Time anfitrião', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_anf')), 
                                sgui.Combo(sorted([f'{time.nome}' for time in self.ctrl.cm.ct.times_registrados]), font=(16) , size=(40,1), readonly=True, default_value=('Escolha um time da lista'), key=('lst_anf'))]])],
                  [sgui.Frame('Time visitante', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_vis')), 
                                sgui.Combo(sorted([f'{time.nome}' for time in self.ctrl.cm.ct.times_registrados]), font=(16) , size=(40,1), readonly=True, default_value=('Escolha um time da lista'), key=('lst_vis'))]])],
                  [sgui.Frame('Árbitro', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_arb')), 
                                sgui.Combo(sorted([f'{arbitro.nome}' for arbitro in self.ctrl.cm.cp.arbitros_registrados]), font=(16) , size=(40,1), readonly=True, default_value=('Escolha um árbitro da lista'), key=('lst_arb'))]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), sgui.Cancel('Voltar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]

        window = sgui.Window('Hora da pelada!', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.__janela = window
        return

    def menu_criar_partidas_camp(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        menu = [['Arquivo', ['Abrir', 'Salvar', 'Propriedades', 'Sair']]]

        layout = [[sgui.Menu(menu)],
                  [sgui.Text('Criação de partidas de campeonato', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Informe o campeonato cujas partidas deseja criar:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_camp')), 
                                sgui.Combo(sorted([f'{campeonato.nome}' for campeonato in self.ctrl.cm.cc.campeonatos_registrados]), font=(16) , size=(40,1), readonly=True, default_value=('Escolha um campeonato da lista'), key=('lst_camp'))]])],
                  [sgui.Text('ou marque a opção abaixo para criar partidas para todos os times cadastrados:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Sem campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Criar partidas desvinculadas de campeonato', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), sgui.Cancel('Voltar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]

        window = sgui.Window('Quem ganhar não paga o churrasco!', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.__janela = window
        return

    def popup_confirmacao_partida(self, partida: Partida):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'{partida}', text_color=text, background_color='#06470F', font=('Candara', 14), size=(50,3), justification='c')],
                  [sgui.Text('Confirmar criação da partida?', text_color='#F3EE44', background_color=background, font=('Candara', 14, 'bold'))],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Fechou time?', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def popup_confirmacao_partidas(self, lista, campeonato: Campeonato = None):
        if campeonato == None:
            nome_camp = '?'
        else:
            nome_camp = f'referentes ao campeonato {campeonato.nome}?'
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Confirmar criação de {(len(lista)-1)*2} partidas{nome_camp}', size=(30,1), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Fechou time?', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def popup_msg_erro_partida(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('A partida deve ser composta por dois times diferentes e um árbitro.', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Text('Escolha novamente.', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Button('OK', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, pad=(0,20))]]
        window = sgui.Window('Cartão Amarelo!'.upper(), layout, titlebar_font=('Candara', 14, 'bold'), background_color='#F3EE44', element_justification='Center', force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return

    def popup_msg_erro_partidas(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Não foi informado um campeonato válido!', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Text('Escolha novamente ou marque a opção "sem campeonato".', text_color='#20660C', background_color='#F3EE44', font=('Candara', 16, 'bold'))],
                  [sgui.Button('OK', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color, pad=(0,20))]]
        window = sgui.Window('Cartão Amarelo!'.upper(), layout, titlebar_font=('Candara', 14, 'bold'), background_color='#F3EE44', element_justification='Center', force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return

    def menu_jogar_camp(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Jogar partidas de campeonato', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Informe o campeonato a ser jogado:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_camp')), 
                                sgui.Combo(sorted([f'{campeonato.nome}' for campeonato in self.ctrl.cm.cc.campeonatos_registrados]), font=(16) , size=(40,1), readonly=True, default_value=('Escolha um campeonato da lista'), key=('lst_camp'))]])],
                  [sgui.Text('ou marque a opção abaixo para jogar partidas fora de campeonato:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Sem campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Jogar partidas desvinculadas de campeonato', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), sgui.Cancel('Voltar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Jogar partidas', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.__janela = window
        return

    def popup_jogar_camp(self, lista, campeonato: Campeonato = None):
        if campeonato == None:
            nome_camp = '?'
        else:
            nome_camp = f'referentes ao campeonato {campeonato.nome}?'
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text(f'Jogar {(len(lista))} partidas{nome_camp}', size=(30,1), pad=((20,20)), text_color='#F3EE44', background_color='#06470F', border_width=(10), font=('Candara', 14, 'bold'), justification='c')],
                  [sgui.Button('Confirmar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color), 
                        sgui.Button('Cancelar', size=(10,2), font=('Candara', 12,'bold'), border_width=2, focus=True, button_color=button_color)]]
        window = sgui.Window('Fechou time?', layout, background_color=background, element_justification='Center', element_padding=(10,10), force_toplevel=True, keep_on_top=True)
        botao, valores = window.Read()
        window.Close()
        return botao

    def mostrar_partidas_campeonato(self, partidas: list):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layer = [[sgui.Text('Resultados das partidas', text_color='#FAE98E', background_color=background, font=('Candara', 25), size= (50,2), justification='center')],
                  [sgui.Button('Voltar', size=(10,2), font=('Candara', 12,'bold'), pad=(0,20), border_width=2, focus=True, button_color=button_color)]]
        layer2 = []
        for i in range(len(partidas)):
            texto = [sgui.Text(f'{partidas[i]}', font=('Candara', 14,'bold'), size=(30,0), text_color=text, background_color=background, justification='center')]
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
        self.__janela = window
        return self.__janela

    def menu_mostrar_partidas(self):
        background = '#20660C'
        text = '#FAE98E'
        button_color=('#F3EE44', '#06470F')
        layout = [[sgui.Text('Ver partidas jogadas', text_color='#FAE98E', background_color=background, size=(60,3), font=('Candara', 25), justification='center')],
                  [sgui.Text('Informe o campeonato a ser visualizado:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Text('Nome: ', size=(10,1), background_color='#06470F', font=('Candara', 12,'bold')), 
                                sgui.InputText(size=(40,1), font=(16), key=('in_camp')), 
                                sgui.Combo(sorted([f'{campeonato.nome}' for campeonato in self.ctrl.cm.cc.campeonatos_registrados]), font=(16) , size=(40,1), readonly=True, default_value=('Escolha um campeonato da lista'), key=('lst_camp'))]])],
                  [sgui.Text('ou marque a opção abaixo para ver todas as partidas já jogadas:'.upper(), font=('Candara', 16,'bold'), text_color=text, background_color=background)],
                  [sgui.Frame('Sem campeonato', font=('Candara', 12,'bold'), title_color=text, background_color='#06470F', title_location='nw', 
                        layout=[[sgui.Checkbox('Visualizar todas as partidas jogadas', size=(40,2), font=('Candara', 12,'bold'), background_color='#06470F', key='check')]])],
                  [sgui.Submit('Confirmar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color), sgui.Cancel('Voltar', size=(10,2), font=('Candara', 12,'bold'), button_color=button_color)],
                  [sgui.Text('', background_color=background, size=(0,4))]]
        window = sgui.Window('Jogar partidas', layout, background_color=background, finalize=True, element_padding=(10,10))
        self.__janela = window
        return


    def strip_str(self, resposta):
        aux = ''
        resposta = resposta.split()
        for n in resposta:
            aux += n + ' '
        resposta = aux.strip().title()
        return resposta
