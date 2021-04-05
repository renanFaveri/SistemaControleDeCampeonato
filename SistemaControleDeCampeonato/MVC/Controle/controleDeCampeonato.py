from MVC.entidade.campeonato import Campeonato 
from .controleDeEntidade import ControladorDeEntidade
from MVC.limite.tela import Tela
from MVC.limite.telaDeCampeonato import TelaDeCampeonatos



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
    def campeonatos_registrados(self):
        return self.__campeonatos_registrados
            
            
    def buscar_nome(self, nome = None):
        if nome is None:
            nome = self.tela.recebe_str('Procurar por nome do campeonato: ')
        for obj in self.__campeonatos_registrados:
            if obj.nome.lower() == nome.lower():
                self.mostrar_informacoes(obj)
                return obj
   

    def buscar_id(self):
        id_ = self.tela.recebe_int('Procurar por ID: ')
        contador = 0
        while contador < len(self.__campeonatos_registrados):
            if id_ == self.__campeonatos_registrados[contador].id_:
                self.mostrar_informacoes(self.__campeonatos_registrados[contador])
                return self.__campeonatos_registrados[contador]
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
            buscando = self.tela.recebe_int('Procurar outro campeonato? [1 - Sim / 0 - Não]: ', [0,1])         
            
            
    def verificacao(self, campeonato: Campeonato):
        if isinstance(campeonato, Campeonato):
            contador = 0
            while contador < len(self.__campeonatos_registrados):
                if campeonato.nome == self.__campeonatos_registrados[contador].nome and\
                            campeonato.n_times == self.__campeonatos_registrados[contador].n_times:
                    raise ValueError
                else:
                    contador += 1
        else:
            raise TypeError   
        
        
    def cadastrar(self):
        cadastrando = True
        while cadastrando:
            nome_campeonato = self.tela.recebe_str('Informe o nome do campeonato: ', 3)
            n_times = self.tela.recebe_str('Informe o número de times que disputará o campeonato: ')

            ################        adicionar calendário           ################

            campeonato = Campeonato(nome_campeonato, n_times)
            try:
                self.verificacao(campeonato)
                self.__campeonatos_registrados.append(campeonato)
                self.mostrar_informacoes(campeonato)
            except ValueError:
                self.tela.mostrar_mensagem('»»»» Já existe um campeonato com esses dados.')
            except TypeError:
                self.tela.mostrar_mensagem('»»»» Somente um campeonato pode ser cadastrado.')
            cadastrando = self.tela.recebe_int('Realizar nova operação? [1 - Sim / 0 - Não]: ', [0,1])

        
