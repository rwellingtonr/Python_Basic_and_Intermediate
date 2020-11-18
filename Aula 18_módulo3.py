#bibliotecas
from random import randint
from time import sleep
#Aula 18
print('-='*30,'\n',' '*20, 'INÍCIO DA AULA 18\n','-='*29)
teste = list()
teste.append('Wellington')
teste.append('23')
galera = []
galera.append(teste[:])
teste[0] = 'Ruberval'
teste[1] = '40'
galera.append(teste[:])
print(galera)
#Lista dentro de lista
galera1 = [['Wellington', 23], ['Ana', 28] , ['Rodrigo', 26]]
print(galera1[0][0])
for g in galera1:
    print(f'{g[0]} tem {g[1]} anos de idade')
#Inserindo dados em lista de lista
galera2 = []
dado = []
for coun in range(5):
    dado.append(str(input('Digite um nome: ')).title().strip())
    dado.append(int(input('Qual é a idade? ')))
    galera2.append(dado[:])
    dado.clear()
print('Participantes da Festa!')
for cn in galera2:
    if cn[1] >= 21:
        print(f'\033[1;35mNome: {cn[0]}, idade: {cn[1]}\033[m')
    else:
        print(f'\033[1;37mNome: {cn[0]}, idade: {cn[1]}\033[m')

print('-='*30,'\n',' '*20, 'INÍCIO DOS EXERCÍCIOS\n','-='*29)
#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista85 = []
pares = []
impares = []
for l in range(7):
    lista85.append(int(input('Digite um número: ')))
    if lista85[0] % 2 == 0:
        pares.append(lista85[:])
    else:
        impares.append(lista85[:])
    lista85.clear()
pares.sort()
impares.sort()
print(f'Numero pares: {pares}')
print(f'numeros impares: {impares}')
print('-='*40,'\nExercício Python 086 e 087')
#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par86 = mlinha = mcoluna = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha+1}] [{1+coluna}]: '))
for linha in range(3):
    for coluna in range(3):
        print(f'\033[1;93m [{matriz[linha][coluna]:^6}]\033[m', end='')
        sleep(.8)
        if matriz[linha][coluna] % 2 == 0:
            par86 += matriz[linha][coluna]
        if mlinha < matriz[1][coluna]:
            mlinha = matriz[1][coluna]
    if coluna == 2:
        mcoluna += matriz[linha][coluna]
    print()
print('A) A soma de todos os valores pares digitados.', f'\n\033[1;96mSomatória dos pares é {par86}\033[m')
print('B) A soma dos valores da terceira coluna.', f'\n\033[1;96mSomatória da terceira coluna {mcoluna}\033[m')
print('C) O maior valor da segunda linha.', f'\n\033[1;96mMaior valor da segunda linha é o {mlinha}\033[m')
#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
palpites = []
palpites88 = list()
total_jogos = 0
print('xX'*30)
print('\n                     Jogos da Megasena \n')
print('xX'*30)
jogos88 = int(input('Quantos jogos você deseja fazer? '))
print(f'Gerando {jogos88} jogos para apostar na Megasena')
while total_jogos <= jogos88:
    contador = 0
    while True:
        numero88 = randint(1, 60)
        if numero88 not in palpites:
            palpites.append(numero88)
            contador += 1
        if contador >= 6:
            break
    total_jogos += 1
    palpites.sort()
    palpites88.append(palpites[:])
    palpites.clear()
for j88 in range(0, jogos88):
    if j88 % 2 == 0:
        print(f'\033[1;36mJogo Nº {j88+1}: {palpites88[j88]}\033[m')
    else:
        print(f'\033[1;31mJogo Nº {j88 + 1}: {palpites88[j88]}\033[m')
    sleep(1)
print('\nExercício Python 089')
#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = list()
escolar = dict()
media = 0
while True:
   # continuar = ' '
    aluno = str(input('Nome do aluno: ')).title().strip()
    n1 = float(input('Nota da primeira prova: '))
    n2 = float(input('Nota da segunda prova: '))
    media = (n1 + n2)/2
    lista.append([aluno, [n1, n2], media])
    lista.sort()
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('\033[35mDeseja continuar? \033[m'))[0].lower()
    if continuar == 'n':
        print('mostrar nota')
        break
print('_-'*40)
print(f'\033[1;47m{"No.":^6} | {"Aluno":^15} | {"Média":>5}\033[m')
for n, a in enumerate(lista):
    print(f'{n+1:^6} | {a[0]:^15} | \033[31m{a[2]:>5.2f}\033[m ' if a[2] < 7 else f'{n+1:^6} | {a[0]:^15} | \033[32m{a[2]:>5.2f}\033[m')
while True:
    continuar1 = ' '
    while continuar1 not in 'SsnN':
        continuar1 = str(input('Deseja verificar a nota de algum aluno? '))[0]
    if continuar1 in 'sS':
        estudante = str(input('Qual aluno? ')).title().strip()
        for a,b in enumerate(lista):
            if estudante == b[0]:
                print(f'As notas são: {lista[a][1]}')
    elif continuar1 in 'Nn':
        break
print('Boletim Finalizado')
print('-='*30,'\n',' '*20, 'FINAL DA LISTA DE EXERCÍCIOS\n','-='*29)