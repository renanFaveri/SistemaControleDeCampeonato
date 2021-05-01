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
        self.__p = [Partida(self.__controlador_master.ct.times_registrados[0], self.__controlador_master.ct.times_registrados[1], self.__controlador_master.cp.arbitros_registrados[0])]
    
    @property
    def cm(self):
        return self.__controlador_master
    
    @property
    def tela(self):
        return self.__tela

    @property
    def partidas(self):
        return self.__p
    
    
    def jogar_amistoso(self, time_anfitriao = None, time_visitante = None, arbitro_designado = None,
                      data_do_jogo = None):
        while True:
            if not (time_anfitriao and time_visitante and arbitro_designado):
                self.tela.menu_criar_partida()
                botao, valores = self.tela.abreTela()
                if botao == 'Confirmar':
                    time_anfitriao = self.tela.selecionar_entradas((valores['in_anf'], valores['lst_anf']))
                    if time_anfitriao != None:
                        time_anfitriao = self.cm.ct.buscar_nome(time_anfitriao)
                    time_visitante = self.tela.selecionar_entradas((valores['in_vis'], valores['lst_vis']))
                    if time_visitante != None:
                        time_visitante = self.cm.ct.buscar_nome(time_visitante)                    
                    arbitro_designado = self.tela.selecionar_entradas((valores['in_arb'], valores['lst_arb']))
                    if arbitro_designado != None:
                        arbitro_designado = self.cm.cp.buscar_nome(nome=arbitro_designado, lista=self.cm.cp.arbitros_registrados)
                else:
                    self.tela.fechaTela()
                    break
            try:        
                if isinstance(time_anfitriao, Time) and isinstance(time_visitante, Time) and isinstance(arbitro_designado, Arbitro) and (time_anfitriao != time_visitante):
                    if (len(time_anfitriao.jogadores) < time_anfitriao.min_jogadores) and (len(time_visitante.jogadores) < time_visitante.min_jogadores):
                        raise TimeIncompletoError()
                    else:
                        partida = Partida(time_anfitriao, time_visitante, arbitro_designado)
                        botao = self.tela.popup_confirmacao_partida(partida)
                        if botao == 'Confirmar':
                            self.__p.append(partida)      
                            self.tela.fechaTela()
                            return self.jogar(partida)
                        else:
                            self.tela.fechaTela()
                            return self.jogar_amistoso()
                else:
                    raise EntradaVaziaError()
                
            except EntradaVaziaError:
                self.tela.popup_msg_erro_partida()
                self.tela.fechaTela()
                return self.jogar_amistoso()
            except TimeIncompletoError:
                self.tela.popup_msg_erro_partida()
                self.tela.fechaTela()
                return self.jogar_amistoso()
    
    
    def criar_partidas(self):
        while True:
            self.tela.menu_criar_partidas_camp()
            botao, valores = self.tela.abreTela()
            try:
                if botao != 'Confirmar':
                    self.tela.fechaTela()
                    break
                else:
                    sem_campeonato = valores['check']
                    if sem_campeonato:
                        lista = self.cm.ct.times_registrados
                        campeonato = None
                    else:
                        nome_campeonato = self.tela.selecionar_entradas((valores['in_camp'], valores['lst_camp']))
                        campeonato = self.cm.cc.buscar_nome(nome_campeonato)
                        if not campeonato:
                            raise EntradaVaziaError()
                        else:
                            lista = campeonato.times
                    partidas = []
                    arbitros = self.cm.cp.arbitros_registrados
                    botao = self.tela.popup_confirmacao_partidas(lista, campeonato)
                    if botao != 'Confirmar':
                        self.tela.fechaTela()
                        return self.criar_partidas()
                    else:
                        for time1 in lista:
                            for time2 in lista:
                                if isinstance(time1, Time) and isinstance(time2, Time) and (time1 != time2):
                                    i = random.randrange(len(arbitros))
                                    arbitro = arbitros[i]
                                    partida = Partida(time1, time2, arbitro)
                                    partidas.append(partida)
                        if not sem_campeonato:
                            campeonato.partidas.extend(partidas)
                        self.partidas.extend(partidas)
                        self.tela.fechaTela()
                    return partidas
            except EntradaVaziaError:
                self.tela.popup_msg_erro_partidas()
                self.tela.fechaTela()
    
    
    def jogar_partida(self, partida: Partida):

        def sort_gols(max_gols = 5):
            gols = []
            for i in range(max_gols):
                gol = random.randint(0,1)
                gols.append(gol)
            return sum(gols)
    
        def sort_temp_gols(qt_gols, temp = 90):
            tempo = []
            tgol = None
            for i in range(qt_gols):
                tgol = random.randrange(1, temp)
                while tgol in tempo:
                    tgol = random.randrange(1, temp)
                tempo.append(tgol)
                tempo.sort()
            return tempo
        
        def sort_jog_marc(time, gols):
            lj = []
            while len(lj) < gols:
                j = random.randrange(len(time.jogadores))
                jg = time.jogadores[j]
                if jg.posicao.posicao is not Goleiro().posicao:
                    lj.append(jg)
            return lj
                
        def sort_jog_tempo(lja, ljv, ltemp_gols):
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
                tupla = (marcadores[i], ltemp_gols[i])
                j_t.append(tupla)
            return j_t              
            
        def atl_jogadores(jogadores):
            for j in jogadores:
                j.gols_marcados += 1
                
        def atl_goleiro(time, gols_sofridos):
            i = 0
            while i < len(time.jogadores):
                if time.jogadores[i].posicao.posicao == Goleiro().posicao:
                    time.jogadores[i].gols_concedidos += gols_sofridos
                    return
                else:
                    i += 1
                    
        def atl_time(time, gols_p, gols_c):
            if gols_p > gols_c:
                time.vitorias += 1
            elif gols_p < gols_c:
                time.derrotas += 1
            else:
                time.empates += 1
            time.gols_marcados += gols_p
            time.gols_sofridos += gols_c


        ta = partida.time_anfitriao
        tv = partida.time_visitante
        gols_a = sort_gols()
        gols_v = sort_gols()
        placar = f'{gols_a} x {gols_v}'
        partida.placar = placar
        marc_a = sort_jog_marc(ta, gols_a)
        marc_v = sort_jog_marc(tv, gols_v)
        atl_goleiro(ta, gols_v)
        atl_goleiro(tv, gols_a)
        atl_time(ta, gols_a, gols_v)
        atl_time(tv, gols_v, gols_a)
        atl_jogadores(marc_a + marc_v)
        tt_gols = gols_a + gols_v
        tempo_gols = sort_temp_gols(tt_gols)
        rel_jog_gol = sort_jog_tempo(marc_a, marc_v, tempo_gols)
        rel_partida = [(partida.id_),(ta, gols_a, marc_a),(tv, gols_v, marc_v)]
        partida.relatorio = rel_jog_gol
        partida.gerar_sumula(rel_jog_gol)
        self.tela.janela_final_partida(partida)
        partida.tela_final = self.tela.janela
        partida.jogada = True

    
    def jogar(self, partida: Partida, multiplas_partidas = False):
        if not multiplas_partidas:
            self.tela.janela_inicio_partida(partida)
            botao, valores = self.tela.abreTela()
            self.tela.fechaTela()
            if botao == 'Jogar':
                self.jogar_partida(partida)
                self.tela.abreTela()
                self.tela.fechaTela()
        else:
            self.jogar_partida(partida)
        

    def jogar_camp(self):
        while True:
            self.tela.menu_jogar_camp()
            botao, valores = self.tela.abreTela()
            try:
                if botao != 'Confirmar':
                    self.tela.fechaTela()
                    break
                else:
                    sem_campeonato = valores['check']
                    if sem_campeonato:
                        partidas = []
                        for partida in self.partidas:
                            if not partida.jogada:
                                partidas.append(partida)
                        campeonato = None
                    else:
                        nome_campeonato = self.tela.selecionar_entradas((valores['in_camp'], valores['lst_camp']))
                        campeonato = self.cm.cc.buscar_nome(nome_campeonato)
                        if not campeonato:
                            raise EntradaVaziaError()
                        else:
                            partidas = campeonato.partidas
                    botao = self.tela.popup_jogar_camp(partidas, campeonato)
                    if botao != 'Confirmar':
                        self.tela.fechaTela()
                    else:
                        self.tela.fechaTela()
                        partidas_jogadas = []
                        for partida in partidas:
                            self.jogar(partida, True)
                            partidas_jogadas.append(partida)
                        return  self.ver_partidas_campeonato(partidas)
            except EntradaVaziaError:
                self.tela.popup_msg_erro_partidas()
                self.tela.fechaTela()

    
    def ver_partidas_campeonato(self, partidas):
        while True:
            self.tela.mostrar_partidas_campeonato(partidas)
            botao, valores = self.tela.abreTela()
            self.tela.fechaTela()
            if botao in range(1, len(partidas)+1):
                self.tela.janela_final_partida(partidas[botao-1])
                self.tela.abreTela()                
                self.tela.fechaTela()                   
            else:
                self.tela.fechaTela()
                break


    def ver_paridas_jogadas(self):
        while True:
            self.tela.menu_mostrar_partidas()
            botao, valores = self.tela.abreTela()
            try:
                if botao != 'Confirmar':
                    self.tela.fechaTela()
                    break
                else:
                    sem_campeonato = valores['check']
                    if sem_campeonato:
                        partidas = []
                        for partida in self.partidas:
                            if partida.jogada:
                                partidas.append(partida)
                        campeonato = None
                    else:
                        nome_campeonato = self.tela.selecionar_entradas((valores['in_camp'], valores['lst_camp']))
                        campeonato = self.cm.cc.buscar_nome(nome_campeonato)
                        if not campeonato:
                            raise EntradaVaziaError()
                        else:
                            partidas = []
                            for partida in campeonato.partidas:
                                if partida.jogada:
                                    partidas.append(partida)
                    self.tela.fechaTela()
                    return  self.ver_partidas_campeonato(partidas)
            except EntradaVaziaError:
                self.tela.popup_msg_erro_partidas()
                self.tela.fechaTela()

 
    def abre_tela(self):
        tela = True
        while tela:
            self.tela.exibir_menu()
            botao, valores = self.tela.abreTela()
            self.tela.fechaTela()
            opcoes = {'cp': self.jogar_amistoso, 'cps': self.criar_partidas, 'camp': self.jogar_camp, 'vpj': self.ver_paridas_jogadas}
            if botao in opcoes:
                opcoes[botao]()
            else:
                tela = False
            
              