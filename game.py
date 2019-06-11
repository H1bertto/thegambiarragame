# Python bytecode 3.6 (3379)
# Embedded file name: C:\Users\humberto.v.souza\PycharmProjects\Kivy\The_Gambiarra.py
# Compiled at: 2018-06-22 19:35:56
# Decompiled by https://python-decompiler.com
from win32com.client import Dispatch
from random import randint
import getpass
import time
import sys


class Character:

    def __init__(self):
        self.name = ''
        self.enemy = ''
        self.arma = 0
        self.espadafogo = 4
        self.lancafog = 5
        self.hadouken = 7
        self.martelothor = 6
        self.pistolalaser = 4
        self.sabre = 6
        self.peido = 5
        self.desintegrador = 7
        self.shuriken = 4
        self.a1 = 1
        self.a2 = 2
        self.a3 = 3
        self.health = 1
        self.health_max = 1
        self.exploration = 0
        self.experience = 0
        self.experience_max = 5
        self.dic_location = {1: 'uma passagem sinuosa',
                             2: 'uma sala secreta',
                             3: 'um vale',
                             4: 'redores de um lago',
                             5: 'uma caverna',
                             6: 'o Brasil',
                             7: 'a Guaicurus',
                             8: 'buteco Risca Faca',
                             9: 'a Nova Sala do Tech Master',
                             10: 'o Bh Shop',
                             11: 'a Praca 7',
                             12: 'o toba da pessoa da sua frente',
                             13: 'uma floresta densa',
                             14: 'uma Praia',
                             15: 'um estacionamento',
                             16: 'dentro do seu guarda-roupa',
                             17: 'um Predio Abandonado ',
                             18: 'um quarto de Motel',
                             19: 'o deserto do Saara',
                             20: 'debaixo da mesa',
                             21: 'a Lua',
                             22: 'o Sol',
                             23: 'sua Casa',
                             24: 'a Russia',
                             25: 'rua la de casa'}
        self.dic_enemy = {1: 'Darth Vader',
                          2: 'Thanos',
                          3: 'Michel Temer',
                          4: 'The Gambiarra',
                          5: 'Donald Trump',
                          6: 'Juiz dos Erros Mexicano',
                          7: 'Madero',
                          8: 'Acriano Carequinha',
                          9: 'C.I.O.',
                          10: 'Seu Ex',
                          11: 'Idoso Andando Devagar na Sua Frente',
                          12: 'Fornecedor',
                          13: 'Fila do Refeitorio',
                          14: 'Operador de Telemarket Chato',
                          15: 'Funkero de Som Alto',
                          16: 'Sua Ex',
                          17: 'Motorista do Busao',
                          18: 'Bowser',
                          19: 'Teletubies',
                          20: 'Michael Jeckson',
                          21: 'Massagista Tailandes',
                          22: 'Um Duende',
                          23: 'Um Orc',
                          24: 'Loki',
                          25: 'Um Robo',
                          26: 'Um Zumbi',
                          27: 'Sua Sombra',
                          28: 'Neymar',
                          29: 'Roberval',
                          30: 'Menina do Tinder'}
        self.dic_arma = {1: self.espadafogo,
                         2: self.lancafog,
                         3: self.hadouken,
                         4: self.martelothor,
                         5: self.pistolalaser,
                         6: self.sabre,
                         7: self.peido,
                         8: self.desintegrador,
                         9: self.shuriken,
                         10: self.a1,
                         11: self.a2,
                         12: self.a3}

    def do_damage(self, enemy, special=None, skill=None):
        tank = 0
        doutk = 0
        if special == 0:
            damage = self.arma * int(randint(3, self.arma + 2))
        else:
            if skill == 1:
                damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health) + int(randint(0, self.arma))
                if randint(0, 1) and randint(0, 1) and randint(0, 1):
                    self.health += damage
                    if self.health >= self.health_max:
                        self.health = self.health_max
                    print('Lifesteal!!!   HP %d/%d' % (self.health, self.health_max))
            elif skill == 2:
                damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health) + int(randint(0, self.arma))
                if randint(0, 1) and randint(0, 1) and randint(0, 1):
                    atk = randint(20, 40)
                    print('Frenzy!!!  ATK +' + str(atk))
                    damage += atk
            elif skill == 3:
                print('Invisible!!!')
                damage = 0
            elif skill == 5:
                damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health) + int(randint(0, self.arma))
                if randint(0, 1) and randint(0, 1) and randint(0, 1):
                    tank += randint(20, 40)
                    print('Full Tank!!!  HP +' + str(tank))
            else:
                damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health) + int(randint(0, self.arma))
                if randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1):
                    print('Critico!')
                    damage = int(damage + damage / 2)
                if damage > int(enemy.health_max + enemy.health_max / 2):
                    print('Critico!')
            if skill == 6 and randint(0, 1) and randint(0, 1) and randint(0, 1):
                doutk = 1
                print('Double ATK!!!')
                enemy.health = enemy.health - damage
                enemy.health = tank + enemy.health - damage
        if damage == 0:
            print('%s desvia do ataque de %s.' % (enemy.name, self.name))
        elif special == 0 and skill == 6 and doutk == 1:
            print('%s usa todo seu poder Special e acerta [%s] de dano em %s!' % (self.name, str(damage), enemy.name))
            print('%s usa todo seu poder Special e acerta [%s] de dano em %s!' % (self.name, str(damage), enemy.name))
            print('%s canalisa o Special acertando [%s] de dano em %s!' % (self.name, str(damage), enemy.name))
        elif skill == 6 and doutk == 1:
            print('%s acerta [%s] de dano em %s!' % (self.name, str(damage), enemy.name))
            print('%s acerta [%s] de dano em %s!' % (self.name, str(damage), enemy.name))
        else:
            print('%s acerta [%s] de dano em %s!' % (self.name, str(damage), enemy.name))
        return enemy.health <= 0


