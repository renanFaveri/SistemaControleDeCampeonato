from .controleDeEntidade import ControladorDeEntidade
from MVC.entidade.time import Time
from MVC.exceptionLista import ListaError
from MVC.limite.telaDeTime import TelaDeTimes
from MVC.limite.tela import Tela
from MVC.entidade.tecnico import Tecnico
from MVC.entidade.jogador import Jogador

class ControladorDeTimes(ControladorDeEntidade):

    def __init__(self, controlador_master):
        self.__controlador_master = controlador_master
        self.__times_registrados = [Time('Man Utd', 'red', 'white'), Time('Man City', 'light blue', 'white')]
        self.__times_registrados[0].adicionar_jogadores(self.__controlador_master.cp.jogadores_registrados[0:2])
        self.__times_registrados[1].adicionar_jogadores(self.__controlador_master.cp.jogadores_registrados[2:])
        self.__tela = TelaDeTimes(self)
        
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
            
    @property
    def times_registrados(self):
        return self.__times_registrados
                    
            
    def buscar_nome(self, nome = None):
        if nome is None:
            pass
            # nome = self.tela.recebe_str('Procurar time por nome: ')
        for obj in self.times_registrados:
            if obj.nome.lower() == nome.lower():
                return obj


    def buscar_id(self):
        id_ = self.tela.recebe_int('Procurar time por ID: ')
        contador = 0
        while contador < len(self.times_registrados):
            if id_ == self.times_registrados[contador].id_:
                self.mostrar_informacoes(self.times_registrados[contador])
                return self.times_registrados[contador]
            else:
                contador += 1

    def buscar(self):
        buscando = True
        while buscando:
            self.tela.menu_buscar_times()
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
                        raise ValueError
                    else:
                        time = Time(nome_time, cor_primaria, cor_secundaria)
                        self.__times_registrados.append(time)
                        self.tela.fechaTela()
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

    
    def contratar(self, time):
        self.tela.tela_contratar_jogador(time)
        botao, valores = self.tela.abreTela()
        if botao == 'Confirmar':
            negociados = valores['box_goleiros'] + valores['box_defensores'] + valores['box_meio_campistas'] + valores['box_atacantes']
            jogadores = [self.cm.cp.buscar_nome(self.cm.cp.jogadores_registrados, jogador) for jogador in negociados]
            botao = self.tela.popup_confirmar_compra(jogadores)
            if botao == 'Confirmar':
                time.adicionar_jogadores(jogadores)
        self.tela.fechaTela()
        return 

    def vender(self, time):
        self.tela.tela_vender_jogador(time)
        botao, valores = self.tela.abreTela()
        if botao == 'Confirmar':
            jogadores = [self.cm.cp.buscar_nome(self.cm.cp.jogadores_registrados, jogador) for jogador in valores['lstbox']]
            botao = self.tela.popup_confirmar_venda(jogadores)
            if botao == 'Confirmar':
                time.remover_jogadores(jogadores)
        self.tela.fechaTela()
        return 

     
    def alterar(self, time):
        while True:
            self.tela.janela_time(time)
            botao, valores = self.tela.abreTela()
            janela_aux = self.tela.janela
            if botao == 'excluir':
                excluiu = self.excluir(time)
                self.tela.fechaTela()
                if excluiu:
                    break 
            elif botao == 'Vender':
                self.vender(time)
                self.tela.janela = janela_aux
                self.tela.fechaTela()
            elif botao == 'Contratar':
                self.contratar(time)
                self.tela.janela = janela_aux
                self.tela.fechaTela()
            elif botao == 'Confirmar':
                alterou = False
                if valores['cor1'] != time.cor_primaria or valores['cor2'] != time.cor_secundaria or valores['time_nome'] != time.nome:
                    alterou = True
                if alterou:
                    botao = self.tela.popup_confirmar_alteracao()
                    if botao == 'Confirmar':
                        time.nome = valores['time_nome'].title()
                        time.cor_secundaria = valores['cor2']
                        time.cor_primaria = valores['cor1']
                self.tela.fechaTela()
            else:
                self.tela.janela = janela_aux
                self.tela.fechaTela()
                break
        return self.lista()
            

    def listar(self, n_entradas = None):
        while True:
            self.tela.listar_times()
            botao, valores = self.tela.abreTela()
            time = botao
            self.tela.fechaTela()
            try:
                if time in self.times_registrados:
                    return self.alterar(time)
                else:
                    break
            except:
                pass

     
    def excluir(self, time):
        botao = self.tela.popup_msg_excluir()
        if botao == 'Confirmar':
            i = self.times_registrados.index(time)
            time.remover_jogadores(time.jogadores.copy())
            self.times_registrados.pop(i)
     
    
    def mostrar_informacoes(self, time):
        self.tela.mostrar_mensagem('')
        self.tela.mostrar_mensagem('> ')
        self.tela.mostrar_mensagem(time)
        
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


