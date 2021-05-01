from .controleDeEntidade import ControladorDeEntidade
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
from MVC.limite.tela import Tela
from MVC.limite.telaDePessoa import TelaDePessoas
from MVC.exceptionLista import ListaError



class ControladorDePessoas(ControladorDeEntidade):
    
    def __init__(self, controlador_master):
        self.__controlador_master = controlador_master
        self.__posicoes = {1: Goleiro(), 2: Defensor(), 3: MeioCampista(), 4: Atacante()}
        self.__mentalidades = {1: Defensiva(), 2: Moderada(), 3: Ofensiva()}
        self.__rigidez = {1: Brando(), 2: Moderado(), 3: Severo()}
        self.__jogadores_registrados = [Jogador('Jogador Um', self.__posicoes[1]), Jogador('Jogador Dois', self.__posicoes[4]), Jogador('Jogador Tres', self.__posicoes[1]), Jogador('Jogador Quatro', self.__posicoes[4]), Jogador('Jogador Cinco', self.__posicoes[1])]
        self.__tecnicos_registrados = []
        self.__arbitros_registrados = [Arbitro('Margarida', self.__rigidez[3])]
        self.__tela = TelaDePessoas(self)
        

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
    def jogadores_registrados(self):
        return self.__jogadores_registrados
    
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

    
    def cadastrar_jogador(self):
        nome_jogador = self.tela.recebe_str('Informe o nome do jogador: ', 3)
        menu = ['1 - Goleiro', '2 - Defensor','3 - Meio campista', '4 - Atacante']
        opcao = self.tela.exibir_menu(menu, range(1,5))
        posicao = self.__posicoes[opcao]
        try:
            jogador = Jogador(nome_jogador, posicao)
            contador = 0
            while contador < len(self.__jogadores_registrados):
                if jogador.nome ==  self.__jogadores_registrados[contador].nome and jogador.posicao == self.__jogadores_registrados[contador].posicao:
                        raise ValueError
                else:
                    contador += 1
            self.__jogadores_registrados.append(jogador)
            self.mostrar_informacoes(jogador)
        except TypeError:
            self.tela.mostrar_mensagem('»»»» Não foi informada a posição do jogador.')

        
        
    def cadastrar_tecnico(self):
        nome_tecnico = self.tela.recebe_str('Digite o nome do técnico: ', 3)
        menu = ['1 - Defensiva', '2 - Moderada','3 - Ofensiva']
        opcao = self.tela.exibir_menu(menu, range(1,4))
        mentalidade = self.__mentalidades[opcao]
        try:
            tecnico = Tecnico(nome_tecnico, mentalidade)
            contador = 0
            while contador < len(self.__tecnicos_registrados):
                if tecnico.nome ==  self.__tecnicos_registrados[contador].nome and tecnico.mentalidade == self.__tecnicos_registrados[contador].mentalidade:
                    raise ValueError
                else:
                    contador += 1
            self.__tecnicos_registrados.append(tecnico)
            self.mostrar_informacoes(tecnico)
        except TypeError:
            self.tela.mostrar_mensagem('»»»» Não foi informada a mentalidade do técnico.')
        
        
    def cadastrar_arbitro(self):
        nome_arbitro = self.tela.recebe_str('Digite o nome do ábitro: ', 3)
        menu = ['1 - Brando', '2 - Moderado','3 - Severo']
        opcao = self.tela.exibir_menu(menu, range(1,4))
        rigidez = self.__rigidez[opcao]
        try:
            arbitro = Arbitro(nome_arbitro, rigidez)
            contador = 0
            while contador < len(self.__arbitros_registrados):
                if arbitro.nome ==  self.__arbitros_registrados[contador].nome and arbitro.rigidez == self.__arbitros_registrados[contador].rigidez:
                    raise ValueError
                else:
                    contador += 1
            self.__arbitros_registrados.append(arbitro)
            self.mostrar_informacoes(arbitro)
        except TypeError:
            self.tela.mostrar_mensagem('»»»» Não foi informada a rigidez do árbitro.')     
    
                
    def cadastrar(self):
        cadastrando = True
        while cadastrando:
            opcoes = {1: self.cadastrar_jogador, 2: self.cadastrar_tecnico, 3: self.cadastrar_arbitro}
            menu = ['1 - Cadastrar jogador', '2 - Cadastrar técnico','3 - Cadastrar árbitro', '0 - Voltar ao menu inicial']
            opcao = self.tela.exibir_menu(menu, range(4))
            if opcao != 0:
                try:
                    opcoes[opcao]()
                except ValueError:
                    self.tela.mostrar_mensagem('»»»» Já existe uma pessoa com esses dados.')
                cadastrando = self.tela.recebe_int('Realizar nova operação? [1 - Sim / 0 - Não]: ', [0,1])
            else:
                cadastrando = False
        
    def buscar_nome(self, lista = None, nome = None):
        if nome is None:
            nome = self.tela.recebe_str('Procurar por nome: ')
        for obj in lista:
            if obj.nome.lower() == nome.lower():
                self.mostrar_informacoes(obj)
                return obj
    
    def buscar_id(self, lista):
        id_ = self.tela.recebe_int('Procurar por ID: ')
        contador = 0
        while contador < len(lista):
            if id_ == lista[contador].id_:
                self.mostrar_informacoes(lista[contador])
                return lista[contador]
            else:
                contador += 1
                
    def buscar_posicao(self):
        posicao = self.tela.recebe_int('Procurar jogador por posição: 1 - Goleiro, 2 - Defensor, 3 - Meio campista, 4 - Atacante',
                                       range(1,5))
        encontrados = []
        for obj in self.__jogadores_registrados:
            if obj.posicao == self.__posicoes[posicao]:
                encontrados.append(obj)
        for pessoa in encontrados:
            self.mostrar_informacoes(pessoa)
    
    def buscar_mentalidade(self):
        mentalidade = self.tela.recebe_int('Procurar técnico por mentalidade: 1 - Defensiva, 2 - Moderada, 3 - Ofensiva',
                                       range(1,4))
        encontrados = []
        for obj in self.__tecnicos_registrados:
            if obj.mentalidade == self.__mentalidades[mentalidade]:
                encontrados.append(obj)
        for pessoa in encontrados:
            self.mostrar_informacoes(pessoa)
    
    def buscar_rigidez(self):
        rigidez = self.tela.recebe_int('Procurar técnico por mentalidade: 1 - Brando, 2 - Moderado, 3 - Severo',
                                       range(1,4))
        encontrados = []
        for obj in self.__arbitros_registrados:
            if obj.rigidez == self.__rigidez[rigidez]:
                encontrados.append(obj)
        for pessoa in encontrados:
            self.mostrar_informacoes(pessoa)
    
    def buscar_jogador(self, metodo):
        if metodo == 1:
            return self.buscar_nome(self.__jogadores_registrados)
        elif metodo == 2:
            return self.buscar_id(self.__jogadores_registrados)
        elif metodo == 3:
            return self.buscar_posicao()
            
    def buscar_tecnico(self, metodo):
        if metodo == 1:
            return self.buscar_nome(self.__tecnicos_registrados)
        elif metodo == 2:
            return self.buscar_id(self.__tecnicos_registrados)
        elif metodo == 3:
            return self.buscar_mentalidade()
        
    def buscar_arbitro(self, metodo):
        if metodo == 1:
            return self.buscar_nome(self.__arbitros_registrados)
        elif metodo == 2:
            return self.buscar_id(self.__arbitros_registrados)
        elif metodo == 3:
            return self.buscar_rigidez()    
        
    def buscar(self, lista):
        if isinstance(lista, list):            
            buscando = True
            opcoes = {1: self.buscar_nome, 2: self.buscar_id}
            while buscando:
                menu = ['1 - Buscar por nome', '2 - Buscar por ID', '0 - Voltar ao menu inicial']
                opcao = self.tela.exibir_menu(menu, range(3))
                if opcao == 0:
                    buscando = False
                else:
                    resultado = opcoes[opcao](lista)
                    if resultado is None:
                        self.tela.mostrar_mensagem('Não há pessoa cadastrada com esses dados.')
                        buscando = self.tela.recebe_int('Procurar outra pessoa? [1 - Sim / 0 - Não]: ', [0,1])
                    else:
                        return resultado
        else:
            raise ListaError
                
             
    def buscar_pessoas(self):
        buscando = True
        while buscando:
            menu = ['1 - Bucar jogador', '2 - Buscar técnico', '3 - Buscar árbitro', '0 - Voltar ao menu inicial']
            opcao = self.tela.exibir_menu(menu, range(4))
            if opcao == 1:
                menu = ['1 - Bucar por nome', '2 - Buscar por ID', '3 - Buscar por posição']
                opcao = self.tela.exibir_menu(menu, range(1,4))
                self.buscar_jogador(opcao)
            elif opcao == 2:
                menu = ['1 - Bucar por nome', '2 - Buscar por ID', '3 - Buscar por mentalidade']
                opcao = self.tela.exibir_menu(menu, range(1,4))
                self.buscar_tecnico(opcao)
            elif opcao == 3:
                menu = ['1 - Bucar por nome', '2 - Buscar por ID', '3 - Buscar por rigidez']
                opcao = self.tela.exibir_menu(menu, range(1,4))
                self.buscar_arbitro(opcao)
            elif opcao == 0:
                buscando = False
                return
            buscando = self.tela.recebe_int('Procurar outra pessoa? [1 - Sim / 0 - Não]: ', [0,1])
            
        
    def alterar_jogador(self):
        menu = ['Escolher cadastro de jogador a ser alterado.', '1 - Escolher por nome', '2 - Escolher por ID']
        opcao = self.tela.exibir_menu(menu, range(1,3))
        jogador = self.buscar_jogador(opcao)
        if jogador is not None:
            alterando = True
            while alterando:
                try:
                    menu = ['Informe os atributos a serem alterados:',
                            '1 - Nome',
                            '2 - Posição',
                            '3 - Gols marcados',
                            '4 - Gols cedidos',
                            '5 - Disponibilidade',
                            '0 - Sair']
                    opcao = self.tela.exibir_menu(menu, range(6))
                    if opcao == 1:
                            nome_jogador = self.tela.recebe_str('Informe o nome do jogador: ', 3)
                            contador = 0
                            while contador < len(self.__jogadores_registrados):
                                if nome_jogador ==  self.__jogadores_registrados[contador].nome and jogador.posicao == self.__jogadores_registrados[contador].posicao:
                                    raise ValueError
                                else:
                                    contador += 1
                            jogador.nome = nome_jogador
                    elif opcao == 2:
                            menu = ['1 - Goleiro', '2 - Defensor','3 - Meio campista', '4 - Atacante']
                            opcao = self.tela.exibir_menu(menu, range(1,5))
                            posicao = self.__posicoes[opcao]
                            contador = 0
                            while contador < len(self.__jogadores_registrados):
                                if jogador.nome ==  self.__jogadores_registrados[contador].nome and posicao == self.__jogadores_registrados[contador].posicao:
                                    raise ValueError
                                else:
                                    contador += 1
                            jogador.posicao = posicao
                    elif opcao == 3:
                            gols_marcados = self.tela.recebe_int('Informe o número de gols marcados.')
                            jogador.gols_marcados = gols_marcados
                    elif opcao == 4:
                            gols_concedidos = self.tela.recebe_int('Informe o número de gols cedidos.')
                            jogador.gols_concedidos = gols_concedidos
                    elif opcao == 5:
                            menu = ['Informe a disponibilidade do jogador: 1 - Disponível, 0 - Indisponível']
                            opcao = self.tela.exibir_menu(menu, range(0,2))
                            jogador.disponivel = opcao == True
                    else:
                        alterando = False
                        return
                    alterando = self.tela.recebe_int('Realizar outra operação? [1 - Sim / 0 - Não]: ', [0,1])
                except ValueError:
                    self.tela.mostrar_mensagem('»»»» Já existe uma pessoa com esses dados.')
    
    def alterar_tecnico(self):
        menu = ['Escolher cadastro de técnico a ser alterado.',
                '1 - Escolher por nome',
                '2 - Escolher por ID']
        opcao = self.tela.exibir_menu(menu, range(1,3))
        tecnico = self.buscar_tecnico(opcao)
        if tecnico is not None:
            alterando = True
            while alterando:
                try:
                    menu = ['Informe os atributos a serem alterados:',
                            '1 - Nome',
                            '2 - Mentalidade',
                            '3 - Disponibilidade',
                            '0 - Sair']
                    opcao = self.tela.exibir_menu(menu, range(4))
                    if opcao == 1:
                            nome_tecnico = self.tela.recebe_str('Informe o nome do técnico: ', 3)
                            contador = 0
                            while contador < len(self.__tecnicos_registrados):
                                if nome_tecnico ==  self.__tecnicos_registrados[contador].nome and tecnico.mentalidade == self.__tecnicos_registrados[contador].mentalidade:
                                    raise ValueError
                                else:
                                    contador += 1
                            tecnico.nome = nome_tecnico
                    elif opcao == 2:
                            menu = ['1 - Defensiva', '2 - Moderada','3 - Ofensiva']
                            opcao = self.tela.exibir_menu(menu, range(1,4))
                            mentalidade = self.__mentalidades[opcao]
                            contador = 0
                            while contador < len(self.__tecnicos_registrados):
                                if tecnico.nome ==  self.__tecnicos_registrados[contador].nome and mentalidade == self.__tecnicos_registrados[contador].mentalidade:
                                    raise ValueError
                                else:
                                    contador += 1
                            tecnico.mentalidade = mentalidade
                    elif opcao == 3:
                            menu = ['Informe a disponibilidade do técnico:',
                                    '1 - Disponível',
                                    '0 - Indisponível']
                            opcao = self.tela.exibir_menu(menu, range(0,2))
                            tecnico.disponivel = opcao == True
                    else:
                            alterando = False
                            return
                    alterando = self.tela.recebe_int('Realizar outra operação? [1 - Sim / 0 - Não]: ', [0,1])
                except ValueError:
                    self.tela.mostrar_mensagem('»»»» Já existe uma pessoa com esses dados.')
    
    def alterar_arbitro(self):
        menu = ['Escolher cadastro de árbitro a ser alterado.',
                '1 - Escolher por nome',
                '2 - Escolher por ID']
        opcao = self.tela.exibir_menu(menu, range(1,3))
        arbitro = self.buscar_arbitro(opcao)
        if arbitro is not None:
            alterando = True
            while alterando:
                try:
                    menu = ['Informe os atributos a serem alterados:',
                            '1 - Nome',
                            '2 - Rigidez',
                            '0 - Sair']
                    opcao = self.tela.exibir_menu(menu, range(3))
                    if opcao == 1:
                            nome_arbitro = self.tela.recebe_str('Informe o nome do árbitro: ', 3)
                            contador = 0
                            while contador < len(self.__arbitros_registrados):
                                if nome_arbitro ==  self.__arbitros_registrados[contador].nome and arbitro.rigidez == self.__arbitros_registrados[contador].rigidez:
                                    raise ValueError
                                else:
                                    contador += 1
                            arbitro.nome = nome_arbitro
                    elif opcao == 2:
                            menu = ['1 - Brando', '2 - Moderado','3 - Severo']
                            opcao = self.tela.exibir_menu(menu, range(1,4))
                            rigidez = self.__rigidez[opcao]
                            contador = 0
                            while contador < len(self.__arbitros_registrados):
                                if arbitro.nome ==  self.__arbitros_registrados[contador].nome and rigidez == self.__arbitros_registrados[contador].rigidez:
                                    raise ValueError
                                else:
                                    contador += 1
                            arbitro.rigidez = rigidez
                    elif opcao == 3:
                            menu = ['Informe a disponibilidade do árbitro:',
                                        '1 - Disponível',
                                        '0 - Indisponível']
                            opcao = self.tela.exibir_menu(menu, range(0,2))
                            arbitro.disponivel = opcao == True
                    else:
                            alterando = False
                            return
                    alterando = self.tela.recebe_int('Realizar outra operação? [1 - Sim / 0 - Não]: ', [0,1])
                except ValueError:
                    self.tela.mostrar_mensagem('»»»» Já existe uma pessoa com esses dados.')
                        
    
    def alterar(self):
        opcoes = {0: self.abre_tela, 1: self.alterar_jogador, 2: self.alterar_tecnico, 3: self.alterar_arbitro}
        menu = ['1 - Alterar jogador', '2 - Alterar técnico', '3 - Alterar árbitro', '0 - Voltar ao menu inicial']
        opcao = self.tela.exibir_menu(menu, range(4))
        opcoes[opcao]()

    
    def listar_jogadores(self, n_entradas = None):
        jogadores = []
        lista = self.__jogadores_registrados
        if n_entradas is None:
            menu = ['1 - Listar todos os jogadores cadastrados', '2 - Listar número determinado de jogadores']
            opcao = self.tela.exibir_menu(menu, range(1,3))
            if opcao == 1:
                for jogador in lista:
                    self.mostrar_informacoes(jogador)
                jogadores.extend(lista)
            elif opcao == 2:
                n_entradas = self.tela.recebe_int('Informe o número de jogadores a serem listados: ')
                for i in range(n_entradas):
                    jogador = self.buscar(lista)
                    if jogador:
                        jogadores.append(jogador)
        if len(jogadores) == 0:
            raise ListaError()
        else:
            return jogadores
    
    
    def listar_tecnicos(self, n_entradas = None):
        tecnicos = []
        lista = self.__tecnicos_registrados
        if n_entradas is None:
            menu = ['1 - Listar todos os técnicos cadastrados', '2 - Listar número determinado de técnicos']
            opcao = self.tela.exibir_menu(menu, range(1,3))
            if opcao == 1:
                for tecnico in lista:
                    self.mostrar_informacoes(tecnico)
                tecnicos.extend(lista)
            elif opcao == 2:
                n_entradas = self.tela.recebe_int('Informe o número de técnicos a serem listados: ')
                for i in range(n_entradas):
                    tecnico = self.buscar(lista)
                    if tecnico:
                        tecnicos.append(tecnico)
        if len(tecnicos) == 0:
                raise ListaError()
        else:
            return tecnicos
                
    
        
    def listar_arbitros(self, n_entradas = None):
        arbitros = []
        lista = self.__arbitros_registrados
        if n_entradas is None:
            menu = ['1 - Listar todos os árbitros cadastrados', '2 - Listar número determinado de árbitros']
            opcao = self.tela.exibir_menu(menu, range(1,3))
            if opcao == 1:
                for arbitro in lista:
                    self.mostrar_informacoes(arbitro)
                arbitros.extend(lista)
            elif opcao == 2:
                n_entradas = self.tela.recebe_int('Informe o número de árbitros a serem listados: ')
                for i in range(n_entradas):
                    arbitro = self.buscar(lista)
                    if arbitro:
                        arbitros.append(arbitro)
        if len(arbitros) == 0:
            raise ListaError()
        else:
            return arbitros


    def listar(self, opcao = None):
        try:
            opcoes = {0: self.abre_tela, 1: self.listar_jogadores, 2: self.listar_tecnicos, 3: self.listar_arbitros}
            if opcao is None:
                menu = ['1 - Listar jogadores', '2 - Listar técnicos','3 - Listar Árbitros', '0 - Voltar ao menu inicial']
                opcao = self.tela.exibir_menu(menu, range(len(opcoes)))
                opcoes[opcao]()
            elif isinstance(opcao, int) and opcao in range(len(opcoes)):
                opcoes[opcao]()
            else:
                raise ValueError
        except ValueError:
            self.tela.mostrar_mensagem('»»»» Somente é possível listar jogadores, técnicos ou árbitros.')
        except ListaError:
            self.tela.mostrar_mensagem('»»»» Não foram informadas pessoas a serem adicionadas.')

        
    def excluir_jogador(self):
        opcoes = {1: self.buscar_nome, 2: self.buscar_id}
        menu = ['1 - Excluir por nome', '2 - Excluir por ID']
        opcao = self.tela.exibir_menu(menu, range(1,3))
        jogador = self.buscar_jogador(opcao)
        if jogador:
            self.__jogadores_registrados.remove(jogador)
            if jogador not in self.__jogadores_registrados:
                self.tela.mostrar_mensagem('Jogador excluído com sucesso.')
            else:
                self.tela.mostrar_mensagem('Não foi possível realizar a exclusão.')
            
    def excluir_tecnico(self):
        opcoes = {1: self.buscar_nome, 2: self.buscar_id}
        menu = ['1 - Excluir por nome', '2 - Excluir por ID']
        opcao = self.tela.exibir_menu(menu, range(1,3))
        tecnico = self.buscar_tecnico(opcao)
        if tecnico:
            self.__tecnicos_registrados.remove(tecnico)
            if tecnico not in self.__tecnicos_registrados:
                self.tela.mostrar_mensagem('Técnico excluído com sucesso.')
            else:
                self.tela.mostrar_mensagem('Não foi possível realizar a exclusão.')
        
    def excluir_arbitro(self):
        opcoes = {1: self.buscar_nome, 2: self.buscar_id}
        menu = ['1 - Excluir por nome', '2 - Excluir por ID']
        opcao = self.tela.exibir_menu(menu, range(1,3))
        arbitro = self.buscar_arbitro(opcao)
        if arbitro:
            self.__arbitros_registrados.remove(arbitro)
            if arbitro not in self.__arbitros_registrados:
                self.tela.mostrar_mensagem('Árbitro excluído com sucesso.')
            else:
                self.tela.mostrar_mensagem('Não foi possível realizar a exclusão.')           
        
    def excluir(self):
        try:
            opcoes = {0: self.abre_tela, 1: self.excluir_jogador, 2: self.excluir_tecnico, 3: self.excluir_arbitro}
            menu = ['1 - Excluir jogador', '2 - Excluir técnico','3 - Excluir árbitro', '0 - Voltar ao menu inicial']
            opcao = self.tela.exibir_menu(menu, range(len(opcoes)))
            opcoes[opcao]()
        except Exception:
            self.tela.mostrar_mensagem('»»»» Somente é possível excluir jogadores, técnicos ou árbitros.')
        
    def mostrar_informacoes(self, pessoa):
            self.tela.mostrar_mensagem('')
            self.tela.mostrar_mensagem('>: ')
            self.tela.mostrar_mensagem(pessoa)
    
    def abre_tela(self):
        tela = True
        while tela:
            opcoes = {1: self.cadastrar, 2: self.buscar_pessoas, 3: self.alterar, 4: self.listar,
                      5: self.excluir}
            menu = ['1 - Cadastrar pessoa', '2 - Buscar pessoa', '3 - Alterar pessoa',
                    '4 - Listar pessoa', '5 - Excluir pessoa', '0 - Sair']
            opcao = self.tela.exibir_menu(menu, range(6))
            if opcao != 0:
                opcoes[opcao]()
            else:
                tela = False