class Enemy(Character):

    def __init__(self, player):
        Character.__init__(self)
        inim = randint(4, len(self.dic_enemy))
        if randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1):
            inim = randint(1, 2)
        if randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1) and randint(0, 1):
            inim = randint(3, 6)
        self.name = self.dic_enemy[inim]
        if self.name == 'Darth Vader' or self.name == 'Thanos':
            print('ULTRA BOSS!!!')
            self.health = int(player.health_max + player.health_max * 2)
            self.health_max = self.health
            self.arma = int(self.dic_arma[randint(1, len(self.dic_arma))]) + 5
        else:
            if self.name == 'Michel Temer' or self.name == 'The Gambiarra' or self.name == 'Donald Trump' or self.name == 'Juiz dos Erros Mexicano':
                print('Boss!!!')
                self.health = int(player.health_max + player.health_max + 15)
                self.health_max = self.health
                self.arma = int(self.dic_arma[randint(1, len(self.dic_arma))]) + 3
            else:
                if randint(0, 1):
                    print('Normal!')
                    self.health = randint(10, player.health_max)
                    self.health_max = self.health
                    self.arma = int(self.dic_arma[randint(1, len(self.dic_arma))])
                else:
                    print('Fraco!')
                    self.health = randint(1, player.health_max - 10)
                    self.health_max = self.health
                    self.arma = int(self.dic_arma[randint(1, len(self.dic_arma))]) - 3
            if self.arma < 1:
                self.arma = 1
            if player.nv > 100:
                self.health_max += 20
                self.arma += 20
            else:
                if player.nv > 80:
                    self.health_max += 15
                    self.arma += 17
                else:
                    if player.nv > 65:
                        self.health_max += 10
                        self.arma += 14
                    else:
                        if player.nv > 50:
                            self.health_max += 5
                            self.arma += 10
                        else:
                            if player.nv > 40:
                                self.arma += 7
                            else:
                                if player.nv > 30:
                                    self.arma += 5
                                else:
                                    if player.nv > 20:
                                        self.arma += 4
                                    else:
                                        if player.nv > 15:
                                            self.arma += 3
                                        else:
                                            if player.nv > 10:
                                                self.arma += 2
                                            else:
                                                if player.nv > 5:
                                                    self.arma += 1
            self.health = self.health_max


