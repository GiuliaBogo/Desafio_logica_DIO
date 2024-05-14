'''
Desafio Classificador de nível de Herói

XP < 1000 = Ferro
1.001 <= XP <= 2.000 = Bronze
2.001 <= XP <= 5.000 = Prata
5.001 <= XP <= 7.000 = Ouro
7.001 <= XP <= 8.000 = Platina
8.001 <= XP <= 9.000 = Ascendente
9001 <= XP <= 10.000 = Imortal
XP >= 10.001 = Radiante

Output: "O Herói de nome {nome} está no nível de {nivel}"
'''

nome = input("Insira a seguir o nome do seu Herói: ")
xp = int(input("Insira a seguir a XP do seu Herói: "))

if xp <= 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 5000:
    nivel = "Prata"
elif 5001 <= xp <= 7000:
    nivel = "Ouro"
elif 7001 <= xp <= 8000:
    nivel = "Platina"
elif 8001 <= xp <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp <= 10000:
    nivel = "Imortal"
elif xp >= 10001:
    nivel = "Radiante"

print(f"O Herói de nome {nome} está no nível de {nivel}")