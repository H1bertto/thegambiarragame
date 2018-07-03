from firebase.firebase import FirebaseAuthentication
from firebase.firebase import FirebaseApplication
from random import randint
import getpass
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

    def dodamage(self, a):
        self.dano = randint(a-int(a/3), a+a)


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.skill = 0
        self.skill2 = 0
        self.skill3 = 0
        self.skill4 = 0
        self.supreme = 0
        self.coin = 0
        self.bag = {}
        if self.race == "Politico":
            self.hpmax = 170
            self.hp = self.hpmax
            self.spmax = 160
            self.sp = self.spmax
        elif self.race == "Viking":
            self.hpmax = 200
            self.hp = self.hpmax
            self.spmax = 130
            self.sp = self.spmax
        elif self.race == "Jedi":
            self.hpmax = 180
            self.hp = self.hpmax
            self.spmax = 180
            self.sp = self.spmax
        elif self.race == "Palhaço":
            self.hpmax = 150
            self.hp = self.hpmax
            self.spmax = 200
            self.sp = self.spmax
        elif self.race == "Dark Safari":
            self.hpmax = 160
            self.hp = self.hpmax
            self.spmax = 190
            self.sp = self.spmax
        elif self.race == "Constantine":
            self.hpmax = 170
            self.hp = self.hpmax
            self.spmax = 190
            self.sp = self.spmax
        elif self.race == "Avenger":
            self.hpmax = 180
            self.hp = self.hpmax
            self.spmax = 180
            self.sp = self.spmax

    def politico(self):
        a = ''
        while a == '':
            print("(1)Adaga de Ferro, (2)Punhal Dente de Urso, (3)Estilingue de Madeira")
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

    def viking(self):
        a = ''
        while a == '':
            print("(1)Machado De Ferro, (2)Marreta de Pedra, (3)Maça de Ferro")
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

    def jedi(self):
        a = ''
        while a == '':
            print("(1)Sabre Verde, (2)Sabre Azul, (3)Sabre Amarelo")
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

    def monge(self):
        a = ''
        while a == '':
            print("(1)Orbes, (2)Cajado de Ferro, (3)Punhos")
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

    def xaman(self):
        a = ''
        while a == '':
            print("(1)Espirito de Urso, (2)Espirito de Rapoza, (3)Espirito de Águia")
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

    def constantine(self):
        a = ''
        while a == '':
            print("(1)Varinha de Ossos, (2)Cajado de Madeira, (3)Orbe")
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


class Game:
    def __init__(self):
        print("The Gambiarra")
        self.p = None
        self.continua = True
        self.senha = ''
        self.app = FirebaseApplication('https://thegambiarragame.firebaseio.com', authentication=None)
        self.authentication = FirebaseAuthentication('', '@gmail.com', extra={'id': 123})
        self.app.authentication = self.authentication

    def carregarpersonagem(self, char):
        self.p.nv = self.app.get('/Personagens' + char, "Nv")
        self.p.hp = self.app.get('/Personagens' + char, "Hp")
        self.p.hpmax = self.app.get('/Personagens' + char, "HpMax")
        self.p.sp = self.app.get('/Personagens' + char, "Sp")
        self.p.spmax = self.app.get('/Personagens' + char, "SpMax")
        self.p.dano = self.app.get('/Personagens' + char, "Damage")
        self.p.atk = self.app.get('/Personagens' + char, "Atk")
        self.p.matk = self.app.get('/Personagens' + char, "MAtk")
        self.p.defe = self.app.get('/Personagens' + char, "Def")
        self.p.mdefe = self.app.get('/Personagens' + char, "MDef")
        self.p.pfor = self.app.get('/Personagens' + char, "For")
        self.p.pcon = self.app.get('/Personagens' + char, "Con")
        self.p.pint = self.app.get('/Personagens' + char, "Int")
        self.p.pdex = self.app.get('/Personagens' + char, "Dex")
        self.p.crit = self.app.get('/Personagens' + char, "Crit")
        self.p.esq = self.app.get('/Personagens' + char, "Esq")
        self.p.race = self.app.get('/Personagens' + char, "Class")
        self.p.skill = self.app.get('/Personagens' + char, "Skill")
        self.p.skill2 = self.app.get('/Personagens' + char, "Skill2")
        self.p.skill3 = self.app.get('/Personagens' + char, "Skill3")
        self.p.skill4 = self.app.get('/Personagens' + char, "Skill4")
        self.p.supreme = self.app.get('/Personagens' + char, "Supreme")
        self.p.coin = self.app.get('/Personagens' + char + '/Bag', "Coins")
        self.p.bag = self.app.get('/Personagens' + char + '/Bag', "Item")

    def chooserace(self):
        escolhido = False
        while escolhido is False:
            print("(1) Politico - ")
            print("(2) Viking - ")
            print("(3) Jedi - ")
            print("(4) Monge - ")
            print("(5) Xaman - ")
            print("(6) Constantine - ")
            print("(7) Avenger - ")
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
            elif a == 7:
                self.p.race = "Avenger"
                escolhido = self.p.avenger()
            else:
                print("Não possue essa classe")
                escolhido = False

    def play(self):
        while self.continua:
            correto = False
            print("\n\n\n> Start --------------------------------------------------")
            self.p = Player()
            """Commands = {
                'q': Player.quit,
                'h': Player.help,
                's': Player.status,
                'r': Player.rest,
                'e': Player.explore,
                'f': Player.flee,
                'a': Player.attack,
                'd': Player.defend,
                'w': Player.special,
                '0': Player.equip,
            }"""
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
                    self.senha = str(input("Senha: "))
                    self.chooserace()
                    correto = True

            self.p.bag['HpPot'] = 5
            self.p.bag['SpPot'] = 5
            self.p.coin = 1000

            x = input("\nGostaria de Salvar seu progresso? (s/n): ")
            if x == 's':
                self.app.put('/Personagens/' + self.p.name, "Pass", self.senha)
                self.app.put('/Personagens/' + self.p.name, "Nv", self.p.nv)
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
                self. app.put('/Personagens/' + self.p.name, "Skill4", '')
                self.app.put('/Personagens/' + self.p.name + '/Bag', "Coins", self.p.coin)
                self.app.put('/Personagens/' + self.p.name + '/Bag', "Item", self.p.bag)


if __name__ == "__main__":
    Game().play()

