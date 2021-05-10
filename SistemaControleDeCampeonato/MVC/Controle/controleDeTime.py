import PySimpleGUI as sgui
from .controleDeEntidade import ControladorDeEntidade
from MVC.limite.telaDeTime import TelaDeTime
from MVC.limite.tela import Tela
from MVC.entidade.time import Time
from MVC.entidade.timeDao import TimeDAO
from MVC.entidade.tecnico import Tecnico
from MVC.entidade.jogador import Jogador
from MVC.exceptionLista import ListaError
from MVC.exceptionVazia import EntradaVaziaError
from MVC.exceptionDadosIndisponivel import DadoIndisponivelError
from MVC.exceptionCapacidadeMax import CapacidadeMaximaError


class ControladorDeTimes(ControladorDeEntidade):

    def __init__(self, controlador_master):
        super().__init__(controlador_master)
        self.__times_DAO = TimeDAO()
        self.__tela = TelaDeTime(self)

    @property
    def time_dao(self):
        return self.__times_DAO

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        if isinstance(tela, Tela):
            self.__tela = tela
            
    @property
    def times_registrados(self):
        self.time_dao.carregar()
        return self.__times_DAO.cache

    def listar_nomes_times(self):
        return [time.nome for time in self.times_registrados]
                    
    def buscar_nome(self, nome):
        for obj in self.times_registrados:
            if obj.nome.lower() == nome.lower():
                return obj

    def buscar(self):
        while True:
            lista_nome_times = self.listar_nomes_times()
            self.tela.menu_buscar(lista_nome_times)
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
        while True:
            self.tela.menu_cadastrar()
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':   
                    nome_time = self.tela.strip_str(valores['time_nome'])
                    cor_primaria = valores['cor1']
                    cor_secundaria = valores['cor2']
                    if 'None' in (nome_time, cor_primaria, cor_secundaria) or\
                                '' in (nome_time, cor_primaria, cor_secundaria):
                        raise EntradaVaziaError()
                    elif self.buscar_nome(nome_time):
                        raise DadoIndisponivelError()
                    else:
                        botao = self.tela.popup_confirmar_cadastro()
                        if botao == 'Confirmar':
                            time = Time(nome_time, cor_primaria, cor_secundaria)
                            self.__times_DAO.add(time)
                            self.tela.popup_cadastro_criado()
                            return
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except TypeError:
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()

    def contratar_tecnico(self, time):
        tecnicos = [tecnico.nome for tecnico in self.cm.cp.tecnicos_registrados if tecnico.time == '']
        while True:
            self.tela.tela_contratar_tecnico(tecnicos)
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    nome_tecnico = valores['box_tecnicos']
                    if len(nome_tecnico) == 0:
                        raise EntradaVaziaError()
                    else:
                        nome_tecnico = valores['box_tecnicos'][0]
                        tecnico = self.cm.cp.buscar_nome(self.cm.cp.tecnicos_registrados, nome_tecnico)
                        botao = self.tela.popup_confirmar_compra(1)
                        if botao == 'Confirmar':
                            time.tecnico = tecnico
                            time.tecnico.time = time
                            self.cm.cp.tecnico_dao.atualizar_objeto(tecnico)
                            return
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                    self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()

    def demitir_tecnico(self, time):
        tecnico = time.tecnico
        if tecnico == '' or tecnico == None:
            raise EntradaVaziaError()
        else:
            botao = self.tela.popup_confirmar_demissao(time.tecnico.nome)
            if botao == 'Confirmar':
                time.tecnico.time = None
                time.tecnico = None
                self.cm.cp.tecnico_dao.atualizar_objeto(tecnico)

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
                    nomes_jogadores = valores['box_goleiros'] + valores['box_defensores'] + valores['box_meio_campistas'] + valores['box_atacantes']
                    if len(nomes_jogadores) == 0:
                        raise EntradaVaziaError()
                    else:
                        jogadores = [self.cm.cp.buscar_nome(self.cm.cp.jogadores_registrados, self.tela.strip_str(jogador)) for jogador in nomes_jogadores]
                        botao = self.tela.popup_confirmar_compra(len(jogadores))
                        if botao == 'Confirmar':
                            time.adicionar_jogadores(jogadores)
                            for jogador in jogadores:
                                self.cm.cp.jogador_dao.atualizar_objeto(jogador)
                            return
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            except CapacidadeMaximaError:
                self.tela.popup_msg_erro_excedeu()
            finally:
                self.tela.fechaTela()
             
    def vender_jogador(self, time):
        lista_jogadores = time.dict_dados()['jogadores']
        while True:
            self.tela.tela_vender_jogador(lista_jogadores)
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    nomes_jogadores = [nome.split('-')[0] for nome in valores['lstbox']]
                    if len(nomes_jogadores) == 0:
                        raise EntradaVaziaError()
                    else:
                        jogadores = [self.cm.cp.buscar_nome(time.jogadores, self.tela.strip_str(jogador)) for jogador in nomes_jogadores]
                        botao = self.tela.popup_confirmar_venda(len(jogadores))
                        if botao == 'Confirmar':
                            time.remover_jogadores(jogadores.copy())
                            for jogador in jogadores:
                                self.cm.cp.jogador_dao.atualizar_objeto(jogador)
                            return
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()

    def carregar_jogadores(self, time):
        for i in range(len(time.jogadores)):
            time.jogadores[i] = self.cm.cp.jogador_dao.get(time.jogadores[i])

    def atualizar_jogadores(self, time):
        for i in range(len(time.jogadores)):
            self.cm.cp.jogador_dao.atualizar_objeto(time.jogadores[i])

    def atualizar_tecnico(time):
        if time.tecnico and time.tecnico != '':
            self.cm.cp.tecnico_dao.atualizar_objeto(time.tecnico)

    def alterar(self, time):
        while True:
            self.time_dao.carregar()
            time = self.time_dao.get(time)
            self.carregar_jogadores(time)
            self.tela.menu_alterar(time.dict_dados())
            botao, valores = self.tela.abreTela()
            janela_aux = self.tela.janela
            try:
                if botao == 'excluir':
                    excluiu = self.excluir(time)
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
                            indisponivel = self.buscar_nome(valores['time_nome'])
                            if indisponivel and time != indisponivel:
                                raise DadoIndisponivelError()
                            else:
                                time.cor_secundaria = valores['cor2']
                                time.cor_primaria = valores['cor1']
                                time.nome = self.tela.strip_str(valores['time_nome'])
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except TypeError:
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            except DadoIndisponivelError:
                self.tela.popup_msg_erro_dado_indisponivel()
            else:
                self.time_dao.atualizar_objeto(time)
                time = self.time_dao.get(time)
                self.atualizar_jogadores(time)
            finally:
                self.tela.fechaTela()

            
    def listar(self):
        while True:
            lista_nome_legenda_times = sorted([(time.nome, f'{time}') for time in self.times_registrados], key= lambda tupla: tupla[0])
            self.tela.menu_listar(lista_nome_legenda_times)
            botao, valores = self.tela.abreTela()
            self.tela.fechaTela()
            if not(botao == sgui.WIN_CLOSED or botao == 'Voltar'):
                nome_time = botao
                time = self.buscar_nome(nome_time)
                self.alterar(time)
            else:
                break

    def excluir(self, time):
        botao = self.tela.popup_msg_excluir()
        if botao == 'Confirmar':
            jogadores = time.jogadores.copy()
            time.remover_jogadores(jogadores)
            for jogador in jogadores:
                self.cm.cp.jogador_dao.atualizar_objeto(jogador)
            for campeonato in self.cm.cc.campeonatos_registrados:
                for competidor in campeonato.times:
                    if time.id_ == competidor.id_:
                        campeonato.remover_times([competidor])
                        self.cm.cc.campeonato_dao.atualizar_objeto(campeonato)
            self.tela.popup_cadastro_excluido()
            return self.__times_DAO.remover_e_retornar(time)
     
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