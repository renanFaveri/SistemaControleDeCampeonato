import PySimpleGUI as sgui
from MVC.entidade.campeonato import Campeonato 
from MVC.entidade.time import Time
from MVC.entidade.campeonatoDao import CampeonatoDAO
from .controleDeEntidade import ControladorDeEntidade
from MVC.limite.tela import Tela
from MVC.limite.telaDeCampeonato import TelaDeCampeonato
from MVC.exceptionLista import ListaError
from MVC.exceptionVazia import EntradaVaziaError
from MVC.exceptionDadosIndisponivel import DadoIndisponivelError
from MVC.exceptionCapacidadeMax import CapacidadeMaximaError


class ControladorDeCampeonatos(ControladorDeEntidade):

    def __init__(self, controlador_master):
        super().__init__(controlador_master)
        self.__tela = TelaDeCampeonato(self)
        self.__campeonato_DAO = CampeonatoDAO()

    @property
    def tela(self):
        return self.__tela
    
    @tela.setter
    def tela(self, tela):
        if isinstance(tela, Tela):
            self.__tela = tela

    @property
    def campeonato_dao(self):
        return self.__campeonato_DAO
            
    @property
    def campeonatos_registrados(self):
        self.campeonato_dao.carregar()
        return self.__campeonato_DAO.cache

    def listar_nomes_campeonatos(self):
        return [campeonato.nome for campeonato in self.campeonatos_registrados]
            
    def buscar_nome(self, nome):
        for obj in self.campeonatos_registrados:
            if obj.nome.lower() == nome.lower():
                return obj
         
    def buscar(self):
        lista_campeonatos = self.listar_nomes_campeonatos()
        while True:
            self.tela.menu_buscar(lista_campeonatos)
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    if valores['check']:
                        self.tela.fechaTela()
                        return self.listar()
                    else:
                        nome_campeonato = self.tela.selecionar_entradas((valores['in_campeonato'], valores['lst_campeonato']))
                        campeonato = self.buscar_nome(nome_campeonato)
                        if not campeonato:
                            raise EntradaVaziaError()
                        else:
                            self.tela.fechaTela()
                            return self.alterar(campeonato)
                else:
                    return
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
                    nome_campeonato = self.tela.strip_str(valores['campeonato_nome'])
                    n_times = int(valores['n_times'])
                    if '' == nome_campeonato:
                        raise EntradaVaziaError()
                    elif self.buscar_nome(nome_campeonato):
                        raise DadoIndisponivelError()
                    else:
                        botao = self.tela.popup_confirmar_cadastro()
                        if botao == 'Confirmar':
                            campeonato = Campeonato(nome_campeonato, n_times)
                            self.campeonato_dao.add(campeonato)
                            self.tela.popup_cadastro_criado()
                            return
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except TypeError:
                self.tela.popup_msg_erro_cadastro()
            except DadoIndisponivelError:
                self.tela.popup_msg_erro_dado_indisponivel()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()

    def adicionar_competidores(self, campeonato):
        lista_times = [time.nome for time in self.cm.ct.times_registrados if time.nome not in campeonato.dict_dados()['times']]
        while True:
            self.tela.tela_adicionar_times(lista_times)
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    nomes_competidores = valores['competidores']
                    if len(nomes_competidores) == 0:
                        raise EntradaVaziaError()
                    else:
                        adicionar = [self.cm.ct.buscar_nome(nome_time).id_ for nome_time in nomes_competidores]
                        competidores = [self.cm.ct.buscar_nome(time) for time in nomes_competidores]
                        botao = self.tela.popup_confirmar_adicao(len(competidores))
                        if botao == 'Confirmar':
                            campeonato.adicionar_times(competidores)
                            self.campeonato_dao.atualizar_objeto(campeonato)
                            return
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except TypeError:
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            except CapacidadeMaximaError:
                self.tela.popup_erro_cadastro_cheio()
            except DadoIndisponivelError:
                self.tela.popup_msg_erro_dado_indisponivel()
            finally:
                self.tela.fechaTela()

    def remover_competidores(self, campeonato):
        lista_times = [time.nome for time in self.buscar_nome(campeonato.nome).times if time]
        while True:            
            self.tela.tela_remover_times(lista_times)
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    nomes_competidores = valores['lstbox']
                    if len(nomes_competidores) == 0:
                        raise EntradaVaziaError()
                    else:
                        remover = [self.cm.ct.buscar_nome(nome_time).id_ for nome_time in nomes_competidores]
                        competidores = [time for time in campeonato.times if time.id_ in remover]
                        botao = self.tela.popup_confirmar_remocao(len(competidores))
                        if botao == 'Confirmar':
                            campeonato.remover_times(competidores)
                            self.campeonato_dao.atualizar_objeto(campeonato)
                            return
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
            finally:
                self.tela.fechaTela()

    def carregar_times(self, campeonato):
        for i in range(len(campeonato.times)):
            campeonato.times[i] = self.cm.ct.time_dao.get(campeonato.times[i])
        self.campeonato_dao.atualizar_objeto(campeonato)

    def atualizar_partidas(self, campeonato):
        for i in range(len(campeonato.partidas)):
            campeonato.partidas[i] = self.cm.jc.partidas_dao.get(campeonato.partidas[i])
        self.campeonato_dao.atualizar_objeto(campeonato)

    def alterar(self, campeonato):
        while True:
            self.carregar_times(campeonato)
            campeonato = self.campeonato_dao.get(campeonato)
            dados_camp = campeonato.dict_dados()
            self.tela.menu_alterar(dados_camp)
            botao, valores = self.tela.abreTela()
            janela_aux = self.tela.janela
            try:
                if botao == 'excluir':
                    excluiu = self.excluir(campeonato)
                    if excluiu:
                        return 
                elif botao == 'remover':
                    self.remover_competidores(campeonato)
                    self.tela.janela = janela_aux
                elif botao == 'adicionar':
                    self.adicionar_competidores(campeonato)
                    self.tela.janela = janela_aux
                elif botao == 'Confirmar':
                    alterou = False
                    if valores['n_times'] != campeonato.n_times or valores['campeonato_nome'] != campeonato.nome:
                        alterou = True
                    if alterou:
                        botao = self.tela.popup_confirmar_alteracao()
                        if botao == 'Confirmar':
                            indisponivel = self.buscar_nome(valores['campeonato_nome'])
                            if indisponivel and campeonato.id_ != indisponivel.id_:
                                raise DadoIndisponivelError()
                            else:
                                campeonato.nome = self.tela.strip_str(valores['campeonato_nome'])
                                campeonato.n_times = int(valores['n_times'])
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
            except CapacidadeMaximaError:
                self.tela.popup_erro_cadastro_cheio()
            else:
                self.campeonato_dao.atualizar_objeto(campeonato)
            finally:
                self.tela.janela = janela_aux
                self.tela.fechaTela()

    def listar(self):
        while True:
            lista_info_campeonatos = sorted([(campeonato.nome, f'{campeonato}') for campeonato in self.campeonatos_registrados], key= lambda tupla: tupla[0])
            self.tela.menu_listar(lista_info_campeonatos)
            botao, valores = self.tela.abreTela()
            self.tela.fechaTela()
            if not(botao == sgui.WIN_CLOSED or botao == 'Voltar'):
                campeonato_nome = botao
                campeonato = self.buscar_nome(campeonato_nome)
                self.alterar(campeonato)
            else:
                break

    def excluir(self, campeonato):
        botao = self.tela.popup_msg_excluir()
        if botao == 'Confirmar':
            self.tela.popup_cadastro_excluido()
            campeonato.remover_times(campeonato.times.copy())
            return self.campeonato_dao.remover_e_retornar(campeonato)
        
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
                