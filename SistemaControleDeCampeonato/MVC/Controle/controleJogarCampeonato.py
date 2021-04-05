import random
from MVC.exceptionTime import TimeIncompletoError
from MVC.exceptionVazia import EntradaVaziaError
from MVC.limite.telaDePartidas import TelaDePartidas
from .controleDeCampeonato import ControladorDeCampeonatos
from MVC.entidade.time import Time
from MVC.entidade.arbitro import Arbitro
from MVC.entidade.partida import Partida
from MVC.entidade.goleiro import Goleiro
from MVC.limite.tela import Tela

class JogarCampeonato:

    def __init__(self, controlador_master):
        self.__controlador_master = controlador_master
        self.__tela = TelaDePartidas(self)
        self.__p = []
    
    @property
    def cm(self):
        return self.__controlador_master
    
    @property
    def tela(self):
        return self.__tela
    
    
    def criar_partida(self, time_anfitriao = None, time_visitante = None, arbitro_designado = None,
                      data_do_jogo = None):
        try:
            if not (time_anfitriao and time_visitante and arbitro_designado):
                self.tela.mostrar_mensagem('Informe o time anfitrião.')
                time_anfitriao = self.cm.ct.buscar()
                self.tela.mostrar_mensagem('Informe o time visitante.')
                time_visitante = self.cm.ct.buscar()
                self.tela.mostrar_mensagem('Informe o árbitro da partida.')
                arbitro_designado = self.cm.cp.buscar(self.cm.cp.arbitros_registrados)
            if isinstance(time_anfitriao, Time) and isinstance(time_visitante, Time) and (arbitro_designado, Arbitro):
                if (len(time_anfitriao.jogadores) < time_anfitriao.min_jogadores) and                        (len(time_visitante.jogadores) < time_visitante.min_jogadores):
                    raise TimeIncompletoError
                else:
                    partida = Partida(time_anfitriao, time_visitante, arbitro_designado)
                    self.__p.append(partida)
            else:
                raise EntradaVaziaError
            return partida
        except EntradaVaziaError:
            self.tela.mostrar_mensagem('»»»» A partida deve ser composta obrigatoriamente por 2 times e 1 árbitro.')
        except TimeIncompletoError:
            self.tela.mostrar_mensagem('»»»» A partida deve ser composta obrigatoriamente por 2 times e 1 árbitro.')
    
    
    def criar_partidas(self, lista_de_times_do_campeonato):
        partidas = []
        arbitros = self.cm.cp.arbitros_registrados
        for time1 in lista_de_times_do_campeonato:
            for time2 in lista_de_times_do_campeonato:
                if isinstance(time1, Time) and isinstance(time2, Time) and time1 is not time2:
                    i = random.randrange(len(arbitros))
                    arbitro = arbitros[i]
                    partida = self.criar_partida(time1, time2, arbitro)
        return partidas
    
    
    def sort_gols(self, max_gols = 5):
        gols = []
        for i in range(max_gols):
            gol = random.randint(0,1)
            gols.append(gol)
        return sum(gols)
    
    
    def sort_temp_gols(self, qt_gols, temp = 90):
        tempo = []
        tgol = None
        for i in range(qt_gols):
            tgol = random.randrange(1, temp)
            while tgol in tempo:
                tgol = random.randrange(1, temp)
            tempo.append(tgol)
            tempo.sort()
        return tempo
    
    def sort_jog_marc(self, time, gols):
        lj = []
        while len(lj) < gols:
            j = random.randrange(len(time.jogadores))
            jg = time.jogadores[j]
            if jg.posicao.posicao is not Goleiro().posicao:
                lj.append(jg)
        return lj
            
    def sort_jog_tempo(self, lja, ljv, ltemp_gols):
        j_t = []
        marcadores = []
        l = lja + ljv
        lidx = []
        while len(marcadores) < len(ltemp_gols):
            idx = random.randrange(len(l))
            if idx not in lidx:
                marcadores.append(l[idx])
                lidx.append(idx)
        for i in range(len(ltemp_gols)):
            j_t.append((marcadores[i], ltemp_gols[i]))
        return j_t              
    
    def atl_gols_time(self, time, gols_p, gols_c):
        time.gols_marcados = gols_p
        time.gols_sofridos = gols_c
        
        
    def atl_jogadores(self, jogadores):
        for j in jogadores:
            j.gols_marcados += 1
            
    def atl_goleiro(self, time, gols_sofridos):
        i = 0
        while i < len(time.jogadores):
            if time.jogadores[i].posicao.posicao == Goleiro().posicao:
                time.jogadores[i].gols_concedidos += gols_sofridos
                return
            else:
                i += 1
                
    def atl_time(self, time, gols_p, gols_c):
        if gols_p > gols_c:
            time.vitorias += 1
        elif gols_p < gols_c:
            time.derrotas += 1
        else:
            time.empates += 1
        time.gols_marcados += gols_p
        time.gols_sofridos += gols_c
        
    
    def jogar_partida(self, partida: Partida):
        ta = partida.time_anfitriao
        tv = partida.time_visitante
        gols_a = self.sort_gols()
        gols_v = self.sort_gols()
        self.atl_gols_time(ta, gols_a, gols_v)
        self.atl_gols_time(tv, gols_v, gols_a)
        placar = f'{gols_a} x {gols_v}'
        partida.placar = placar
        marc_a = self.sort_jog_marc(ta, gols_a)
        marc_v = self.sort_jog_marc(tv, gols_v)
        self.atl_goleiro(ta, gols_v)
        self.atl_goleiro(tv, gols_a)
        self.atl_time(ta, gols_a, gols_v)
        self.atl_time(tv, gols_v, gols_a)
        tt_gols = gols_a + gols_v
        rel_jog_gol = self.sort_jog_tempo(marc_a, marc_v, self.sort_temp_gols(tt_gols))
        rel_partida = [(partida.id_),(ta, gols_a, marc_a),(tv, gols_v, marc_v)]
        partida.relatorio = rel_partida
        partida.gerar_sumula(rel_jog_gol)
        self.tela.mostrar_tela_partida(partida.sumula)
        partida.jogada = True        
                  
            
    def teste(self):
        for p in self.__p:
            if not p.jogada:
                return self.jogar_partida(p)
        
            
    def abre_tela(self):
        tela = True
        while tela:
            opcoes = {1: self.criar_partida, 2: self.criar_partidas, 3: self.jogar_partida, 4: self.teste}
            menu = ['1 - Criar partida', '2 - Criar partidas', '3 - Jogar partida', '4 - teste', '0 - Sair']
            opcao = self.tela.exibir_menu(menu, range(5))
            if opcao != 0:
                opcoes[opcao]()
            else:
                tela = False