#     def adicionar(self, campeonato: Campeonato, controlador_times = self.__controlador_master.ct):
#         if isinstance(campeonato, Campeonato) and isinstance(controlador_times, ControladorDeTimes):
#             adicionando = True
#             while adicionando:
#                 try:
#                     times = controlador_times.listar()
#                     campeonato.adicionar_times(times)
#                     self.tela.mostrar_mensagem(f'{len(times)} time(s) adicionado(s) ao campeonato {campeonato.nome}!')
#                 except TypeError:
#                     self.tela.mostrar_mensagem('»»»» Somente é possível adicionar times ao campeonato!')
#                 except ValueError:
#                     self.tela.mostrar_mensagem('»»»» O número de times informado excede o limite do campeonato!')
#         else:
#             raise TypeError

 
    def alterar(self):
        self.tela.exibir_mensagem('Escolha o cadastro de campeonato a ser alterado.')
        campeonato = self.buscar()
        if campeonato is not None:
            alterando = True
            while alterando:
                try:
                    menu = ['Informe os atributos a serem alterados:',
                            '1 - Nome',
                            '2 - Número de times competidores',
                            '3 - Times competidores',
                            '4 - Calendário',
                            '0 - Sair']
                    opcao = self.tela.exibir_menu(menu, range(5))
                    if opcao == 1:
                            nome_campeonato = self.tela.recebe_str('Informe o novo nome do campeonato: ', 3)
                            contador = 0
                            while contador < len(self.__campeonatos_registrados):
                                if nome_campeonato ==  self.__campeonatos_registrados[contador].nome and\
                                            campeonato.times == self.__campeonatos_registrados[contador].times and\
                                            campeonato.n_times == self.__campeonatos_registrados[contador].n_times:
                                    raise ValueError
                                else:
                                    contador += 1
                            campeonato.nome = nome_campeonato
                    elif opcao == 2:
                            n_times = self.tela.recebe_int('Informe o número de times que disputará o campeonato: ')
                            contador = 0
                            while contador < len(self.__campeonatos_registrados):
                                if nome_campeonato ==  self.__campeonatos_registrados[contador].nome and\
                                            campeonato.times == self.__campeonatos_registrados[contador].times and\
                                            campeonato.n_times == self.__campeonatos_registrados[contador].n_times:
                                    raise ValueError
                                else:
                                    contador += 1
                            campeonato.n_times = n_times
                    elif opcao == 3:
                            menu = ['1 - Adicionar time',
                                    '2 - Remover time',
                                    '0 - Voltar ao menu inicial']
                            opcao = self.tela.exibir_menu(menu, range(3))
                            if opcao == 2:
                                self.tela.mostrar_mensagem('Informe os times a serem removidos.')
                                times = self.__controlador_master.ct.listar()
                                try:
                                    campeonato.remover_times(times)
                                except TypeError:
                                    self.tela.mostrar_mensagem('»»»» Somente é possível remover times.')
                                except ValueError:
                                    self.tela.mostrar_mensagem('»»»» Impossível remover times não cadastrados no campeonato.')
                                except ListaError:
                                    self.tela.mostrar_mensagem('»»»» Não foram informados times a serem removidos.')
                            elif opcao == 1:
                                self.tela.mostrar_mensagem('Informe os times a serem adicionados.')
                                times = self.__controlador_master.ct.listar()
                                try:
                                    campeonato.adicionar_times(times)
                                except TypeError:
                                    self.tela.mostrar_mensagem('»»»» Somente é possível adicionar times.')
                                except ValueError:
                                    self.tela.mostrar_mensagem('»»»» Impossível adicionar times não cadastrados.')
                                except ListaError:
                                    self.tela.mostrar_mensagem('»»»» Não foram informados times a serem adicionados.')
                            else:
                                alterando = False
                                self.alterar() 
                    else:
                            alterando = False
                            return
                    alterando = self.tela.recebe_int('Realizar outra alteração? [1 - Sim / 0 - Não]: ', [0,1])
                except ValueError:
                    self.tela.mostrar_mensagem('»»»» Já existe um campeonato com esses dados.')
                    
                  

    def listar(self, n_entradas = None):
        campeonatos = []
        if n_entradas is None:
            menu = ['1 - Buscar todos os campeonatos cadastrados', '2 - Buscar campeonatos individualmente']
            opcao = self.tela.exibir_menu(menu, range(1,3))
            if opcao == 1:
                n_entradas = len(self.__campeonatos_registrados)
            elif opcao == 2:
                n_entradas = self.tela.recebe_int('Informe o número de campeonatos a serem listados: ')
        for i in range(n_entradas):
            campeonato = self.buscar()
            campeonatos.append(campeonato)
        return campeonatos
    
    
    def mostrar_informacoes(self, campeonato):
        self.tela.mostrar_mensagem('')
        self.tela.mostrar_mensagem('Resultado:')
        self.tela.mostrar_mensagem(campeonato)
  

    def excluir(self):
        campeonato = self.buscar()
        self.__campeonatos_registrados.remove(campeonato)
        if campeonato not in self.__campeonatos_registrados:
            self.tela.mostrar_mensagem('Campeonato excluído com sucesso.')
        else:
            self.tela.mostrar_mensagem('Não foi possível realizar a exclusão.')
        
        
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
                self.tela.mostrar_mensagem('»»»» Somente campeonatos podem executar essa ação!')
                
    
