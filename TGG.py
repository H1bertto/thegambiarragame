from firebase.firebase import FirebaseAuthentication
from firebase.firebase import FirebaseApplication
from random import randint
# import getpass
import time
import sys


class Character:
    def __init__(self):
        self.name = ''
        self.race = ''
        self.nv = 1
        self.hp = 0
        self.hpmax = 0
        self.sp = 0
        self.spmax = 0
        self.dano = 0
        self.mdano = 0
        self.atk = 0
        self.matk = 0
        self.defe = 0
        self.mdefe = 0
        self.pfor = 0
        self.pcon = 0
        self.pint = 0
        self.pdex = 0
        self.crit = 0
        self.esq = 0
        self.dic_enemy = {
                          0: "THE GAMBIARRA",  # ULTRA BOSS
                          1: "Thanos",
                          2: "Dragão Branco de Olhos Azuis",
                          3: "Seu Chefe",
                          4: "Papai Noel",
                          5: "Darth Vader",
                          6: "Michel Temer",
                          7: "Bolsonaro",
                          8: "Ghal",
                          9: "Neymar",
                          10: "Ex peguete",
                          11: "Dorid",
                          12: "Cabal Sinistro",
                          13: "Motorista do Busão",
                          14: "Massagista Tailandeza",
                          15: "Roberval",
                          16: "Assaltante Favelado",
                          17: "Storm Trooper",
                          18: "Menina do Tinder",
                          19: "Fila do Refeitorio",
                          20: "Fornecedor",
                          21: "Esqueleto Magico",
                          22: "Pirata Raivoso",
                          23: "Árvore Monstro",
                          24: "Inumano",
                          25: "Soldado da Legião Vermelha",
                          26: "Vex",
                          27: "Decaido",
                          28: "Bowser",
                          29: "Fantasma",
                          30: "Eleitor Fanatico",
                          31: "Vespa Mutante",
                          32: "Lobo Feroz",
                          33: "Zumbi",
                          34: "Trol",
                          35: "Orc",
                          36: "Goblin",
                         }
        self.dic_places = {}

    def do_damage(self, enemy):
        damage = min(
            max(randint(0, self.hp) - randint(0, enemy.hp), 0),
            enemy.hp)
        enemy.hp = enemy.hp - damage
        if damage == 0:
            print("%s desvia do atk de %s'." % (enemy.name, self.name))
        else:
            print("%s acerta %d de dano em %s!" % (self.name, damage, enemy.name))
        return enemy.hp <= 0


