#Bibliotecas
from time import sleep
from random import randint
#Aula
print('-='*60)
print(' '*50, 'INÍCIO DA AULA 15')
print('-='*60)
print('Para sair do programa digite 999')
entrada = media = i = soma = 0
while True:
    entrada = int(input('Digite um valor inteiro: '))
    if entrada == 999:
        print('O programa será encerrado!')
        break
    else:
        i += 1
    soma += entrada
media = soma/i
print(f'Total de entradas {i};\nValor da soma {soma};\nMédia {media:.2f}')
sleep(1)
print('-='*60)
print(' '*50, 'INÍCIO DOS EXERCÍCIOS')
print('-='*60,'\nExercício Python 067')
#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    tabuada = int(input('Digite um valor para a tabuada: '))
    if tabuada < 0:
        print('Programa interrompido!')
        break
    print('x'*20)
    for c in range(1, 11):
        print(f'{c} x {tabuada} = {c*tabuada}')
        c += 1
    print('x' * 20)
sleep(2)
print('-'*55, ' / / ', 55*'-','\nExercício Python 068')
#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
v = d = 0
while True:
    escolha_pc = randint(0, 5)
    escolha_jogador = int(input('Escolha um número: '))
    total = escolha_pc + escolha_jogador
    jogador = ' '
    while (jogador not in 'PI'):
        jogador = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]
    print(f'Computador escolheu o número: {escolha_pc} e o Jogador escolheu o número: {escolha_jogador}', end=' ')
    print('Deu Par' if (total % 2 == 0) else 'Deu Impar')
    if jogador == 'P':
        if total % 2 == 0:
            print('O jogador ganhou')
            v += 1
        else:
            print('O computador venceu')
            break
    elif jogador == 'I':
        if total % 2 == 1:
            print('O jogador ganhou')
            v += 1
        else:
            print('O computador venceu')
            break
    print('Vamos jogar novamente...')
print(f'O jogador venceu {v} vezes!')
sleep(2)
print('-'*55, ' / / ', 55*'-','\nExercício Python 069')
'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
mais18 = homem =  mulher = 0
continuar = ' '
while continuar not in 'N':
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Qual é o seu sexo [M/F]? ')).upper().strip()[0]
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if idade > 18:
        mais18 += 1
        if sexo == 'M':
            homem +=1
    else:
        if sexo == 'F':
            mulher +=1
        else:
            homem +=1
print(f'''A) quantas pessoas tem mais de 18? {mais18}
B) quantos homens foram cadastrados? {homem}
C) quantas mulheres tem menos de 20 anos? {mulher}''')
sleep(2)
print('-'*55, ' / / ', 55*'-','\nExercício Python 070')
'''Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
menorp = t = mil = prod = 0
while True:
    produto = str(input('Produto: ')).strip().title()
    preco = float(input('Peço do produto: '))
    if preco > 1000:
        mil += 1
    co = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    t += preco
    prod += 1
    if prod == 1:
        menorp = preco
        barato = produto
    elif preco < menorp:
        menorp = preco
        barato = produto
    if co == 'N':
        print('Proceçando')
        sleep(2)
        break
print(f'''Qual é o total gasto na compra? \33[32m{t}\33[m
Quantos produtos custam mais de R$1000? \33[32mDe {prod} produtos, apenas, {mil} custam mais de R$1000,00\33[m
Qual é o nome do produto mais barato?\33[32m {barato} e custa R${menorp}\33[m''')
sleep(2)
print('-'*55, ' / / ', 55*'-','\nExercício Python 071')
'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
saque = int(input('Quanto deseja sacar? R$'))
ced = 50
word = ' '
numcel = 0
while True:
    if saque >= ced:
        saque -= ced
        numcel += 1
    else:
        if numcel > 0:
            if numcel > 1:
                word = 'cédulas'
            elif numcel == 1:
                word = 'cédula'
            print(f'Necessário {numcel} {word} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if saque == 0:
            break
        numcel = 0
print('-='*60)
print(' '*50, 'FINAL DO MÓDULO 2')
print('-='*60)
