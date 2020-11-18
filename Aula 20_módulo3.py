#Bibliotecas
from random import randint
#Aula
def mostraLinha():
    print('-'*50)


mostraLinha()
print(' '*18, 'INÍCIO DA AULA 20')
mostraLinha()
#Trabahando com Parametros de Função
def titulo(txt):
    print('-'*50)
    print(txt)
    print('-' * 50)


titulo('Trabalhando com')
titulo('Parâmetros de')
titulo('Função!')
#Exercícios
def divisaoDeExercicios():
    from time import sleep
    print('\033[1;104m Final do Exercício!\033[m')
    print('-' * 50)
    sleep(1)


print('Exercício Python 096')
#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimeto):
    total = largura * comprimeto
    print(f'A área do terreno é {total:.2f}')


a = float(input('largura: '))
b = float(input('comprimento: '))
area(a, b)

divisaoDeExercicios()
print('Exercício Python 097')
'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''
def escreva(msg):
    print('~'*40)
    print(msg)
    print('~'*40)
escreva('\033[1;92m Olá, mundo!\033[m')
escreva('\033[1;36m Bonde do Tigrão\033[m')
divisaoDeExercicios()
print('Exercício Python 098')
def contador(inicio, fim, passo):
    print('','-'*40)
    print(f'Contando de \033[1;32m{inicio}\033[m até \033[1;32m{fim}\033[m no passo de \033[1;32m{passo}\033[m')
    if passo > 0:
        for v in range(inicio, fim+1, passo):
            print(v, end= '; ')
    else:
        for v in range(inicio, fim-1, passo):
            print(v, end= '; ')
    print('\n','-'*40)

contador(1, 10, 1)
contador(10,0, -1)
c = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
contador(c, f, p)
divisaoDeExercicios()
#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
print('Exercício Python 099')
def maior(* num):
    maior = cont = 0
    print('Valores analisados:', end=' ', flush=True)
    sleep(0.3)
    for valor99 in num:
        print(f'\033[1;31m{valor99}\033[m', end= ' ', flush=True)
        if cont == 0:
            maior = valor99
        elif valor99 > maior:
            maior = valor99
        cont += 1
    print(f'\nO maior valor informado foi o \033[1;31m{maior}\033[m\nE o número de valores informados foi \033[1;31m{cont}\033[m')


maior(randint(1, 10), randint(1, 10) , randint(1, 10), randint(1, 10))
sleep(1)
print('-'*40)
maior(randint(11, 99), randint(11, 99) , randint(11, 99), randint(11, 99), randint(11, 99), randint(11, 99), randint(11, 99), randint(11, 99), randint(11, 99))
divisaoDeExercicios()
#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
print('Exercício Python 100')
numeros = list()
def sorteia():
    for n in range(5):
        numeros.append(randint(0, 100))
    print('='*30)
    print(      numeros)
    print('=' * 30)

def somaPar():
    valor = 0
    for n1 in numeros:
        if n1 % 2 == 0:
            valor += n1
    print('.' * 50)
    print(f'=> A soma de todos os valores pares é de: {valor}')
    print('.' * 50)

sorteia()
somaPar()
print('-'*40)
print(''*20, 'FINAL DA AULA 20')
print(40*'-')