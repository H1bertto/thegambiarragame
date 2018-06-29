from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication

app = FirebaseApplication('https://thegambiarragame.firebaseio.com', authentication=None)
authentication = FirebaseAuthentication('', '@gmail.com', extra={'id': 123})
app.authentication = authentication
# print(authentication.extra)
user = authentication.get_user()
# print(user.firebase_auth_token)
# result = app.get('/Personagens', "Jaca")
# app.put('/Personagens', "Teste", "Cratoz")
# print(result)
correto = False
while correto is False:
    a = str(input("User: "))
    result = app.get('/Personagens', a)
    if result is not None:
        print("Personagem existente")
        b = str(input("Senha: "))
        paz = app.get('/Personagens/' + a, "Pass")
        if paz == b:
            print("Carregado")
            correto = True
        else:
            print("Senha Incorreta!")
            correto = False
    else:
        print("Novo Personagem")
        b = str(input("Senha: "))
        app.put('/Personagens/' + a, "Pass", b)
        app.put('/Personagens/' + a, "Nv", 1)
        g = str(input("Classe: "))
        app.put('/Personagens/' + a, "Class", g)
        app.put('/Personagens/' + a, "Hp", 30)
        app.put('/Personagens/' + a, "HpMax", 30)
        app.put('/Personagens/' + a, "Sp", 20)
        app.put('/Personagens/' + a, "SpMax", 20)
        app.put('/Personagens/' + a, "Atk", 10)
        app.put('/Personagens/' + a, "MAtk", 0)
        app.put('/Personagens/' + a, "Def", 5)
        app.put('/Personagens/' + a, "MDef", 2)
        app.put('/Personagens/' + a, "Esq", 2)
        app.put('/Personagens/' + a, "Crit", 1)
        app.put('/Personagens/' + a, "Con", 5)
        app.put('/Personagens/' + a, "For", 5)
        app.put('/Personagens/' + a, "Dex", 5)
        app.put('/Personagens/' + a, "Int", 5)
        app.put('/Personagens/' + a, "Skill", 'Espada de Fogo')
        app.put('/Personagens/' + a, "Skill2", 'Lamina Envenenada')
        app.put('/Personagens/' + a, "Skill3", '')
        app.put('/Personagens/' + a, "Skill4", '')
        d = 'Pot'
        app.put('/Personagens/' + a + '/Bag', "Coins", 0)
        app.put('/Personagens/' + a + '/Bag', "Item", d)
        app.put('/Personagens/' + a + '/Bag', "Quant" + d, 0)
        correto = True
