from MVC.entidade.campeonato import Campeonato 
from MVC.entidade.time import Time
from .controleDeEntidade import ControladorDeEntidade
from MVC.limite.tela import Tela
from MVC.limite.telaDeCampeonato import TelaDeCampeonatos
from MVC.exceptionLista import ListaError
from MVC.exceptionVazia import EntradaVaziaError


class ControladorDeCampeonatos(ControladorDeEntidade):
    
    def __init__(self, controlador_master):
        self.__controlador_master = controlador_master
        self.__campeonatos_registrados = []
        self.__tela = TelaDeCampeonatos(self)

    @property
    def tela(self):
        return self.__tela
    
    @tela.setter
    def tela(self, tela):
        if isinstance(tela, Tela):
            self.__tela = tela

    @property
    def cm(self):
        return self.__controlador_master
            
    @property
    def campeonatos_registrados(self):
        return self.__campeonatos_registrados

    def listar_nomes_campeonatos(self):
        return [campeonato.nome for campeonato in self.__campeonatos_registrados]
            
            
    def buscar_nome(self, nome = None):
        for obj in self.__campeonatos_registrados:
            if obj.nome.lower() == nome.lower():
                return obj
         
    def buscar(self):
        buscando = True
        while buscando:
            self.tela.menu_buscar_campeonatos()
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
                    nome_campeonato = self.tela.strip_str(valores['campeonato_nome'])
                    n_times = int(valores['n_times'])
                    if 'None' == nome_campeonato or self.buscar_nome(nome_campeonato):
                        raise ValueError()
                    else:
                        campeonato = Campeonato(nome_campeonato, n_times)
                        self.__campeonatos_registrados.append(campeonato)
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

    def adicionar_competidores(self, campeonato):
        # limite n times
        # levantar e tratar exceções
        self.tela.tela_adicionar_times(campeonato)
        botao, valores = self.tela.abreTela()
        if botao == 'Confirmar':
            nomes_competidores = valores['competidores']
            competidores = [self.cm.ct.buscar_nome(time) for time in nomes_competidores]
            botao = self.tela.popup_confirmar_compra(competidores)
            if botao == 'Confirmar':
                campeonato.adicionar_times(competidores)
        self.tela.fechaTela()
        return 

    def remover_competidores(self, campeonato):
        self.tela.tela_remover_times(campeonato)
        botao, valores = self.tela.abreTela()
        if botao == 'Confirmar':
            nomes_competidores = valores['lstbox']
            competidores = [self.cm.ct.buscar_nome(time) for time in nomes_competidores]
            botao = self.tela.popup_confirmar_venda(competidores)
            if botao == 'Confirmar':
                campeonato.adicionar_times(competidores)
        self.tela.fechaTela()
        return 

    def alterar(self, campeonato):
        while True:
            self.tela.janela_campeonato(campeonato)
            botao, valores = self.tela.abreTela()
            janela_aux = self.tela.janela
            try:
                if botao == 'excluir':
                    excluiu = self.excluir(campeonato)
                    if excluiu:
                        break 
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
                            campeonato.nome = self.tela.strip_str(valores['campeonato_nome'].title())
                            campeonato.n_times = valores['n_times']
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
        while True:
            self.tela.listar_campeonatos()
            botao, valores = self.tela.abreTela()
            campeonato = botao
            self.tela.fechaTela()
            try:
                if campeonato in self.campeonatos_registrados:
                    return self.alterar(campeonato)
                else:
                    break
            except:
                pass

    def excluir(self, campeonato):
        botao = self.tela.popup_msg_excluir()
        if botao == 'Confirmar':
            i = self.campeonatos_registrados.index(campeonato)
            campeonato.remover_competidores(campeonato.times.copy())
            return self.campeonatos_registrados.pop(i)       
        
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
                     