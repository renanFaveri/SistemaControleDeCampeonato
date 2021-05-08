from .controleDeEntidade import ControladorDeEntidade
from .controleDeTime import ControladorDeTimes
from MVC.entidade.pessoa import Pessoa
from MVC.entidade.posicao import Posicao
from MVC.entidade.goleiro import Goleiro
from MVC.entidade.defensor import Defensor
from MVC.entidade.meioCampo import MeioCampista
from MVC.entidade.atacante import Atacante
from MVC.entidade.mentalidade import Mentalidade
from MVC.entidade.defensiva import Defensiva
from MVC.entidade.moderada import Moderada
from MVC.entidade.ofensiva import Ofensiva
from MVC.entidade.rigidez import Rigidez
from MVC.entidade.brando import Brando
from MVC.entidade.moderado import Moderado
from MVC.entidade.severo import Severo
from MVC.entidade.arbitro import Arbitro
from MVC.entidade.tecnico import Tecnico
from MVC.entidade.jogador import Jogador
from MVC.entidade.jogadorDao import JogadorDAO
from MVC.limite.tela import Tela
from MVC.limite.telaDePessoa import TelaDePessoas
from MVC.exceptionLista import ListaError
from MVC.exceptionDadosIndisponivel import DadoIndisponivelError
from MVC.exceptionVazia import EntradaVaziaError

    
class ControladorDePessoas(ControladorDeEntidade):
    
    def __init__(self, controlador_master):
        self.__controlador_master = controlador_master
        self.__posicoes = {1: Goleiro(), 2: Defensor(), 3: MeioCampista(), 4: Atacante()}
        self.__mentalidades = {1: Defensiva(), 2: Moderada(), 3: Ofensiva()}
        self.__rigidez = {1: Brando(), 2: Moderado(), 3: Severo()}
        self.__jogador_DAO = JogadorDAO()
        self.__tecnicos_registrados = []
        self.__arbitros_registrados = [Arbitro('Margarida', self.__rigidez[3])]
        self.__tela = TelaDePessoas(self)

    @property
    def jogador_DAO(self):
        return self.__jogador_DAO.cache

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        if isinstance(tela, Tela):
            self.__tela = tela

    @property
    def tecnicos_registrados(self):
        return self.__tecnicos_registrados

    @property
    def arbitros_registrados(self):
        return self.__arbitros_registrados

    @property
    def posicoes(self):
        return self.__posicoes

    @property
    def mentalidades(self):
        return self.__mentalidades

    @property
    def rigidez(self):
        return self.__rigidez

    def dict_dados(self):
        return {'posicoes': [self.posicoes[chave].posicao for chave in self.posicoes], 'mentalidades': [self.mentalidades[chave].mentalidade for chave in self.mentalidades],
                'rigidez': [self.rigidez[chave].rigidez for chave in self.rigidez]}

    def listar_nomes_arbitros(self):
        return [arbitro.nome for arbitro in self.__arbitros_registrados]

    def listar_nomes_tecnicos(self):
        return [tecnico.nome for tecnico in self.__tecnicos_registrados]

    def listar_nomes_jogadores(self):
        return [jogador.nome for jogador in self.__jogador_DAO.cache]

    def listar_gdma_disponiveis(self):
        g = []
        d = []
        m = []
        a = []
        for jogador in self.__jogador_DAO.cache:
            if not jogador.time or jogador.time == '':
                if jogador.posicao.posicao == 'Goleiro':
                    g.append(jogador.nome)
                elif jogador.posicao.posicao == 'Defensor':
                    d.append(jogador.nome)
                elif jogador.posicao.posicao == 'Meio campista':
                    m.append(jogador.nome)
                else:
                    a.append(jogador.nome)
        g = sorted(g)
        d = sorted(d)
        m = sorted(m)
        a = sorted(a)
        return g,d,m,a

    def pegar_posicao(self, nome_posicao):
        encontrou = False
        for i in range(len(self.__posicoes)):
            if self.__posicoes[i+1].posicao == nome_posicao:
                encontrou = self.__posicoes[i+1]
                print(encontrou)
        if encontrou:
            return encontrou
        else:
            raise EntradaVaziaError()

    def pegar_mentalidade(self, nome_mentalidade):
        encontrou = False
        for i in range(len(self.__mentalidades)):
            if self.__mentalidades[i+1].mentalidade == nome_mentalidade:
                encontrou =  self.__mentalidades[i+1]
        if encontrou:
            return encontrou
        else:
            raise EntradaVaziaError()

    def pegar_rigidez(self, nome_rigidez):
        encontrou = False
        for i in range(len(self.__rigidez)):
            if self.__rigidez[i+1].rigidez == nome_rigidez:
                encontrou = self.__rigidez[i+1]
        if encontrou:
            return encontrou
        else:
            raise EntradaVaziaError()

    def cadastrar(self): 
        while True:
            self.tela.tela_cadastrar_pessoas(self.dict_dados())
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    if valores['jogador']:
                        nome_jogador = self.tela.strip_str(valores['jogador_nome']).title()
                        str_posicao = valores['posicao']
                        posicao = self.pegar_posicao(str_posicao)
                        if nome_jogador in self.listar_nomes_jogadores():
                            raise DadoIndisponivelError()
                        if nome_jogador == '' or not posicao:
                            raise EntradaVaziaError()
                        jogador = Jogador(nome_jogador, posicao)
                        botao = self.tela.popup_confirmar_cadastro((jogador.nome, jogador.funcao, jogador.posicao.posicao))
                        if botao == 'Confirmar':
                            self.__jogador_DAO.add(jogador)
                            self.tela.popup_cadastro_criado()
                    elif valores['tecnico']:
                        nome_tecnico = self.tela.strip_str(valores['tecnico_nome']).title()
                        str_mentalidade = valores['mentalidade']
                        mentalidade = self.pegar_mentalidade(str_mentalidade)
                        if nome_tecnico in self.listar_nomes_tecnicos():
                            raise DadoIndisponivelError()
                        elif nome_tecnico == '' or not mentalidade:
                            raise EntradaVaziaError()
                        tecnico = Tecnico(nome_tecnico, mentalidade)
                        botao = self.tela.popup_confirmar_cadastro((tecnico.nome, tecnico.funcao, tecnico.mentalidade.mentalidade))
                        if botao == 'Confirmar':
                            self.__tecnicos_registrados.append(tecnico)
                            self.tela.popup_cadastro_criado()
                    elif valores['arbitro']:
                        nome_arbitro = self.tela.strip_str(valores['arbitro_nome']).title()
                        str_rigidez = valores['rigidez']
                        rigidez = self.pegar_rigidez(str_rigidez)
                        if nome_arbitro in self.listar_nomes_arbitros():
                            raise DadoIndisponivelError()
                        elif nome_arbitro == '' or not rigidez:
                            raise EntradaVaziaError()
                        arbitro = Arbitro(nome_arbitro, rigidez)
                        botao = self.tela.popup_confirmar_cadastro((arbitro.nome, arbitro.funcao, arbitro.rigidez.rigidez))
                        if botao == 'Confirmar':
                            self.__arbitros_registrados.append(arbitro)
                            self.tela.popup_cadastro_criado()
                    else:
                        raise EntradaVaziaError()                    
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except DadoIndisponivelError:
                #fazer popup 'já existe um cadastro com essas informações
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()

    def buscar_nome(self, lista = None, nome = None):
        for obj in lista:
            if obj.nome.lower() == nome.lower():
                return obj

    def buscar(self):
        while True:
            self.tela.menu_buscar_pessoas(self.listar_nomes_jogadores(), self.listar_nomes_tecnicos(), self.listar_nomes_arbitros())
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    if valores['jogador']:
                        nome_jogador = self.tela.selecionar_entradas((valores['in_jnome'], valores['lst_jnome']))
                        jogador = self.buscar_nome(self.__jogador_DAO.cache, nome_jogador)
                        if not jogador:
                            raise EntradaVaziaError()
                        else:
                            self.tela.fechaTela()
                            return self.alterar(jogador)
                    elif valores['tecnico']:
                        nome_tecnico = self.tela.selecionar_entradas((valores['in_tnome'], valores['lst_tnome']))
                        tecnico = self.buscar_nome(self.tecnicos_registrados, nome_tecnico)
                        if not tecnico:
                            raise EntradaVaziaError()
                        else:
                            self.tela.fechaTela()
                            return self.alterar(tecnico)
                    elif valores['arbitro']:
                        nome_arbitro = self.tela.selecionar_entradas((valores['in_anome'], valores['lst_anome']))
                        arbitro = self.buscar_nome(self.arbitros_registrados, nome_arbitro)
                        if not arbitro:
                            raise EntradaVaziaError()
                        else:
                            self.tela.fechaTela()
                            return self.alterar(arbitro)
                    else:
                        raise EntradaVaziaError()
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()

    def alterar(self, cadastro):
        while True:
            try:
                if isinstance(cadastro, Jogador):
                    jogador = cadastro
                    dados = {'nome': jogador.nome, 'funcao': jogador.funcao, 'time': jogador.time.nome if jogador.time else '', 'posicao': jogador.posicao.posicao, 
                            'gols_m': jogador.gols_marcados, 'gols_c': jogador.gols_concedidos}
                    lista_posicoes = self.dict_dados()['posicoes']
                    self.tela.janela_jogador(dados, lista_posicoes)
                    botao, valores = self.tela.abreTela()
                    if botao == 'Confirmar':
                        if valores['nome_jogador'] != jogador.nome or valores['posicao'] != jogador.posicao.posicao:
                            botao = self.tela.popup_confirmar_alteracao()
                            if botao == 'Confirmar':
                                jogador.posicao = self.pegar_posicao(valores['posicao'])
                                indisponivel = self.buscar_nome(self.__jogador_DAO.cache, valores['nome_jogador'])
                                if indisponivel:
                                    raise DadoIndisponivelError()
                                else:
                                    jogador.nome = valores['nome_jogador']
                                    self.__jogador_DAO.atualizar(jogador)
                    elif botao == 'excluir':
                        return self.excluir(jogador) and self.__jogador_DAO.remove(jogador)
                    else:
                        return
                elif isinstance(cadastro, Tecnico):
                    tecnico = cadastro
                    dados = {'nome': tecnico.nome, 'funcao': tecnico.funcao, 'mentalidade': tecnico.mentalidade.mentalidade}
                    lista_mentalidades = self.dict_dados()['mentalidades']
                    self.tela.janela_tecnico(dados, lista_mentalidades)
                    botao, valores = self.tela.abreTela()
                    if botao == 'Confirmar':
                        if valores['nome_tecnico'] != tecnico.nome or valores['mentalidade'] != tecnico.mentalidade.mentalidade:
                            botao = self.tela.popup_confirmar_alteracao()
                            if botao == 'Confirmar':
                                tecnico.mentalidade = self.pegar_mentalidade(valores['mentalidade'])
                                indisponivel = self.buscar_nome(self.tecnicos_registrados, valores['nome_tecnico'])
                                if indisponivel:
                                    raise DadoIndisponivelError()
                                else:
                                    tecnico.nome = valores['nome_tecnico']
                    elif botao == 'excluir':
                        return self.excluir(tecnico)
                    else:
                        return
                elif isinstance(cadastro, Arbitro):
                    arbitro = cadastro
                    dados = {'nome': arbitro.nome, 'funcao': arbitro.funcao, 'rigidez': arbitro.rigidez}
                    lista_rigidez = self.dict_dados()['rigidez']
                    self.tela.janela_arbitro(dados, lista_rigidez)
                    botao, valores = self.tela.abreTela()
                    if botao == 'Confirmar':
                        if valores['nome_arbitro'] != arbitro.nome or valores['rigidez'] != arbitro.rigidez.rigidez:
                            botao = self.tela.popup_confirmar_alteracao()
                            if botao == 'Confirmar':
                                arbitro.rigidez = valores['rigidez']
                                indisponivel = self.buscar_nome(self.arbitros_registrados, valores['nome_arbitro'])
                                if indisponivel:
                                    raise DadoIndisponivelError()
                                else:
                                    arbitro.nome = valores['nome_arbitro']
                    elif botao == 'excluir':
                        return self.excluir(arbitro)
                    else:
                        return
                else:
                    raise EntradaVaziaError()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            except DadoIndisponivelError:
                #fazer popup 'já existe um cadastro com essas informações
                self.tela.popup_msg_erro_cadastro()
            except TypeError:
                self.tela.popup_msg_erro_cadastro()
            finally:
                self.tela.fechaTela()


    def listar(self, opcao = None):
        pass


    def excluir(self, cadastro):
        botao = self.tela.popup_msg_excluir()
        if botao == 'Confirmar':
            if isinstance(cadastro, Jogador):
                lista = self.__jogador_DAO.cache
                time = cadastro.time
                if not time == None or time != '':
                    time.remover_jogadores([cadastro])
                    #OBS: Atualizar persistencia de time 
                lista.remove(cadastro)
            elif isinstance(cadastro, Tecnico):
                lista = self.__tecnicos_registrados
                time = cadastro.time
                if not time == None or time != '':
                    time.tecnico = None
                lista.remove(cadastro)
            elif isinstance(cadastro, Arbitro):
                lista = self.__arbitros_registrados
                lista.remove(cadastro)
            self.tela.popup_cadastro_excluido()
        return


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
