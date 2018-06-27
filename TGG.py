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
        correto = True
