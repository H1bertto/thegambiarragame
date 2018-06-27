from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication

app = FirebaseApplication('https://thegambiarragame.firebaseio.com', authentication=None)
authentication = FirebaseAuthentication('', 'humbertovs20@gmail.com', extra={'id': 123})
app.authentication = authentication
# print(authentication.extra)
user = authentication.get_user()
# print(user.firebase_auth_token)
result = app.get('/Personagens/Cratoz', "Pass")
# app.put('/Personagens', "Teste", "Cratoz")
print(result)
a = str(input(">"))
b = str(input("senha"))
app.put('/Personagens/' + a, "Pass", b)
