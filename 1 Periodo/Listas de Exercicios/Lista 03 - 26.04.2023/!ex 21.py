'''
21. Em uma eleição existem quatro candidatos. Os votos são informados através de códigos. Os dados
utilizados para a contagem dos votos obedecem à seguinte codificação:
a. 1, 2, 3, 4: voto para os respectivos candidatos
b. 5 = voto nulo
c. 6 = votam em branco
Escreva um programa que faz a leitura de uma sequência de votos (até que zero seja digitado). Ao
final, o programa deve calcular e mostrar os totais de:
a. votos por candidato
b. votos nulos
c. Votos em branco
OBS: os votos em branco somam para o candidato que tiver mais votos (ao final).
'''

numero = int(input('Escolha um valor para o número: '))

votosCandidato1 = 0
votosCandidato2 = 0
votosCandidato3 = 0
votosCandidato4 = 0
votosNulos = 0
votosBrancos = 0

while numero != 0:
    if numero == 1:
        votosCandidato1 += 1
    elif numero == 2:
        votosCandidato2 += 1
    elif numero == 3:
        votosCandidato3 += 1
    elif numero == 4:
        votosCandidato4 += 1
    elif numero == 5:
        votosNulos += 1
    elif numero == 6:
        votosBrancos += 1
    numero = int(input('Escolha um valor para o número: '))

maior = votosCandidato1
if votosCandidato2 > maior:
    maior = votosCandidato2
if votosCandidato3 > maior:
    maior = votosCandidato2
if votosCandidato4 > maior:
    maior = votosCandidato2

print(f'''
      Candidato1 = {votosCandidato1}
      Candidato2 = {votosCandidato2}
      Candidato3 = {votosCandidato2}
      Candidato4 = {votosCandidato2}
      Nulos = {votosNulos}
      Brancos = {votosBrancos}
      Mais votos + Brancos = {maior + votosBrancos}
      ''')

#github.com/tiagodefendi