class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = self.dic_enemy[randint(0, len(self.dic_enemy))]
        self.hp = randint(1, player.hp)


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.enemy = None
        self.state = 'normal'
        self.facction = ''
        self.reborn = False
        self.pcon = 5
        self.pfor = 5
        self.pdex = 5
        self.pint = 5
        self.exp = 0
        self.expmax = 0
        self.skill = 0
        self.skill2 = 0
        self.skill3 = 0
        self.skill4 = 0
        self.supreme = 0
        self.coin = 0
        self.bag = {}
        self.anteratk = 0
        self.antermatk = 0
        self.anterhpmax = 0
        self.anterspmax = 0
        self.antercrit = 0
        self.anteresq = 0
        self.anterdefe = 0
        self.antermdefe = 0
        self.armadisplay = "({0}) {name}\n\tAtk:\t{1}\n\tM.Atk:\t{2}\n\tDano:\t{3}\n\tDef:\t{4}" \
                           "\n\tM.Def:\t{5}\n\tInt:\t{6}\n\tDex:\t{7}\n\tCon:\t{8}\n\tFor:\t{9}\n"

    def atualizaratribs(self):
        baseatk = self.pfor * 2 + self.pcon
        basematk = self.pint * 2 + self.pcon
        basehpmax = self.pcon * 2 + self.pfor
        basespmax = self.pint * 2 + self.pcon
        basecrit = int(self.pdex * .5)
        baseesq = int(self.pdex * .75)
        basedefe = int(self.pfor * .5)
        basemdefe = int(self.pint * .5)
        self.atk += baseatk - self.anteratk
        self.matk += basematk - self.antermatk
        self.hpmax += basehpmax - self.anterhpmax
        self.spmax += basespmax - self.anterspmax
        self.crit += basecrit - self.antercrit
        self.esq += baseesq - self.anteresq
        self.defe += basedefe - self.anterdefe
        self.mdefe += basemdefe - self.antermdefe
        self.hp = self.hpmax
        self.sp = self.spmax
        self.anteratk = baseatk
        self.antermatk = basematk
        self.anterhpmax = basehpmax
        self.anterspmax = basespmax
        self.antercrit = basecrit
        self.anteresq = baseesq
        self.anterdefe = basedefe
        self.antermdefe = basemdefe

    def politico(self):
        self.hpmax = 175
        self.hp = self.hpmax
        self.spmax = 185
        self.sp = self.spmax
        a = ''
        while a == '':
            # Indc / Atk / M.Atk / Dano / Def / M.Def / Int / Dex / Con / For / Name
            print(self.armadisplay.format("1", "10", "0", "7~13", "+1", "+1", "0", "0", "0", "+1", name="Adaga de Ferro") +
                  self.armadisplay.format("2", "8", "0", "5~10", "+2", "+1", "0", "0", "+1", "0", name="Punhal Dente de Urso") +
                  self.armadisplay.format("3", "11", "0", "8~14", "+1", "0", "0", "+2", "0", "0", name="Estilingue de Madeira"))
            a = str(input("> "))
            try:
                a = int(a)
            except ValueError:
                print("Ainda não temos essa Arma")
                a = ''
            if a == 1:
                self.atk = 10
                self.defe = 1
                self.mdefe = 1
                self.pfor = 1
                return True
            elif a == 2:
                self.atk = 8
                self.defe = 2
                self.mdefe = 1
                self.pcon = 1
                return True
            elif a == 3:
                self.atk = 11
                self.defe = 1
                self.pdex = 2
                return True
            else:
                print("Ainda não temos essa Arma")
                a = ''

    def viking(self):
        self.hpmax = 210
        self.hp = self.hpmax
        self.spmax = 150
        self.sp = self.spmax
        a = ''
        while a == '':
            # Indc / Atk / M.Atk / Dano / Def / M.Def / Int / Dex / Con / For / Name
            print(self.armadisplay.format("1", "11", "0", "8~14", "+2", "0", "0", "0", "0", "+1", name="Machado de Ferro") +
                  self.armadisplay.format("2", "10", "0", "7~13", "+1", "0", "0", "0", "+1", "+1", name="Marreta de Pedra") +
                  self.armadisplay.format("3", "10", "0", "7~13", "+1", "0", "0", "0", "+2", "0", name="Maça de Ferro"))
            a = str(input("> "))
            try:
                a = int(a)
            except ValueError:
                print("Ainda não temos essa Arma")
                a = ''
            if a == 1:
                self.atk = 11
                self.defe = 2
                self.pfor = 1
                return True
            elif a == 2:
                self.atk = 10
                self.defe = 1
                self.pcon = 1
                self.pfor = 1
                return True
            elif a == 3:
                self.atk = 10
                self.defe = 1
                self.pcon = 2
                return True
            else:
                print("Ainda não temos essa Arma")
                a = ''

    def jedi(self):
        self.hpmax = 180
        self.hp = self.hpmax
        self.spmax = 180
        self.sp = self.spmax
        a = ''
        while a == '':
            # Indc / Atk / M.Atk / Dano / Def / M.Def / Int / Dex / Con / For / Name
            print(self.armadisplay.format("1", "11", "0", "8~14", "0", "0", "0", "+1", "0", "+1", name="Sabre Verde") +
                  self.armadisplay.format("2", "10", "0", "7~13", "0", "+1", "0", "0", "+1", "+1", name="Sabre Azul") +
                  self.armadisplay.format("3", "10", "0", "7~13", "+1", "0", "0", "+1", "+1", "0", name="Sabre Amarelo"))
            a = str(input("> "))
            try:
                a = int(a)
            except ValueError:
                print("Ainda não temos essa Arma")
                a = ''
            if a == 1:
                self.atk = 11
                self.pdex = 1
                self.pfor = 1
                return True
            elif a == 2:
                self.atk = 10
                self.mdefe = 1
                self.pcon = 1
                self.pfor = 1
                return True
            elif a == 3:
                self.atk = 10
                self.defe = 1
                self.pdex = 1
                self.pcon = 1
                return True
            else:
                print("Ainda não temos essa Arma")
                a = ''

    def monge(self):
        self.hpmax = 160
        self.hp = self.hpmax
        self.spmax = 200
        self.sp = self.spmax
        a = ''
        while a == '':
            # Indc / Atk / M.Atk / Dano / Def / M.Def / Int / Dex / Con / For / Name
            print(self.armadisplay.format("1", "0", "9", "6~12", "0", "+2", "+1", "0", "0", "0", name="Orbes de Ferro") +
                  self.armadisplay.format("2", "0", "11", "8~14", "+1", "+1", "0", "+1", "0", "0", name="Bastão de Madeira") +
                  self.armadisplay.format("3", "0", "10", "7~13", "+2", "0", "0", "0", "+1", "0", name="Punhos de Couro"))
            a = str(input("> "))
            try:
                a = int(a)
            except ValueError:
                print("Ainda não temos essa Arma")
                a = ''
            if a == 1:
                self.matk = 9
                self.mdefe = 2
                self.pint = 1
                return True
            elif a == 2:
                self.matk = 11
                self.defe = 1
                self.mdefe = 1
                self.pdex = 1
                return True
            elif a == 3:
                self.matk = 10
                self.defe = 2
                self.pcon = 1
                return True
            else:
                print("Ainda não temos essa Arma")
                a = ''

    def xaman(self):
        self.hpmax = 170
        self.hp = self.hpmax
        self.spmax = 190
        self.sp = self.spmax
        a = ''
        while a == '':
            # Indc / Atk / M.Atk / Dano / Def / M.Def / Int / Dex / Con / For / Name
            print(self.armadisplay.format("1", "0", "9", "6~12", "+2", "0", "0", "+1", "0", "0", name="Espirito de Urso") +
                  self.armadisplay.format("2", "0", "11", "8~14", "0", "0", "+3", "0", "0", "0", name="Espirito de Rapoza") +
                  self.armadisplay.format("3", "0", "10", "7~13", "+1", "0", "0", "0", "0", "+2", name="Espirito de Águia"))
            a = str(input("> "))
            try:
                a = int(a)
            except ValueError:
                print("Ainda não temos essa Arma")
                a = ''
            if a == 1:
                self.matk = 9
                self.defe = 2
                self.pcon = 1
                return True
            elif a == 2:
                self.matk = 11
                self.pdex = 3
                return True
            elif a == 3:
                self.matk = 10
                self.defe = 1
                self.pfor = 2
                return True
            else:
                print("Ainda não temos essa Arma")
                a = ''

    def constantine(self):
        self.hpmax = 170
        self.hp = self.hpmax
        self.spmax = 190
        self.sp = self.spmax
        a = ''
        while a == '':
            print("(1)Bastão de Ossos, (2)Cajado de Madeira, (3)Foice Lisa")
            # Indc / Atk / M.Atk / Dano / Def / M.Def / Int / Dex / Con / For / Name
            print(self.armadisplay.format("1", "0", "9", "6~12", "+2", "0", "0", "+1", "0", "0", name="Espirito de Urso") +
                  self.armadisplay.format("2", "0", "11", "8~14", "0", "0", "+3", "0", "0", "0", name="Espirito de Rapoza") +
                  self.armadisplay.format("3", "0", "10", "7~13", "+1", "0", "0", "0", "0", "+2", name="Espirito de Águia"))
            a = str(input("> "))
            try:
                a = int(a)
            except ValueError:
                print("Ainda não temos essa Arma")
                a = ''
            if a == 1:
                self.atk = 10
                self.matk = 0
                self.defe = 1
                self.mdefe = 1
                return True
            elif a == 2:
                self.atk = 8
                self.matk = 0
                self.defe = 2
                self.mdefe = 2
                return True
            elif a == 3:
                self.atk = 11
                self.matk = 0
                self.defe = 1
                self.mdefe = 0
                return True
            else:
                print("Ainda não temos essa Arma")
                a = ''

    def avenger(self):
        self.hpmax = 180
        self.hp = self.hpmax
        self.spmax = 180
        self.sp = self.spmax
        a = ''
        while a == '':
            print("(1)Punhos de choque, (2)Arco e flecha, (3)Pistola")
            a = str(input("> "))
            try:
                a = int(a)
            except ValueError:
                print("Ainda não temos essa Arma")
                a = ''
            if a == 1:
                self.atk = 10
                self.matk = 0
                self.defe = 1
                self.mdefe = 1
                return True
            elif a == 2:
                self.atk = 8
                self.matk = 0
                self.defe = 2
                self.mdefe = 2
                return True
            elif a == 3:
                self.atk = 11
                self.matk = 0
                self.defe = 1
                self.mdefe = 0
                return True
            else:
                print("Ainda não temos essa Arma")
                a = ''

    # Ações
    def quit(self):
        print("%s can't find the way back home, and dies of starvation.\nR.I.P." % self.name)
        self.hp = 0

    def help(self):
        pass

    def status(self):
        print("%s's HP: %d/%d" % (self.name, self.hp, self.hpmax))
        try:
            print("%s's HP: %d/%d" % (self.enemy.name, self.enemy.hp, self.enemy.hpmax))
        except AttributeError:
            pass

    def tired(self):
        print("%s fica cansado." % self.name)
        self.hp = max(1, self.hp - 1)

    def rest(self):
        if self.state != 'normal':
            print("%s não pode descansar agora!" % self.name)
            self.enemy_attacks()
        else:
            print("%s descansa e se recupera." % self.name)
        if randint(0, 1):
            self.enemy = Enemy(self)
            print("%s é brutalmente atacado por %s!" % (self.name, self.enemy.name))
            self.state = 'fight'
            self.enemy_attacks()
        else:
            if self.hp < self.hpmax:
                self.hp = self.hp + randint(10, 30)
                if self.hp > self.hpmax:
                    self.hp = self.hpmax
            else:
                print("%s descança demais." % self.name)
                self.hp = self.hp - 1

    def explore(self):
        if self.state != 'normal':
            print("%s está ocupado agora!" % self.name)
            self.enemy_attacks()
        else:
            print("%s explora uma pssagem sinuosa." % self.name)
            if randint(0, 1):
                self.enemy = Enemy(self)
                print("%s encontra %s!" % (self.name, self.enemy.name))
                self.state = 'fight'
            else:
                if randint(0, 1) and randint(0, 1):
                    self.tired()

    def flee(self):
        if self.state != 'fight':
            print("%s anda em circulos, parece retardado." % self.name)
            self.tired()
        else:
            if randint(1, self.hp + 5) > randint(1, self.enemy.hp):
                print("%s é covarde e foge da luta %s." % (self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
            else:
                print("%s não pode fugir agora %s!" % (self.name, self.enemy.name))
                self.enemy_attacks()

    def attack(self):
        if self.state != 'fight':
            print("%s ataca o ar, que burro da 0 pra ele." % self.name)
            self.tired()
        else:
            if self.do_damage(self.enemy):
                print("%s executa %s!" % (self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
                if randint(0, self.hp) < self.hpmax:
                    self.hp = self.hp + 1
                    self.hpmax = self.hpmax + 1
                    print("%s fica mais forte!" % self.name)
            else:
                self.enemy_attacks()

    def enemy_attacks(self):
        if self.enemy.do_damage(self):
            print("%s morreu por ser fraco de mais %s!!!\nR.I.P." % (self.name, self.enemy.name))


class Game:
    def __init__(self):
        self.version = "1.0.0"
        print("""
       ▄▄▄▄▀ ▄  █ ▄███▄         ▄▀  ██   █▀▄▀█ ███   ▄█ ██   █▄▄▄▄ █▄▄▄▄ ██       ▄█ ▄█ 
    ▀▀▀ █   █   █ █▀   ▀      ▄▀    █ █  █ █ █ █  █  ██ █ █  █  ▄▀ █  ▄▀ █ █      ██ ██ 
        █   ██▀▀█ ██▄▄        █ ▀▄  █▄▄█ █ ▄ █ █ ▀ ▄ ██ █▄▄█ █▀▀▌  █▀▀▌  █▄▄█     ██ ██ 
       █    █   █ █▄   ▄▀     █   █ █  █ █   █ █  ▄▀ ▐█ █  █ █  █  █  █  █  █     ▐█ ▐█ 
      ▀        █  ▀███▀        ███     █    █  ███    ▐    █   █     █      █      ▐  ▐ 
              ▀                       █    ▀              █   ▀     ▀      █            
                                     ▀                   ▀                ▀                     
        """)
        self.p = None
        self.continua = True
        self.senha = ''
        self.app = FirebaseApplication('https://thegambiarragame.firebaseio.com', authentication=None)
        self.authentication = FirebaseAuthentication('4PjjnBreuNDHH1vEnFcmURL2nVSNHRHR1vl5voIk', 'thegambiarra2@gmail.com', extra={'id': 123})
        self.app.authentication = self.authentication
        x = ''
        for i in range(11):
            x += '.'
            if len(x) == 4:
                x = ''
            print("", end="\rCarregando" + x)
            time.sleep(.3)
        print("", end="\r")

    def verificarversion(self):
        vers = self.app.get('/', "Version")
        if vers != self.version:
            print("Versão Desatualizada!")
            print("Versão Nova: " + vers)
            print("Versão Arual: " + self.version)
            print("Para Atualizar acesse:")
            print("https://innersource.accenture.com/projects/PSTFSC/repos/the-gambiarra/browse")
            time.sleep(15)
            sys.exit()
        else:
            print("Versão: " + self.version + " OK!")

    def carregarpersonagem(self, char):
        self.p.nv = self.app.get('/Personagens/' + char, "Nv")
        self.p.exp = self.app.get('/Personagens/' + char, "Exp")
        self.p.expmax = self.app.get('/Personagens/' + char, "ExpMax")
        self.p.hp = self.app.get('/Personagens/' + char, "Hp")
        self.p.hpmax = self.app.get('/Personagens/' + char, "HpMax")
        self.p.sp = self.app.get('/Personagens/' + char, "Sp")
        self.p.spmax = self.app.get('/Personagens/' + char, "SpMax")
        self.p.dano = self.app.get('/Personagens/' + char, "Damage")
        self.p.atk = self.app.get('/Personagens/' + char, "Atk")
        self.p.matk = self.app.get('/Personagens/' + char, "MAtk")
        self.p.defe = self.app.get('/Personagens/' + char, "Def")
        self.p.mdefe = self.app.get('/Personagens/' + char, "MDef")
        self.p.pfor = self.app.get('/Personagens/' + char, "For")
        self.p.pcon = self.app.get('/Personagens/' + char, "Con")
        self.p.pint = self.app.get('/Personagens/' + char, "Int")
        self.p.pdex = self.app.get('/Personagens/' + char, "Dex")
        self.p.crit = self.app.get('/Personagens/' + char, "Crit")
        self.p.esq = self.app.get('/Personagens/' + char, "Esq")
        self.p.race = self.app.get('/Personagens/' + char, "Class")
        self.p.skill = self.app.get('/Personagens/' + char, "Skill")
        self.p.skill2 = self.app.get('/Personagens/' + char, "Skill2")
        self.p.skill3 = self.app.get('/Personagens/' + char, "Skill3")
        self.p.skill4 = self.app.get('/Personagens/' + char, "Skill4")
        self.p.supreme = self.app.get('/Personagens/' + char, "Supreme")
        self.p.coin = self.app.get('/Personagens/' + char + '/Bag', "Coins")
        self.p.bag = self.app.get('/Personagens/' + char + '/Bag', "Item")

    def chooserace(self):
        escolhido = False
        while escolhido is False:
            print("   CLASSES         BASEADO EM       ESTILO                        SKILLS BASE             ")
            print("(1) Politico    - [Mercenário] - Melee/Ranged      - S1: Imposto Alto | S2: Cobrar Imposto")
            print("(2) Viking      - [Tank]       - Melee             - S1: ")
            print("(3) Jedi        - [Guerreiro]  - Melee/Ranged      - S1: ")
            print("(4) Monge       - [Mago]       - Melee/Mage        - S1: ")
            print("(5) Xaman       - [Invocador]  - Caster/Mage       - S1: ")
            print("(6) Constantine - [Mago Negro] - Caster/Mage       - S1: ")
            print("----------- Classe Liberada Apenas Para Reborn ----------")
            print("(7) Avenger     - [Especial]   - Melee/Mage/Ranged - S1: ")
            a = str(input("Classe: "))
            try:
                a = int(a)
            except ValueError:
                pass
            if a == 1:
                self.p.race = "Politico"
                escolhido = self.p.politico()
            elif a == 2:
                self.p.race = "Viking"
                escolhido = self.p.viking()
            elif a == 3:
                self.p.race = "Jedi"
                escolhido = self.p.jedi()
            elif a == 4:
                self.p.race = "Monge"
                escolhido = self.p.monge()
            elif a == 5:
                self.p.race = "Xaman"
                escolhido = self.p.xaman()
            elif a == 6:
                self.p.race = "Constantine"
                escolhido = self.p.constantine()
            elif a == 7 and self.p.reborn is True:
                self.p.race = "Avenger"
                escolhido = self.p.avenger()
            else:
                print("Não possue essa classe")
                escolhido = False
        self.p.atualizaratribs()

    def save(self):
        self.app.put('/Personagens/' + self.p.name, "Pass", self.senha)
        self.app.put('/Personagens/' + self.p.name, "Nv", self.p.nv)
        self.app.put('/Personagens/' + self.p.name, "Exp", self.p.exp)
        self.app.put('/Personagens/' + self.p.name, "ExpMax", self.p.expmax)
        self.app.put('/Personagens/' + self.p.name, "Class", self.p.race)
        self.app.put('/Personagens/' + self.p.name, "Hp", self.p.hp)
        self.app.put('/Personagens/' + self.p.name, "HpMax", self.p.hpmax)
        self.app.put('/Personagens/' + self.p.name, "Sp", self.p.sp)
        self.app.put('/Personagens/' + self.p.name, "SpMax", self.p.spmax)
        self.app.put('/Personagens/' + self.p.name, "Atk", self.p.atk)
        self.app.put('/Personagens/' + self.p.name, "MAtk", self.p.matk)
        self.app.put('/Personagens/' + self.p.name, "Def", self.p.defe)
        self.app.put('/Personagens/' + self.p.name, "MDef", self.p.mdefe)
        self.app.put('/Personagens/' + self.p.name, "Esq", self.p.esq)
        self.app.put('/Personagens/' + self.p.name, "Crit", self.p.crit)
        self.app.put('/Personagens/' + self.p.name, "Con", self.p.pcon)
        self.app.put('/Personagens/' + self.p.name, "For", self.p.pfor)
        self.app.put('/Personagens/' + self.p.name, "Dex", self.p.pdex)
        self.app.put('/Personagens/' + self.p.name, "Int", self.p.pint)
        self.app.put('/Personagens/' + self.p.name, "Skill", 'Espada de Fogo')
        self.app.put('/Personagens/' + self.p.name, "Skill2", 'Lamina Envenenada')
        self.app.put('/Personagens/' + self.p.name, "Skill3", '')
        self.app.put('/Personagens/' + self.p.name, "Skill4", '')
        self.app.put('/Personagens/' + self.p.name + '/Bag', "Coins", self.p.coin)
        self.app.put('/Personagens/' + self.p.name + '/Bag', "Item", self.p.bag)

    def play(self):
        self.verificarversion()
        new = 0
        while self.continua:
            correto = False
            print("\n> Start --------------------------------------------------")
            self.p = Player()
            Commands = {
                'q': Player.quit,
                'h': Player.help,
                's': Player.status,
                'r': Player.rest,
                'e': Player.explore,
                'f': Player.flee,
                'a': Player.attack,
                'd': 'Player.defend',
                'w': 'Player.special',
                '0': 'Player.equip',
            }
            while correto is False:
                print("Para Carregar ou Criar um personagem faça o Login")
                self.p.name = str(input("User: "))
                while self.p.name == "" or self.p.name == "\r\n" or self.p.name == " ":
                    print("Não pode usar esse nome!")
                    self.p.name = str(input("User: "))
                result = self.app.get('/Personagens', self.p.name)
                if result is not None:
                    print("Personagem existente")
                    self.senha = str(input("Senha: "))
                    pwd = self.app.get('/Personagens/' + self.p.name, "Pass")
                    if pwd == self.senha:
                        self.carregarpersonagem(self.p.name)
                        print("Carregado")
                        correto = True
                    else:
                        print("Senha Incorreta!")
                        correto = False
                else:
                    print("Novo Personagem")
                    new = 1
                    self.senha = str(input("Senha: "))
                    self.chooserace()
                    correto = True

            print("Bem Vindo ao Gambiarra World!")
            if new == 1:
                print("Você ganhou o pacote de iniciante: ")
                print("- Coins = 1000")
                self.p.coin = 1000
                print("- Pot HP = 5")
                self.p.bag['HpPot'] = 5
                print("- Pot SP = 5")
                self.p.bag['SpPot'] = 5
                new = 0
            print("Comece a explorar!")
            while self.p.hp > 0:
                line = input("> ")
                args = line.split()
                if len(args) > 0:
                    commandFound = False
                    for c in Commands.keys():
                        if args[0] == c[:len(args[0])]:
                            Commands[c](self.p)
                            commandFound = True
                            break
                    if not commandFound:
                        print("%s não pode fazer isso agora." % self.p.name)


            x = input("\nGostaria de Salvar seu progresso? (s/n): ")
            if x == 's':
                self.save()

            z = input("\nContinuar? (s/n): ")
            if z == 'n':
                self.continua = False


if __name__ == "__main__":
    Game().play()