class Player(Character):

    def __init__(self):
        Character.__init__(self)
        self.state = 'normal'
        self.titulo = ''
        self.newtitulo = ''
        self.health = 20
        self.health_max = 20
        self.tesouro = 0
        self.nv = 1
        self.kills = 0
        self.bossk = 0
        self.use = 0
        self.bpoints = 0
        self.kpoints = 0
        self.umavez = 0
        self.hppot = 0
        self.skill = None

    def quit(self):
        print('%s saiu com sucesso!' % self.name)
        self.state = 'normal'

    def equip(self):
        a = ''
        while a == '':
            print('Escolha a Arma')
            print('(1)Excalibur, (2)Lanca Missil, (3)Hadouken, (4)Mjolnir, (5)Arma de Paintball (6)Sabre de Luz (7)Peido da Vovo, (8)Desintegrator de Almas, (9)Shuriken')
            a = input('> ')
            try:
                a = int(a)
            except ValueError:
                print('Ainda nao temos essa Arma')
                a = ''

        self.arma = self.dic_arma[a]

    def help(self):
        self.name = self.name
        print("Acoes - 'a': Atk |'d': Def |'w': Special |'r': Recuperar |'f': Fugir | 'e': Explorar")
        print("Infos - 'h': Help |'s': Status |'q': Quit |'.': Ranking |'b': Shop")

    def status(self):
        if self.skill == 1:
            sk = 'Lifesteal'
        else:
            if self.skill == 2:
                sk = 'Frenzy'
            else:
                if self.skill == 3:
                    sk = 'Invisible'
                else:
                    if self.skill == 4:
                        sk = 'Super Hero'
                    else:
                        if self.skill == 5:
                            sk = 'Full Tank'
                        else:
                            if self.skill == 6:
                                sk = 'Double ATK'
                            else:
                                sk = 'Sem Skill'
        try:
            print('%s --- STATUS ---' % self.name)
            print('> HP: %d/%d | ATK: %d | NV: %d | EXP: %d/%d | TITULO: %s' % (
             self.health, self.health_max, self.arma, self.nv, self.experience, self.experience_max, self.titulo))
            print('> SKILL: %s | SPECIAL: %d | HP POT: %d | KILLS: %d | BAUS: %d' % (
             sk, self.use, self.hppot, self.kills, self.tesouro))
            print('%s --- STATUS ---' % self.enemy.name)
            print('> HP: %d/%d | ATK: %d' % (
             self.enemy.health, self.enemy.health_max, self.enemy.arma))
        except AttributeError:
            pass

    def tired(self):
        print('%s sente-se cansado.' % self.name)
        self.health = max(1, self.health - 1)

    def rest(self):
        if self.state != 'normal':
            if self.hppot == 0:
                print('%s nao possue potes de HP!' % self.name)
                self.enemy_attacks()
            else:
                self.hppot -= 1
                if self.health < self.health_max:
                    self.health += randint(4, 8)
                    if self.health > self.health_max:
                        self.health = self.health_max
                print('%s se cura.   |Potes: %d   |HP: %d/%d' % (self.name, self.hppot, self.health, self.health_max))
        else:
            if randint(0, 1):
                if randint(0, 1):
                    if randint(0, 1):
                        self.enemy = Enemy(self)
                        print('%s e rudemente despertado por %s!' % (self.name, self.enemy.name))
                        self.state = 'fight'
                        if randint(0, 1):
                            self.defend()
                        else:
                            self.enemy_attacks()
                    if self.health < self.health_max:
                        if self.nv > 70:
                            self.health += randint(8, 12)
                        else:
                            if self.nv > 50:
                                self.health += randint(5, 9)
                            else:
                                self.health += randint(3, 7)
                        if self.health > self.health_max:
                            self.health = self.health_max
                        print('%s se recupera.    |HP: %d/%d' % (self.name, self.health, self.health_max))
                    else:
                        print('%s dorme demais.' % self.name)

    def explore(self):
        if self.state != 'normal':
            print('%s esta muito ocupado agora!' % self.name)
            self.enemy_attacks()
        else:
            print('%s explora ' % self.name + str(self.dic_location[randint(1, len(self.dic_location))]) + '.')
            if randint(0, 1):
                self.enemy = Enemy(self)
                print('%s encontra %s!' % (self.name, self.enemy.name))
                self.state = 'fight'
                self.exploration = 0
            else:
                if self.exploration == 3:
                    self.exploration = 0
                    self.tired()
                else:
                    if randint(0, 1):
                        if randint(0, 1):
                            if randint(0, 1):
                                pass
        if randint(0, 1):
            if randint(0, 1):
                if randint(0, 1):
                    self.treasure()
                if randint(0, 1):
                    if randint(0, 1):
                        if randint(0, 1):
                            if randint(0, 1):
                                if randint(0, 1):
                                    print('%s encontra Comida!' % self.name)
                                    if self.health < self.health_max:
                                        self.health += randint(3, 5)
                                        if self.health > self.health_max:
                                            self.health = self.health_max
                                        else:
                                            print('%s encontra uma Fonte de Agua!' % self.name)
                                            if self.health < self.health_max:
                                                self.health += randint(1, 3)
                                                if self.health > self.health_max:
                                                    self.health = self.health_max
                                    self.exploration += 1
                                    print('Nada por aqui...')

    def flee(self):
        if self.state != 'fight':
            print('%s corre em circulos por um tempo.' % self.name)
            self.tired()
        else:
            if randint(1, self.health + 5) > randint(1, self.enemy.health):
                print('%s foge de %s.' % (self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
            else:
                print('%s nao pode escapar de %s!' % (self.name, self.enemy.name))
                self.enemy_attacks()

    def attack(self, s=None, sk=None):
        if self.skill != 0 or self.skill is not None:
            sk = self.skill
            if sk == 3:
                sk = None
        if self.state != 'fight':
            print('%s golpeia o ar, sem resultados notaveis.' % self.name)
            self.tired()
        else:
            if self.do_damage(self.enemy, s, sk):
                print('K.O.!')
                print('%s executa %s!' % (self.name, self.enemy.name))
                self.kills += 1
        if self.enemy.name == 'Thanos':
            self.experience += int(self.experience_max / 2 + randint(6, 10))
            self.kpoints += 2000
            self.bossk += 2
            self.newtitulo = '<{{{>AVENGER<}}}>'
            if randint(0, 1) and randint(0, 1):
                print('Drop: Pote de HP')
                self.hppot += 1
            if randint(0, 1):
                if randint(0, 1):
                    pass
        if randint(0, 1):
            if randint(0, 1):
                if randint(0, 1):
                    if randint(0, 1):
                        if randint(0, 1):
                            self.treasure(1)
                        self.treasure()
                    self.title()
                else:
                    if self.enemy.name == 'Darth Vader':
                        self.experience += int(self.experience_max / 2 + randint(6, 10))
                        self.kpoints += 1000
                        self.bossk += 2
                        self.newtitulo = '{{ JEDI MASTER }}'
                        if randint(0, 1):
                            if randint(0, 1):
                                print('Drop: Pote de HP')
                                self.hppot += 1
                        self.title()
                    else:
                        if self.enemy.name == 'Michel Temer' or self.enemy.name == 'The Gambiarra' or self.enemy.name == 'Donald Trump' or self.enemy.name == 'Juiz dos Erros Mexicano':
                            self.experience += int(self.experience_max / 3 + randint(2, 6))
                            self.kpoints += 100
                            self.bossk += 1
                            if randint(0, 1):
                                if randint(0, 1):
                                    print('Drop: Pote de HP')
                                    self.hppot += 1
                                else:
                                    if randint(0, 1):
                                        if randint(0, 1):
                                            if randint(0, 1):
                                                if randint(0, 1):
                                                    print('Drop: Pote de HP')
                                                    self.hppot += 1
                                    self.kpoints += 10
                                    if self.nv > 50:
                                        self.experience += randint(4, 8)
                                    else:
                                        self.experience += randint(1, 5)
                    if self.bossk == 20:
                        self.newtitulo = '<))>>K. BOSS<<((>'
                        self.title()
                    if 20000 <= self.kpoints < 20500:
                        if self.titulo != ')>>  MURDERER <<(':
                            self.newtitulo = ')>> :MURDERER <<('
                            self.title()
                        if 6000 <= self.kpoints < 6500:
                            if self.titulo != ':>>>  SLAYER <<<:':
                                self.newtitulo = ':>>>  SLAYER <<<:'
                                self.title()
                    self.enemy = None
                    self.state = 'normal'
                    self.lvl()
            else:
                self.enemy_attacks()

    def special(self):
        if self.skill == 4:
            if self.health_max >= 24:
                if self.use <= 10:
                    self.use += 1
                    self.attack(s=0)
            print('Special nao liberado')
        else:
            if self.health_max >= 24:
                if self.use < 4:
                    self.use += 1
                    self.attack(s=0)
                print('Special nao liberado')

    def lvl(self):
        if self.experience >= self.experience_max:
            if self.use <= 4:
                self.use = 0
            self.health = self.health + 1
            self.health_max = self.health_max + 1
            self.experience = 0
            self.experience_max += 3
            print('%s se sente mais forte!' % self.name)
            self.nv += 1
            print('Nv: ' + str(self.nv))
            if self.nv % 5 == 0:
                self.arma += 1
            if self.nv == 5:
                self.newtitulo = '    - NOOB -     '
            else:
                if self.nv == 15:
                    self.newtitulo = '   < TECHNO >    '
                else:
                    if self.nv == 30:
                        self.newtitulo = '  .> WARRIOR <.  '
                    else:
                        if self.nv == 50:
                            self.newtitulo = '.^z. KNIGTH .z^. '
                        else:
                            if self.nv == 70:
                                self.newtitulo = '  SUPREMO  '
                            else:
                                if self.nv == 100:
                                    self.newtitulo = '<<|>IMPERADOR<|>>'
            self.title()

    def title(self):
        if self.newtitulo != self.titulo:
            print('Voce adquiriu um novo titulo, deseja mudar? (s/n)')
            print('ATUAL: %s >>> NOVO: %s' % (self.titulo, self.newtitulo))
            mud = input('> ')
            if mud == 's':
                print('Titulo Alterdo, continue explorando...')
                self.titulo = self.newtitulo
            else:
                self.newtitulo = self.titulo
                print('Titulo Mantido, continue explorando...')

    def defend(self):
        if self.state != 'fight':
            print('%s parece um covarde, se escondendo atras do escudo.' % self.name)
            self.tired()
        else:
            if randint(0, 1):
                print('%s nao consegue defender o ataque de %s!' % (self.name, self.enemy.name))
                self.enemy_attacks()
            else:
                print('%s bloqueia o ataque de %s!' % (self.name, self.enemy.name))
                if randint(0, 1):
                    print('%s contra ataca %s!' % (self.name, self.enemy.name))
                    self.attack()

    def treasure(self, e=0):
        if e == 1:
            print('%s encontra um Bau Divino!!!' % self.name)
            print('Arma >> Manopla do Infinito Refinada:  HP +25  ATK +15')
            self.bpoints += 1000
            self.health_max += 25
            self.health = self.health_max
            self.arma += 15
        else:
            print('%s encontra um Bau Magico!' % self.name)
            self.health = self.health_max
            if randint(0, 1):
                if randint(0, 1):
                    if randint(0, 1):
                        pass
            if randint(0, 1):
                if randint(0, 1):
                    if randint(0, 1):
                        print('Lendario!!!')
                        self.tesouro += 1
                        self.bpoints += 100
                        self.health_max += 3
                        self.health = self.health_max
                        self.arma += 3
                    if randint(0, 1):
                        if randint(0, 1):
                            if randint(0, 1):
                                print('Epico!!')
                                self.tesouro += 1
                                self.bpoints += 50
                                self.arma += 2
                            print('Raro!')
                            self.tesouro += 1
                            self.bpoints += 10
                            self.arma += 1
                if self.bpoints >= 5000:
                    self.newtitulo = '$$)>>INFINITY<<($$'
                    self.title()
                if self.bpoints >= 800:
                    self.newtitulo = '<$$FORTUNEHACK$$>'
                    self.title()
                else:
                    if self.bpoints >= 300:
                        self.newtitulo = ':$ LORD  LUCKY $:'
                        self.title()

    def enemy_attacks(self):
        if self.skill == 3:
            pass
        if randint(0, 1):
            if randint(0, 1):
                if self.enemy.do_damage(self, skill=self.skill):
                    print('%s foi abatido por %s!!!\nGAME OVER' % (self.name, self.enemy.name))
                    self.health = 0
                    self.state = 'normal'
                if self.enemy.do_damage(self):
                    print('%s foi abatido por %s!!!\nGAME OVER' % (self.name, self.enemy.name))
                    self.health = 0
                    self.state = 'normal'


class Game:

    def __init__(self):
        self.vers = '9.0.5'
        print('\n')
        print('\t  ===== |   | ====     -==.   /\\   |\\  /| ===-, |   /\\   ===-. ===-.   /\\       ')
        print('\t    |   |===| |--     |   _  /==\\  | \\/ | |--=: |  /==\\  |___/ |___/  /==\\      ')
        print("\t    |   |   | ====     -==T /    \\ |    | ===-' | /    \\ |   \\ |   \\ /    \\    ")
        print('                                                                                      ')
        print('\t      --===::|,,                                            ,,|::===--              ')
        print('\t     --====::|HHHHHHHHHHHHHD~~~~     <>     ~~~~CHHHHHHHHHHHHH|::====--             ')
        print("\t      --===::|''                                            ''|::===--              ")
        print('======================================================================================')
        print('\n')
        x = ''
        for i in range(11):
            x += '.'
            if len(x) == 4:
                x = ''
            print('', end=('\rCarregando' + x))
            time.sleep(0.4)

        print('', end='\r')
        self.continua = True
        self.senha = ''
        self.p = None
        self.select = 'SELECT'
        self.dbRank = 'DBQ=\\\\10.22.81.81\\Unilever\\Uni\\Uni.accdb; Pwd=gambithe2018'
        self.drive = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        self.conn_str = self.drive + self.dbRank
        self.conect = Dispatch('ADODB.Connection')
        self.conect.ConnectionString = self.conn_str
        self.conect.Open()
        self.rs = Dispatch('ADODB.RecordSet')
        self.rs2 = Dispatch('ADODB.RecordSet')
        self.rs3 = Dispatch('ADODB.RecordSet')
        self.rs4 = Dispatch('ADODB.RecordSet')

    def rank(self):
        self.rs2.Open(self.select + ' TOP 5 * FROM tbRank ORDER BY Nv DESC, KillPoints DESC, BauPoints DESC', self.conect, 3, 3)
        self.rs2.MoveFirst()
        print('\n                                            <| RANKING |>')
        print('================================================.\\^/.==============================================')
        print('\tNOME \t NV \tKILLS\tK.POINTS\tBAUS \t B.POINTS\tTITULO')
        while self.rs2.EOF is False:
            namrank = str(self.rs2.Fields.Item('Name').Value)
            if len(namrank) == 4:
                namrank += '  '
            else:
                if len(namrank) == 5:
                    namrank += ' '
            print(f"> {namrank}\t| {str(self.rs2.Fields.Item('Nv').Value)}  \t| {str(self.rs2.Fields.Item('Kills').Value)}\t| {str(self.rs2.Fields.Item('KillPoints').Value)}\t    | {str(self.rs2.Fields.Item('Bau').Value)}  \t  | {str(self.rs2.Fields.Item('BauPoints').Value)}\t\t| {str(self.rs2.Fields.Item('Titulo').Value)}")
            self.rs2.MoveNext()

        print('===================================================================================================')
        self.rs2.Close()

    def shop(self):
        self.rs4.Open(self.select + ' * FROM tbSkill', self.conect, 1, 3)
        self.rs4.MoveFirst()
        print('\n                                    ~~~~~~ SHOP SKILLS ~~~~~~')
        print('=============================================.\\^/.===========================================')
        print(' ID   SKILL\t  B.POINTS     K.POINTS\t DESCRIPTION')
        while self.rs4.EOF is False:
            skname = str(self.rs4.Fields.Item('SkName').Value)
            if len(skname) < 9:
                skname += '    '
            else:
                if len(skname) < 10:
                    skname += ' '
            print('> ' + str(self.rs4.Fields.Item('ID').Value) + ' - ' + skname + '    ' + str(self.rs4.Fields.Item('Cost').Value) + '   ou   ' + str(int(self.rs4.Fields.Item('Cost').Value) * 15) + '\t- ' + str(self.rs4.Fields.Item('Desc').Value))
            self.rs4.MoveNext()

        print('=============================================================================================')
        print('\nDesenha comprar uma Skill? (s/n)')
        dej = input('> ')
        if dej == 's':
            print('Digite o ID da Skill desejada:')
            x = int(input('> '))
            if x <= 6:
                print('Voce possue B.Points: ' + str(self.p.bpoints) + ' |K.Points: ' + str(self.p.kpoints))
                print('Como deseja pagar: 1 - B.Points ou 2 - K.Points')
                pag = int(input('> '))
                x = str(x)
                self.rs4.Filter = 'ID=' + x
                if pag == 1:
                    if int(self.rs4.Fields.Item('Cost').Value) <= self.p.bpoints:
                        self.p.skill = int(self.rs4.Fields.Item('ID').Value)
                        self.p.bpoints -= int(self.rs4.Fields.Item('Cost').Value)
                        print('Parabens voce adquiriu a Skill: ' + str(self.rs4.Fields.Item('SkName').Value))
                    else:
                        print('Pontos insuficientes!')
                else:
                    if pag == 2:
                        if int(self.rs4.Fields.Item('Cost').Value) * 15 <= self.p.kpoints:
                            self.p.skill = int(self.rs4.Fields.Item('ID').Value)
                            self.p.kpoints -= int(self.rs4.Fields.Item('Cost').Value) * 15
                            print('Parabens voce adquiriu a Skill: ' + str(self.rs4.Fields.Item('SkName').Value))
                        else:
                            print('Pontos insuficientes!')
                    else:
                        print('Nao aceitamos essa moeda!')
            else:
                print('Nao possuimos essa Skill!')
        else:
            print('Nao entendi.')
        print('Volte sempre!')
        print('Continue a explorar...')
        self.rs4.Filter = ''
        self.rs4.Close()

    def version(self):
        self.rs3.Open(self.select + ' * FROM tbVersion', self.conect, 3, 3)
        if str(self.rs3.Fields.Item('Versao').Value) != self.vers:
            print('Versao Desatualizada!')
            print('Versao Nova: ' + str(self.rs3.Fields.Item('Versao').Value))
            print('Versao Arual: ' + self.vers)
            print('Para Atualizar acesse:')
            print('https://innersource.accenture.com/projects/PSTFSC/repos/the-gambiarra/browse')
            time.sleep(15)
            self.rs3.Close()
            sys.exit()
        else:
            print('Versao: ' + str(self.rs3.Fields.Item('Versao').Value) + ' OK!')

    def play(self):
        self.version()
        while self.continua:
            self.rs.Open(self.select + ' * FROM tbRank', self.conect, 1, 3)
            self.rank()
            correto = False
            print('\n\n\n> Start --------------------------------------------------')
            self.p = Player()
            Commands = {'q': Player.quit,
                        'h': Player.help,
                        's': Player.status,
                        'r': Player.rest,
                        'e': Player.explore,
                        'f': Player.flee,
                        'a': Player.attack,
                        'd': Player.defend,
                        'w': Player.special,
                        '0': Player.equip
                        }
            while correto is False:
                self.p.name = str(input('\nQual nome do seu Personagem? '))
                while self.p.name == '' or self.p.name == '\r\n' or self.p.name == ' ':
                    print('Nao pode usar esse nome!')
                    self.p.name = str(input('\nQual nome do seu Personagem? '))

                criterio = "Name='" + self.p.name + "'"
                self.rs.Filter = criterio
                if self.rs.EOF is False:
                    print('Nome ja cadastrado')
                    self.senha = getpass.getpass('Digite a senha: ')
                    self.rs.MoveFirst()
                    while self.rs.EOF is False:
                        if self.senha == self.rs.Fields.Item('Senha').Value:
                            print('Personagem carregado!')
                            self.p.nv = int(str(self.rs.Fields.Item('Nv').Value))
                            self.p.experience_max = int(str(self.rs.Fields.Item('Nv').Value)) * 3
                            self.p.health = int(str(self.rs.Fields.Item('Hp').Value))
                            if self.p.health == 0:
                                if self.p.nv >= 75:
                                    self.p.health = 30
                                else:
                                    if self.p.nv >= 50:
                                        self.p.health = 20
                                    else:
                                        self.p.health = 10
                            self.p.health_max = int(str(self.rs.Fields.Item('HpMax').Value))
                            self.p.arma = int(str(self.rs.Fields.Item('Arma').Value))
                            self.p.tesouro = int(str(self.rs.Fields.Item('Bau').Value))
                            self.p.bpoints = int(str(self.rs.Fields.Item('BauPoints').Value))
                            self.p.kills = int(str(self.rs.Fields.Item('Kills').Value))
                            self.p.kpoints = int(str(self.rs.Fields.Item('KillPoints').Value))
                            self.p.titulo = str(self.rs.Fields.Item('Titulo').Value)
                            self.p.newtitulo = self.p.titulo
                            self.p.experience = int(str(self.rs.Fields.Item('Exp').Value))
                            self.p.hppot = int(str(self.rs.Fields.Item('HpPot').Value))
                            self.p.skill = int(str(self.rs.Fields.Item('Skill').Value))
                            if self.p.skill == 0:
                                self.p.skill = None
                            if self.p.nv < 10:
                                mud = input('Deseja mudar de arma? (s/n)')
                                if mud == 's':
                                    Commands['0'](self.p)
                            correto = True
                        self.rs.MoveNext()

                    if correto is False:
                        print('Senha incorreta, digite novamente!')
                    else:
                        print('Novo Personagem!')
                        self.senha = getpass.getpass('Digite a senha: ')
                        Commands['0'](self.p)
                        correto = True

            if randint(0, 1):
                print("(Dica: 'h' mostra a lista de comandos)\n")
            else:
                if randint(0, 1):
                    print('(Dica: Pote de HP cura 4~8 de vida e e consumido apenas em batalhas)\n')
                else:
                    if randint(0, 1):
                        print('(Dica: Special so sera liberado no Nv5)\n')
                    else:
                        print('(Dica: Special so pode usar 4 vezes por Nv)\n')
            print('%s entrou em League of Tech Masters.' % self.p.name)
            print('Que comece a aventura...')
            line = ''
            while self.p.health > 0:
                if line != 'q':
                    line = input('> ')
                    if len(line) > 0:
                        commandFound = False
                        for c in Commands.keys():
                            if line == '.':
                                self.rank()
                                commandFound = True
                                break
                            if line == 'b':
                                self.shop()
                                commandFound = True
                                break
                            if line == c:
                                Commands[c](self.p)
                                commandFound = True
                                break

                        if not commandFound:
                            print('%s nao pode fazer isso agora.' % self.p.name)

            x = input('\nGostaria de Salvar seu progresso? (s/n): ')
            if x == 's':
                criterio1 = "Name='" + self.p.name + "'"
                self.rs.Filter = criterio1
                if self.rs.EOF is False:
                    self.rs.Fields.Item('Nv').Value = self.p.nv
                    self.rs.Fields.Item('Hp').Value = self.p.health
                    self.rs.Fields.Item('HpMax').Value = self.p.health_max
                    self.rs.Fields.Item('Arma').Value = self.p.arma
                    self.rs.Fields.Item('Kills').Value = self.p.kills
                    self.rs.Fields.Item('KillPoints').Value = self.p.kpoints
                    self.rs.Fields.Item('Bau').Value = self.p.tesouro
                    self.rs.Fields.Item('BauPoints').Value = self.p.bpoints
                    self.rs.Fields.Item('Titulo').Value = str(self.p.titulo)
                    self.rs.Fields.Item('Exp').Value = self.p.experience
                    self.rs.Fields.Item('HpPot').Value = self.p.hppot
                    if self.p.skill is None:
                        self.p.skill = 0
                    self.rs.Fields.Item('Skill').Value = self.p.skill
                    self.rs.MoveNext()
                    print('Atualizacao Salva!')
                else:
                    if self.rs.EOF is True:
                        nv = str(self.p.nv)
                        hp = str(self.p.health)
                        hpmax = str(self.p.health_max)
                        arm = str(self.p.arma)
                        kills = str(self.p.kills)
                        kp = str(self.p.kpoints)
                        bau = str(self.p.tesouro)
                        bp = str(self.p.bpoints)
                        tit = str(self.p.titulo)
                        exp = str(self.p.experience)
                        pot = str(self.p.hppot)
                        if self.p.skill is None:
                            self.p.skill = 0
                        sk = str(self.p.skill)
                        into = 'INSERT INTO tbRank VALUES '
                        insert = into + "('" + self.p.name + "', '" + self.senha + "', '" + hp + "', '" + hpmax + "', '" + nv + "', '" + arm + "', '" + kills + "', '" + kp + "', '" + bau + "', '" + bp + "', '" + tit + "', '" + exp + "', '" + pot + "', '" + sk + "')"
                        self.conect.execute(insert)
                        print('Salvo!')
                        del nv
                        del hp
                        del hpmax
                        del arm
                        del kills
                        del kp
                        del bau
                        del bp
                        del into
                        del tit
                        del exp
                        del pot
                        del sk
            n = input('\nTry Again? (s/n): ')
            if n == 'n':
                self.continua = False
            else:
                print('Aeeeeeeeeeeeeee!!!')
                self.rs.Close()
                time.sleep(2)

        print('Adios!')
        self.rs.Close()
        self.conect.Close()
        sys.exit()


if __name__ == '__main__':
    Game().play()
