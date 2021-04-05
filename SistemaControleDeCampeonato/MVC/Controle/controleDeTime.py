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
        self.__times_registrados = []
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
            nome = self.tela.recebe_str('Procurar time por nome: ')
        for obj in self.times_registrados:
            if obj.nome.lower() == nome.lower():
                self.mostrar_informacoes(obj)
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
        opcoes = {1: self.buscar_nome, 2: self.buscar_id}
        while buscando:
            menu = ['1 - Buscar time por nome', '2 - Buscar time por ID', '0 - Voltar ao menu inicial']
            opcao = self.tela.exibir_menu(menu, range(3))
            if opcao == 0:
                buscando = False
            else:
                resultado = opcoes[opcao]()
                if resultado is None:
                    self.tela.mostrar_mensagem('Não há time cadastrado com esses dados.')
                    buscando = self.tela.recebe_int('Procurar outro time? [1 - Sim / 0 - Não]: ', [0,1])
                else:
                    return resultado
            
    def cadastrar(self):
        cadastrando = True
        while cadastrando:
            try:
                nome_time = self.tela.recebe_str('Informe o nome do time: ', 3)
                time = Time(nome_time)
                if self.buscar_nome(nome_time):
                    raise ValueError
                else:
                    self.__times_registrados.append(time)
                    self.mostrar_informacoes(time)
            except ValueError:
                self.tela.mostrar_mensagem('»»»» Já existe um time com esses dados.')
            except TypeError:
                self.tela.mostrar_mensagem('»»»» Dados inválidos.')
            cadastrando = self.tela.recebe_int('Realizar nova operação? [1 - Sim / 0 - Não]: ', [0,1])
  
    def alterar(self):
        self.tela.mostrar_mensagem('Escolha o cadastro de time a ser alterado.')
        time = self.buscar()
        if time is not None:
            alterando = True
            while alterando:
                try:
                    menu = ['Informe os atributos a serem alterados:', '1 - Nome', '2 - Técnico', '3 - Jogadores', '0 - Sair']
                    opcao = self.tela.exibir_menu(menu, range(4))
                    if opcao == 1:
                        nome_time = self.tela.recebe_str('Informe o novo nome do time: ', 3)
                        if self.buscar_nome(nome_time):
                            raise ValueError
                        else:
                            time.nome = nome_time                          
                    elif opcao == 2:
                        menu = ['1 - Contratar técnico',
                                '2 - Demitir técnico',
                                '0 - Voltar ao menu inicial']
                        opcao = self.tela.exibir_menu(menu, range(3))
                        if opcao == 1:
                            try:
                                tecnico = self.cm.cp.buscar(self.cm.cp.tecnicos_registrados)
                                if tecnico:
                                    if tecnico.disponivel:
                                        time.tecnico = tecnico
                                        tecnico.time = time
                                        tecnico.disponivel = False
                                        self.tela.mostrar_mensagem('»»»» Técnico contratado!')
                                    else:
                                        raise ValueError
                                else:
                                    self.tela.mostrar_mensagem('»»»» Não foram encontrados técnicos com esses dados.')
                            except ValueError:
                                self.tela.mostrar_mensagem('»»»» Técnico indisponível.')
                        elif opcao == 2:
                            menu = ['Confirmar demissão do técnico?  [1 - Sim / 0 - Não]']
                            opcao = self.tela.exibir_menu(menu, range(2))
                            if opcao:
                                time.tecnico.disponivel = True
                                time.tecnico.time = None
                                time.tecnico = None
                                self.tela.mostrar_mensagem('Técnico demitido.')
                            else:
                                alterando = False
                        else:
                            alterando = False
                    elif opcao == 3:
                        menu = ['1 - Contratar jogadores','2 - Dispensar jogadores', '0 - Voltar ao menu inicial']
                        opcao = self.tela.exibir_menu(menu, range(3))
                        if opcao == 1:
                            self.tela.mostrar_mensagem('Informe os jogadores a serem contratados.')
                            jogadores = self.cm.cp.listar_jogadores()
                            try:
                                for jogador in jogadores:
                                    if not jogador.disponivel:
                                        raise ValueError
                                if time.adicionar_jogadores(jogadores):
                                    self.tela.mostrar_mensagem('Jogadores contratados!')
                            except TypeError:
                                self.tela.mostrar_mensagem('»»»» Somente é possível contratar jogadores.')
                            except ValueError:
                                self.tela.mostrar_mensagem('»»»» Impossível contratar jogadores não registrados.')
                            except ListaError:
                                self.tela.mostrar_mensagem('»»»» Não foram informados jogadores a serem contratados.')
                        elif opcao == 2:
                            self.tela.mostrar_mensagem('Informe os jogadores a serem dispensados.')
                            jogadores = self.cm.cp.listar_jogadores()
                            try:
                                if time.remover_jogadores(jogadores):
                                    self.tela.mostrar_mensagem('Jogadores dispensados!')
                            except TypeError:
                                self.tela.mostrar_mensagem('»»»» Somente é possível remover jogadores.')
                            except ValueError:
                                self.tela.mostrar_mensagem('»»»» Impossível remover jogadores não contratados pelo time.')
                            except ListaError:
                                self.tela.mostrar_mensagem('»»»» Não foram informados jogadores a serem adicionados.')
                        else:
                            alterando = False
                    else:
                        return
                    alterando = self.tela.recebe_int('Realizar outra operação? [1 - Sim / 0 - Não]: ', [0,1])
                except ValueError:
                    self.tela.mostrar_mensagem('»»»» Já existe um time com esses dados.')

    def listar(self, n_entradas = None):
        times = []
        lista = self.times_registrados
        if n_entradas is None:
            menu = ['1 - Listar todos os times cadastrados', '2 - Listar número determinado de times']
            opcao = self.tela.exibir_menu(menu, range(1,3))
            if opcao == 1:
                n_entradas = len(lista)

                for time in lista:
                    self.mostrar_informacoes(time)
                times.extend(lista)
            elif opcao == 2:
                n_entradas = self.tela.recebe_int('Informe o número de times a serem listados: ')
                for i in range(n_entradas):
                    time = self.buscar()
                    if time:
                        times.append(time)
        if len(times) == 0:
            raise ListaError()
        else:
            return times
     
    def excluir(self):
        time = self.buscar()
        if time:
            self.__times_registrados.remove(time)
            if time not in self.__times_registrados:
                self.tela.mostrar_mensagem('Time excluído com sucesso.')
            else:
                self.tela.mostrar_mensagem('Não foi possível realizar a exclusão.')
            
    
    def mostrar_informacoes(self, time):
        self.tela.mostrar_mensagem('')
        self.tela.mostrar_mensagem('> ')
        self.tela.mostrar_mensagem(time)
        
    def abre_tela(self):
        tela = True
        while tela:
            opcoes = {1: self.cadastrar, 2: self.buscar, 3: self.alterar, 4: self.listar, 5: self.excluir}
            menu = ['1 - Cadastrar time', '2 - Buscar time', '3 - Alterar time', '4 - Listar time',
                    '5 - Excluir time', '0 - Sair']
            opcao = self.tela.exibir_menu(menu, range(6))
            if opcao != 0:
                opcoes[opcao]()
            else:
                tela = False
       

