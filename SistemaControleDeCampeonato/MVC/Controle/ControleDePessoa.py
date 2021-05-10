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
from MVC.entidade.arbitroDao import ArbitroDAO
from MVC.entidade.tecnico import Tecnico
from MVC.entidade.tecnicoDao import TecnicoDAO
from MVC.entidade.jogador import Jogador
from MVC.entidade.jogadorDao import JogadorDAO
from MVC.limite.tela import Tela
from MVC.limite.telaDePessoa import TelaDePessoa
from MVC.exceptionLista import ListaError
from MVC.exceptionDadosIndisponivel import DadoIndisponivelError
from MVC.exceptionVazia import EntradaVaziaError

    
class ControladorDePessoas(ControladorDeEntidade):

    def __init__(self, controlador_master):
        super().__init__(controlador_master)
        self.__posicoes = {1: Goleiro(), 2: Defensor(), 3: MeioCampista(), 4: Atacante()}
        self.__mentalidades = {1: Defensiva(), 2: Moderada(), 3: Ofensiva()}
        self.__rigidez = {1: Brando(), 2: Moderado(), 3: Severo()}
        self.__jogadores_DAO = JogadorDAO()
        self.__tecnicos_DAO = TecnicoDAO()
        self.__arbitros_DAO = ArbitroDAO()
        self.__tela = TelaDePessoa(self)

    @property
    def tela(self):
        return self.__tela

    @property
    def jogador_dao(self):
        return self.__jogadores_DAO

    @property
    def tecnico_dao(self):
        return self.__tecnicos_DAO

    @property
    def arbitro_dao(self):
        return self.__arbitros_DAO
    
    @tela.setter
    def tela(self, tela):
        if isinstance(tela, Tela):
            self.__tela = tela
            
    @property
    def tecnicos_registrados(self):
        self.tecnico_dao.carregar()
        return self.__tecnicos_DAO.cache
    
    @property
    def jogadores_registrados(self):
        self.jogador_dao.carregar()
        return self.__jogadores_DAO.cache
    
    @property
    def arbitros_registrados(self):
        self.arbitro_dao.carregar()
        return self.__arbitros_DAO.cache
    
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
        return [arbitro.nome for arbitro in self.arbitros_registrados]

    def listar_nomes_tecnicos(self):
        return [tecnico.nome for tecnico in self.tecnicos_registrados]

    def listar_nomes_jogadores(self):
        return [jogador.nome for jogador in self.jogadores_registrados]

    def listar_gdma_disponiveis(self):
        g = []
        d = []
        m = []
        a = []
        for jogador in self.jogadores_registrados:
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
            self.tela.menu_cadastrar(self.dict_dados())
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    if valores['jogador']:
                        nome_jogador = self.tela.strip_str(valores['jogador_nome'])
                        str_posicao = valores['posicao']
                        posicao = self.pegar_posicao(str_posicao)
                        if nome_jogador in self.listar_nomes_jogadores():
                            raise DadoIndisponivelError()
                        if nome_jogador == '' or not posicao:
                            raise EntradaVaziaError()
                        jogador = Jogador(nome_jogador, posicao)
                        botao = self.tela.popup_confirmar_cadastro()
                        if botao == 'Confirmar':
                            self.__jogadores_DAO.add(jogador)
                            self.tela.popup_cadastro_criado()
                    elif valores['tecnico']:
                        nome_tecnico = self.tela.strip_str(valores['tecnico_nome'])
                        str_mentalidade = valores['mentalidade']
                        mentalidade = self.pegar_mentalidade(str_mentalidade)
                        if nome_tecnico in self.listar_nomes_tecnicos():
                            raise DadoIndisponivelError()
                        elif nome_tecnico == '' or not mentalidade:
                            raise EntradaVaziaError()
                        tecnico = Tecnico(nome_tecnico, mentalidade)
                        botao = self.tela.popup_confirmar_cadastro()
                        if botao == 'Confirmar':
                            self.__tecnicos_DAO.add(tecnico)
                            self.tela.popup_cadastro_criado()
                    elif valores['arbitro']:
                        nome_arbitro = self.tela.strip_str(valores['arbitro_nome'])
                        str_rigidez = valores['rigidez']
                        rigidez = self.pegar_rigidez(str_rigidez)
                        if nome_arbitro in self.listar_nomes_arbitros():
                            raise DadoIndisponivelError()
                        elif nome_arbitro == '' or not rigidez:
                            raise EntradaVaziaError()
                        arbitro = Arbitro(nome_arbitro, rigidez)
                        botao = self.tela.popup_confirmar_cadastro()
                        if botao == 'Confirmar':
                            self.__arbitros_DAO.add(arbitro)
                            self.tela.popup_cadastro_criado()
                    else:
                        raise EntradaVaziaError()                    
                else:
                    return
            except ValueError:
                self.tela.popup_msg_erro_cadastro()
            except DadoIndisponivelError:
                self.tela.popup_msg_erro_dado_indisponivel()
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
            self.tela.menu_buscar(self.listar_nomes_jogadores(), self.listar_nomes_tecnicos(), self.listar_nomes_arbitros())
            botao, valores = self.tela.abreTela()
            try:
                if botao == 'Confirmar':
                    if valores['jogador']:
                        nome_jogador = self.tela.selecionar_entradas((valores['in_jnome'], valores['lst_jnome']))
                        jogador = self.buscar_nome(self.jogadores_registrados, nome_jogador)
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
                    jogador = self.buscar_nome(self.jogadores_registrados, cadastro.nome)
                    dados = {'nome': jogador.nome, 'funcao': jogador.funcao, 'time': jogador.time.nome if jogador.time else '', 'posicao': jogador.posicao.posicao, 
                            'gols_m': jogador.gols_marcados, 'gols_c': jogador.gols_concedidos}
                    lista_posicoes = self.dict_dados()['posicoes']
                    self.tela.janela_jogador(dados, lista_posicoes)
                    botao, valores = self.tela.abreTela()
                    if botao == 'Confirmar':
                        if valores['nome_jogador'] != jogador.nome or valores['posicao'] != jogador.posicao.posicao:
                            botao = self.tela.popup_confirmar_alteracao()
                            if botao == 'Confirmar':
                                indisponivel = self.buscar_nome(self.jogadores_registrados, valores['nome_jogador'])
                                if indisponivel and jogador.id_ != indisponivel.id_:
                                    raise DadoIndisponivelError()
                                else:
                                    jogador.nome = self.tela.strip_str(valores['nome_jogador'])
                                    jogador.posicao = self.pegar_posicao(valores['posicao'])
                                    jogador.time = self.cm.ct.buscar_nome(dados['time'])
                                    self.jogador_dao.atualizar_objeto(jogador)
                        cadastro = jogador
                    elif botao == 'excluir':
                        return self.excluir(jogador)
                    else:
                        return
                elif isinstance(cadastro, Tecnico):
                    tecnico = self.buscar_nome(self.tecnicos_registrados, cadastro.nome)
                    dados = {'nome': tecnico.nome, 'funcao': tecnico.funcao, 'mentalidade': tecnico.mentalidade.mentalidade, 'time': tecnico.time.nome if tecnico.time else ''}
                    lista_mentalidades = self.dict_dados()['mentalidades']
                    self.tela.janela_tecnico(dados, lista_mentalidades)
                    botao, valores = self.tela.abreTela()
                    if botao == 'Confirmar':
                        if valores['nome_tecnico'] != tecnico.nome or valores['mentalidade'] != tecnico.mentalidade.mentalidade:
                            botao = self.tela.popup_confirmar_alteracao()
                            if botao == 'Confirmar':
                                indisponivel = self.buscar_nome(self.tecnicos_registrados, valores['nome_tecnico'])
                                if indisponivel and tecnico.id_ != indisponivel.id_:
                                    raise DadoIndisponivelError()
                                else:
                                    tecnico.nome = self.tela.strip_str(valores['nome_tecnico'])
                                    tecnico.mentalidade = self.pegar_mentalidade(valores['mentalidade'])
                                    tecnico.time = self.cm.ct.buscar_nome(dados['time'])
                                    self.tecnico_dao.atualizar_objeto(tecnico)
                        cadastro = tecnico
                    elif botao == 'excluir':
                        return self.excluir(tecnico)
                    else:
                        return
                elif isinstance(cadastro, Arbitro):
                    arbitro = self.buscar_nome(self.arbitros_registrados, cadastro.nome)
                    dados = {'nome': arbitro.nome, 'funcao': arbitro.funcao, 'rigidez': arbitro.rigidez}
                    lista_rigidez = self.dict_dados()['rigidez']
                    self.tela.janela_arbitro(dados, lista_rigidez)
                    botao, valores = self.tela.abreTela()
                    if botao == 'Confirmar':
                        if valores['nome_arbitro'] != arbitro.nome or valores['rigidez'] != arbitro.rigidez.rigidez:
                            botao = self.tela.popup_confirmar_alteracao()
                            if botao == 'Confirmar':
                                indisponivel = self.buscar_nome(self.arbitros_registrados, valores['nome_arbitro'])
                                if indisponivel and arbitro.id_ != indisponivel.id_:
                                    raise DadoIndisponivelError()
                                else:
                                    arbitro.nome = self.tela.strip_str(valores['nome_arbitro'])
                                    arbitro.rigidez = valores['rigidez']
                                    self.arbitro_dao.atualizar_objeto(arbitro)
                        cadastro = arbitro
                    elif botao == 'excluir':
                        return self.excluir(arbitro)
                    else:
                        return
                else:
                    raise EntradaVaziaError()
            except EntradaVaziaError:
                self.tela.popup_msg_erro_cadastro()
            except DadoIndisponivelError:
                self.tela.popup_msg_erro_dado_indisponivel()
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
                time = cadastro.time
                if time != None and time != '':
                    time.remover_jogadores([cadastro])
                    self.cm.ct.time_dao.atualizar_objeto(time)
                self.__jogadores_DAO.remover_e_retornar(cadastro)
            elif isinstance(cadastro, Tecnico):
                time = cadastro.time
                if time != None and time != '':
                    time.tecnico = None
                    self.cm.time_dao.atualizar_objeto(time)
                self.__tecnicos_DAO.remover_e_retornar(cadastro)
            elif isinstance(cadastro, Arbitro):
                self.__arbitros_DAO.remover_e_retornar(cadastro)
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


    
