import requests

url = "https://api.powerbi.com/beta/e0793d39-0939-496d-b129-198edd916feb/datasets/f77d1301-ba10-4740-99e2-6abdbf6bbcb8/rows?key=Rc8PyqK9s%2BhIN5xChnSSCeZNrzFCPSovZV0flwd0sKC8kBgzX%2FQTc5o0FC%2FzP7gG4OXMMQd%2B3jJyQWF2qKZaIQ%3D%3D"

variavel = 110

data = f"""[{{
        "SLA": {variavel},
       }}]"""

r = requests.post(url, data=data)
print(r.content)


# Retenção
url = "https://api.powerbi.com/beta/e0793d39-0939-496d-b129-198edd916feb/datasets/049274d3-989d-4f13-864b-412ee8350ab3/rows?key=l1Uq0pQyigQM%2FCkzuYhuksFGN7io%2BZxsF35lwIiq3F9XwrsZGyxV3Q%2BqXWUzg1O7DEbf0aRQmgpwdCr9FALoMw%3D%3D"
# Json
"""
[
{
"SLA" :98.6,
"Ciclo" :98.6,
"Automcao" :"AAAAA555555",
"Inicio" :"2019-06-26T18:54:41.938Z",
"Fim" :"2019-06-26T18:54:41.938Z",
"Caixa" :98.6
}
]
"""

# Download
url = "https://api.powerbi.com/beta/e0793d39-0939-496d-b129-198edd916feb/datasets/96808560-9a35-4803-8e14-0c97dfc18d43/rows?key=%2B9XYa4v6Pjkb%2BHib%2FCkc7q3MAkthPORlSiuK2%2BkaVoQe6O130VGKOaoE8598FkVfajEnJibvxDqGkg72%2F7MURw%3D%3D"
# Json
"""
[
{
"Para Fazer" :98.6,
"Downloads" :98.6,
"Já Analizados" :98.6,
"Feitos" :98.6,
"Salvo" :"2019-06-26T18:24:48.382Z"
}
]
"""

# Validação
url = "https://api.powerbi.com/beta/e0793d39-0939-496d-b129-198edd916feb/datasets/74d61e05-e4e7-44b4-bf88-2bdd23617371/rows?key=kFg4Lb3PuGAzAyM5RgysBr01o91%2FRIhK758DEc8dHmXMbtJjCcYDagLGRbfIWPuvgNGdw1RTLBFWvClInt1e%2BQ%3D%3D"
# Json
"""
[
{
"Para Fazer" :98.6,
"Validados" :98.6,
"Triagem" :98.6,
"Divergência Total" :98.6,
"Já Analizados" :98.6,
"Feitos" :98.6,
"Salvo" :"2019-06-26T18:35:31.064Z"
}
]
"""

# Input
url = "https://api.powerbi.com/beta/e0793d39-0939-496d-b129-198edd916feb/datasets/a82dc67e-afae-46f7-9056-ba57f462ab8d/rows?key=Xh4jpZ1GN%2FBQE6G5qVZ1L2DCmFRAAqmb9HWwjPbPu%2FirmLeypQXweh5Br1Ob6rQUHHSjtVcaGx6pp8yYDOXuww%3D%3D"
# Json
"""
[
{
"Para Fazer" :98.6,
"Inputados" :98.6,
"Já Analizados" :98.6,
"Feitos" :98.6,
"Salvo" :"2019-06-26T18:34:40.576Z"
}
]
"""