from .controleDeEntidade import ControladorDeEntidade
from MVC.entidade.time import Time
from MVC.exceptionLista import ListaError
from MVC.limite.telaDeTime import TelaDeTimes
from MVC.limite.tela import Tela

class ControladorDeTimes(ControladorDeEntidade):
        
    def __init__(self, controlador_master):
        self.__controlador_master = controlador_master
        self.__times_registrados = []
        self.__tela = TelaDeTimes(self)

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
            nome = self.tela.recebe_str('Procurar por nome do time: ')
        for obj in self.times_registrados:
            if obj.nome.lower() == nome.lower():
                self.mostrar_informacoes(obj)
                return obj

    def buscar_id(self):
        id_ = self.tela.recebe_int('Procurar por ID: ')
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
                return
            else:
                opcoes[opcao]()
            buscando = self.tela.recebe_int('Procurar outro time? [1 - Sim / 0 - Não]: ', [0,1])   

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
            except ValueError:
                self.tela.mostrar_mensagem('»»»» Já existe um time com esses dados.')
            cadastrando = self.tela.recebe_int('Realizar nova operação? [1 - Sim / 0 - Não]: ', [0,1])
                         
#     def adicionar_jogador(self, time: Time, controlador_jogadores = self.__controlador_master.cp):
#         if isinstance(time, Time) and isinstance(controlador_jogadores, ControladorDePessoas):
#             adicionando = True
#             while adicionando:
#                 try:
#                     jogador = controlador_jogadores.listar()
#                     campeonato.adicionar_times(times)
#                     self.tela.mostrar_mensagem(f'{len(times)} time(s) adicionado(s) ao campeonato {campeonato.nome}!')
#                 except TypeError:
#                     self.tela.mostrar_mensagem('»»»» Somente é possível adicionar times ao campeonato!')
#                 except ValueError:
#                     self.tela.mostrar_mensagem('»»»» O número de times informado excede o limite do campeonato!')
#         else:
#             raise TypeError
                                
    def alterar(self):
        self.tela.exibir_mensagem('Escolha o cadastro de time a ser alterado.')
        time = self.buscar()
        if time is not None:
            alterando = True
            while alterando:
                try:
                    menu = ['Informe os atributos a serem alterados:',
                            '1 - Nome',                            
                            '2 - Técnico',
                            '3 - Jogadores',
                            '0 - Sair']
                    opcao = self.tela.exibir_menu(menu, range(4))
                    if opcao == 1:
                            nome_time = self.tela.recebe_str('Informe o novo nome do time: ', 3)
                            contador = 0
                            while contador < len(self.__times_registrados):
                                if nome_time ==  self.__times_registrados[contador].nome:
                                    raise ValueError
                                else:
                                    contador += 1
                            time.nome = nome_time
                    elif opcao == 2:
                            menu = ['1 - Contratar técnico',
                                    '2 - Demitir técnico',
                                    '0 - Voltar ao menu inicial']
                            opcao = self.tela.exibir_menu(menu, range(3))
                            if opcao == 1:
                                try:
                                    tecnico = self.__controlador_master.cp.buscar(self.__controlador_master.cp.tecnicos_registrados)
                                    if tecnico.disponivel:
                                        time.tecnico = tecnico
                                    else:
                                        raise ValueError
                                except ValueError:
                                    self.tela.mostrar_mensagem('»»»» Técnico indisponível.')
                            elif opcao == 2:
                                time.tecnico.disponivel = True
                                time.tecnico = None  
                                self.tela.mostrar_mensagem('Técnico demitido.')
                            else:
                                alterando = False
                                self.alterar()                                  
                    elif opcao == 3:
                            menu = ['1 - Contratar jogadores',
                                    '2 - Dispensar jogadores',
                                    '0 - Voltar ao menu inicial']
                            if opcao == 1:
                                self.tela.mostrar_mensagem('Informe os jogadores a serem contratados.')
                                jogadores = self.__controlador_master.cp.listar_jogadores()
                                try:
                                    for jogador in jogadores:
                                        if not jogador.disponivel:
                                            raise ValueError
                                    time.adicionar_jogadore(jogadores)
                                except TypeError:
                                    self.tela.mostrar_mensagem('»»»» Somente é possível contratar jogadores.')
                                except ValueError:
                                    self.tela.mostrar_mensagem('»»»» Impossível contratar jogadores não registrados.')
                                except ListaError:
                                    self.tela.mostrar_mensagem('»»»» Não foram informados jogadores a serem contratados.')
                            elif opcao == 2:
                                self.tela.mostrar_mensagem('Informe os jogadores a serem dispensados.')
                                jogadores = self.__controlador_master.cp.listar_jogadores()
                                try:
                                    time.remover_jogadores(jogadores)
                                except TypeError:
                                    self.tela.mostrar_mensagem('»»»» Somente é possível remover jogadores.')
                                except ValueError:
                                    self.tela.mostrar_mensagem('»»»» Impossível remover jogadores não contratados pelo time.')
                                except ListaError:
                                    self.tela.mostrar_mensagem('»»»» Não foram informados jogadores a serem adicionados.')
                            else:
                                alterando = False
                                self.alterar()                              
                    else:
                            alterando = False
                            self.alterar() 
                    alterando = self.tela.recebe_int('Realizar outra alteração? [1 - Sim / 0 - Não]: ', [0,1])
                except ValueError:
                    self.tela.mostrar_mensagem('»»»» Já existe um time com esses dados.')

    def listar(self, n_entradas = None):
        times = []
        if n_entradas is None:
            menu = ['1 - Buscar todos os times cadastrados', '2 - Buscar times individualmente']
            opcao = self.tela.exibir_menu(menu, range(1,3))
            if opcao == 1:
                n_entradas = len(self.times_registrados)
            elif opcao == 2:
                n_entradas = self.tela.recebe_int('Informe o número de times a serem listados: ')
        for i in range(n_entradas):
            time = self.buscar()
            times.append(time)
        return times
 
    def excluir(self):
        time = self.buscar()
        self.__times_registrados.remove(time)
        if time not in self.__times_registrados:
            self.tela.mostrar_mensagem('Time excluído com sucesso.')
        else:
            self.tela.mostrar_mensagem('Não foi possível realizar a exclusão.')
             
    def mostrar_informacoes(self, time):
        self.tela.mostrar_mensagem('')
        self.tela.mostrar_mensagem('Resultado:')
        self.tela.mostrar_mensagem(time)
        
    def abre_tela(self):
        while True:
            try:
                opcoes = {1: self.cadastrar, 2: self.buscar, 3: self.alterar, 4: self.listar, 5: self.excluir}
                menu = ['1 - Cadastrar', '2 - Buscar', '3 - Alterar', '4 - Listar', '5 - Excluir', '0 - Sair']
                opcao = self.tela.exibir_menu(menu, range(6))
                if opcao != 0:
                    opcoes[opcao]()
                else:
                    return
            except TypeError:
                self.tela.mostrar_mensagem('»»»» Somente times podem executar essa ação!')

