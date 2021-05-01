from MVC.entidade.campeonato import Campeonato 
from .controleDeEntidade import ControladorDeEntidade
from MVC.limite.tela import Tela
from MVC.limite.telaDeCampeonato import TelaDeCampeonatos
from MVC.entidade.time import Time
from MVC.exceptionLista import ListaError


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
            nome = self.tela.recebe_str('Procurar campeonato por nome: ')
        for obj in self.__campeonatos_registrados:
            if obj.nome.lower() == nome.lower():
                self.mostrar_informacoes(obj)
                return obj
   

    def buscar_id(self):
        id_ = self.tela.recebe_int('Procurar campeonato por ID: ')
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
            menu = ['1 - Buscar campeonato por nome', '2 - Buscar campeonato por ID', '0 - Voltar ao menu inicial']
            opcao = self.tela.exibir_menu(menu, range(3))
            if opcao == 0:
                buscando = False
            else:
                resultado = opcoes[opcao]()
                if resultado is None:
                    self.tela.mostrar_mensagem('Não há campeonato cadastrado com esses dados.')
                    buscando = self.tela.recebe_int('Procurar outro campeonato? [1 - Sim / 0 - Não]: ', [0,1])
                else:
                    return resultado        
            
            
    def verificacao(self, campeonato: Campeonato):
        if isinstance(campeonato, Campeonato):
            contador = 0
            while contador < len(self.__campeonatos_registrados):
                if campeonato.nome == self.__campeonatos_registrados[contador].nome and campeonato.n_times == self.__campeonatos_registrados[contador].n_times:
                    raise ValueError
                else:
                    contador += 1
        else:
            raise TypeError   
        
        
    def cadastrar(self):
        nome_campeonato = self.tela.recebe_str('Informe o nome do novo campeonato: ', 3)
        n_times = self.tela.recebe_int('Informe o número de times que disputará o campeonato: ')
        try:
            campeonato = Campeonato(nome_campeonato, n_times)  
        except TypeError:
            self.tela.mostrar_mensagem('»»»» Dados inválidos.')
        try:                
            self.verificacao(campeonato)
            self.__campeonatos_registrados.append(campeonato)
            self.mostrar_informacoes(campeonato)
        except ValueError:
            self.tela.mostrar_mensagem('»»»» Já existe um campeonato com esses dados.')
        except TypeError:
            self.tela.mostrar_mensagem('»»»» Somente um campeonato pode ser cadastrado.')
            

 
    def alterar(self):
        self.tela.mostrar_mensagem('Escolha o cadastro de campeonato a ser alterado.')
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
                                if nome_campeonato ==  self.__campeonatos_registrados[contador].nome and campeonato.times == self.__campeonatos_registrados[contador].times and campeonato.n_times == self.__campeonatos_registrados[contador].n_times:
                                    raise ValueError
                                else:
                                    contador += 1
                            campeonato.nome = nome_campeonato
                    elif opcao == 2:
                            n_times = self.tela.recebe_int('Informe o número de times que disputará o campeonato: ')
                            contador = 0
                            while contador < len(self.__campeonatos_registrados):
                                if nome_campeonato ==  self.__campeonatos_registrados[contador].nome and campeonato.times == self.__campeonatos_registrados[contador].times and campeonato.n_times == self.__campeonatos_registrados[contador].n_times:
                                    raise ValueError
                                else:
                                    contador += 1
                            campeonato.n_times = n_times
                    elif opcao == 3:
                            menu = ['1 - Adicionar time',
                                    '2 - Remover time',
                                    '0 - Voltar ao menu inicial']
                            opcao = self.tela.exibir_menu(menu, range(3))
                            if opcao == 1:
                                self.tela.mostrar_mensagem('Informe os times a serem adicionados.')
                                try:
                                    times = self.__controlador_master.ct.listar()                                
                                    campeonato.adicionar_times(times)
                                except TypeError:
                                    self.tela.mostrar_mensagem('»»»» Somente é possível adicionar times.')
                                except ValueError:
                                    self.tela.mostrar_mensagem('»»»» Impossível adicionar times não cadastrados.')
                                except ListaError:
                                    self.tela.mostrar_mensagem('»»»» Não foram informados times a serem adicionados.')
                            elif opcao == 2:
                                self.tela.mostrar_mensagem('Informe os times a serem removidos.')
                                try:
                                    times = self.__controlador_master.ct.listar()
                                    campeonato.remover_times(times)
                                except TypeError:
                                    self.tela.mostrar_mensagem('»»»» Somente é possível remover times.')
                                except ValueError:
                                    self.tela.mostrar_mensagem('»»»» Impossível remover times não cadastrados no campeonato.')
                                except ListaError:
                                    self.tela.mostrar_mensagem('»»»» Não foram informados times a serem removidos.')                            
                            else:
                                alterando = False
                    else:
                            alterando = False
                            return
                    alterando = self.tela.recebe_int('Realizar outra operação? [1 - Sim / 0 - Não]: ', [0,1])
                except ValueError:
                    self.tela.mostrar_mensagem('»»»» Já existe um campeonato com esses dados.')


    def listar(self, n_entradas = None):
        campeonatos = []
        lista = self.__campeonatos_registrados
        if n_entradas is None:
            menu = ['1 - Listar todos os campeonatos cadastrados', '2 - Listar número determinado de campeonatos']
            opcao = self.tela.exibir_menu(menu, range(1,3))
            if opcao == 1:
                for campeonato in lista:
                    self.mostrar_informacoes(campeonato)
                campeonatos.extend(lista)
            elif opcao == 2:
                n_entradas = self.tela.recebe_int('Informe o número de campeonatos a serem listados: ')
                for i in range(n_entradas):
                    campeonato = self.buscar()
                    if campeonato:
                        campeonatos.append(campeonato)
        if len(campeonatos) == 0:
            raise ListaError()
        else:
            return campeonatos

    

    def mostrar_informacoes(self, campeonato):
        self.tela.mostrar_mensagem('')
        self.tela.mostrar_mensagem('> ')
        self.tela.mostrar_mensagem(campeonato)   
        

    def excluir(self):
        campeonato = self.buscar()
        if campeonato:
            self.__campeonatos_registrados.remove(campeonato)
            if campeonato not in self.__campeonatos_registrados:
                self.tela.mostrar_mensagem('Campeonato excluído com sucesso.')
            else:
                self.tela.mostrar_mensagem('Não foi possível realizar a exclusão.')
        
        
    def abre_tela(self):
        tela = True
        while tela:
            try:
                opcoes = {1: self.cadastrar, 2: self.buscar, 3: self.alterar, 4: self.listar, 5: self.excluir}
                menu = ['1 - Cadastrar campeonato', '2 - Buscar campeonato', '3 - Alterar campeonato',
                        '4 - Listar campeonato', '5 - Excluir campeonato', '0 - Sair']
                opcao = self.tela.exibir_menu(menu, range(6))
                if opcao != 0:
                    opcoes[opcao]()
                else:
                    tela = False
            except TypeError:
                self.tela.mostrar_mensagem('»»»» Somente campeonatos podem executar essa ação!')
                
        