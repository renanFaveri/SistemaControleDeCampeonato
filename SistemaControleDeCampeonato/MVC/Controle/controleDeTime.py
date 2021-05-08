import PySimpleGUI as sgui
from .controleDeEntidade import ControladorDeEntidade
from MVC.limite.telaDeTime import TelaDeTimes
from MVC.limite.tela import Tela
from MVC.entidade.time import Time
from MVC.entidade.timeDao import TimeDAO
from MVC.entidade.tecnico import Tecnico
from MVC.entidade.jogador import Jogador
from MVC.exceptionLista import ListaError
from MVC.exceptionVazia import EntradaVaziaError


class ControladorDeTimes(ControladorDeEntidade):

    def __init__(self, controlador_master):
        self.__controlador_master = controlador_master
        self.__time_DAO = TimeDAO()
        self.__tela = TelaDeTimes(self)

    @property
    def time_DAO(self):
        return self.__time_DAO.cache
        
    @property
    def cm(self):
        return self.__controlador_master

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        if isinstance(tela, Tela):
            self.__tela = tela
            
    def listar_nomes_times(self):
        return [time.nome for time in self.__time_DAO.cache]
                    
    def buscar_nome(self, nome = None):
        for obj in self.__time_DAO.cache:
            if obj.nome.lower() == nome.lower():
                return obj

    def buscar(self):
        buscando = True
        while buscando:
            lista_nome_times = self.listar_nomes_times()
            self.tela.menu_buscar_times(lista_nome_times)
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    if valores['check']:
                        self.tela.fechaTela()
                        return self.listar()
                    else:
                        nome_time = self.tela.selecionar_entradas((valores['in_time'], valores['lst_time']))
                        time = self.buscar_nome(nome_time)
                        if not time:
                            raise EntradaVaziaError()
                        else:
                            self.tela.fechaTela()
                            return self.alterar(time)
                else:
                    self.tela.fechaTela()
                    break
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()            

    def cadastrar(self):
        cadastrando = True
        while cadastrando:
            self.tela.tela_cadastrar()
            botao, valores = self.tela.abreTela()
            if botao == 'Confirmar':
                try:
                    nome_time = self.tela.strip_str(valores['time_nome'])
                    cor_primaria = valores['cor1']
                    cor_secundaria = valores['cor2']
                    if 'None' in (nome_time, cor_primaria, cor_secundaria) or\
                                '' in (nome_time, cor_primaria, cor_secundaria) or\
                                self.buscar_nome(nome_time):
                        raise ValueError()
                    else:
                        time = Time(nome_time, cor_primaria, cor_secundaria)
                        self.__time_DAO.add(time)
                        break
                except ValueError:
                    self.tela.popup_msg_erro_cadastro()
                except TypeError:
                    self.tela.popup_msg_erro_cadastro()
                except EntradaVaziaError:
                    self.tela.popup_msg_erro_cadastro()
                finally:
                    self.tela.fechaTela()
            else:
                self.tela.fechaTela()
                break

    def contratar_tecnico(self, time):
        tecnicos = [tecnico.nome for tecnico in self.cm.cp.tecnicos_registrados if tecnico.time is not time]
        while True:
            self.tela.tela_contratar_tecnico(tecnicos)
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    nome_tecnico = valores['box_tecnicos'][0]
                    tecnico = self.cm.cp.buscar_nome(self.cm.cp.tecnicos_registrados, nome_tecnico)
                    botao = self.tela.popup_confirmar_compra(1)
                    if botao == 'Confirmar':
                        time.tecnico = tecnico
                        return
                else:
                    break
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()             

    def demitir_tecnico(self, time):
        botao = self.tela.popup_confirmar_demissao(time.tecnico.nome)
        if botao == 'Confirmar':
            time.tecnico.time = None
            time.tecnico = None

    def contratar_jogador(self, time):
        g, d, m , a = self.cm.cp.listar_gdma_disponiveis()
        goleiros = [goleiro for goleiro in g]
        defensores = [defensor for defensor in d]
        meio_campistas = [meio_campista for meio_campista in m]
        atacantes = [atacante for atacante in a]
        while True:
            self.tela.tela_contratar_jogador(goleiros, defensores, meio_campistas, atacantes)
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    negociados = valores['box_goleiros'] + valores['box_defensores'] + valores['box_meio_campistas'] + valores['box_atacantes']
                    jogadores = [self.cm.cp.buscar_nome(self.cm.cp.jogador_DAO, jogador) for jogador in negociados]
                    botao = self.tela.popup_confirmar_compra(len(jogadores))
                    if botao == 'Confirmar':
                        time.adicionar_jogadores(jogadores)
                        self.__time_DAO.atualizar(time)
                        return
                else:
                    break
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()

    def vender_jogador(self, time):
        lista_jogadores = time.dict_dados()['jogadores']
        self.tela.tela_vender_jogador(lista_jogadores)
        botao, valores = self.tela.abreTela()
        if botao == 'Confirmar':
            nomes_jogadores = [nome.split('-')[0] for nome in valores['lstbox']]
            jogadores = [self.cm.cp.buscar_nome(self.cm.cp.jogador_DAO, self.tela.strip_str(jogador)) for jogador in nomes_jogadores]
            botao = self.tela.popup_confirmar_venda(len(jogadores))
            if botao == 'Confirmar':
                time.remover_jogadores(jogadores)
                self.__time_DAO.atualizar(time)
        self.tela.fechaTela()
        return 

    def alterar(self, time):
        while True:
            self.tela.janela_time(time.dict_dados())
            botao, valores = self.tela.abreTela()
            janela_aux = self.tela.janela
            try:
                if botao == 'excluir':
                    excluiu = self.excluir(time)
                    self.__time_DAO.remove(time)
                    if excluiu:
                        break 
                elif botao == 'vender':
                    self.vender_jogador(time)
                    self.tela.janela = janela_aux
                elif botao == 'contratar':
                    self.contratar_jogador(time)
                    self.tela.janela = janela_aux
                elif botao == 'contratar_tecnico':
                    self.contratar_tecnico(time)
                    self.tela.janela = janela_aux
                elif botao == 'demitir_tecnico':
                    self.demitir_tecnico(time)
                elif botao == 'Confirmar':
                    alterou = False
                    if valores['cor1'] != time.cor_primaria or valores['cor2'] != time.cor_secundaria or valores['time_nome'] != time.nome:
                        alterou = True
                    if alterou:
                        botao = self.tela.popup_confirmar_alteracao()
                        if botao == 'Confirmar':
                            time.nome = self.tela.strip_str(valores['time_nome'].title())
                            time.cor_secundaria = valores['cor2']
                            time.cor_primaria = valores['cor1']
                            self.__time_DAO.atualizar(time)
                else:
                    break
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except TypeError:
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()
        return self.listar()
            
    def listar(self, n_entradas = None):
        lista_nome_legenda_times = sorted([(time.nome, f'{time}') for time in self.__time_DAO.cache], key= lambda tupla: tupla[0])
        self.tela.listar_times(lista_nome_legenda_times)
        botao, valores = self.tela.abreTela()
        self.tela.fechaTela()
        if not(botao == sgui.WIN_CLOSED or botao == 'Voltar'):
            nome_time = botao
            time = self.buscar_nome(nome_time)
            return self.alterar(time)

    def excluir(self, time):
        botao = self.tela.popup_msg_excluir()
        if botao == 'Confirmar':
            i = self.__time_DAO.get(time)
            time.remover_jogadores(time.jogadores.copy())
            return self.__time_DAO.remove(i)
     
    def abre_tela(self):
        tela = True
        while tela:
            opcoes = {1: self.cadastrar, 2: self.buscar, 3: self.alterar, 4: self.listar, 5: self.excluir}
            self.tela.exibir_menu()
            botao, valores = self.tela.abreTela()
            self.tela.fechaTela()
            if botao == 'Confirmar':
                for key in valores:
                    if valores[key]:
                        opcoes[key]()
            else:
                tela = False

