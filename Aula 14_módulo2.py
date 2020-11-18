#Bibliotecas
from random import randint
from time import sleep

#Códigos
print('INÍCIO DA AULA 14')
c =1
while c <10:
    print(c, end=' ')
    c += 1
print('\n','-'*40, ' / / ', 40*'-')
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Fim. Você digitou {} pares e {} impares'.format(par, impar))
print('-'*40, ' / / ', 40*'-', '\nExercício Python 057')
#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
p = 0
while p != 1:
    s = str(input('Digite o seu sexo [M/F] ')).upper()
    if s == 'M' or s == 'F':
        p += 1
        if s == 'M':
            s = 'Masculino'
        else:
            s = 'Feminino'
print('Sexo: ', s)
print('-'*40, ' / / ', 40*'-', '\nExercício Python 058')
#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
computador = randint(0, 10)
jogador = 11
palpites = 0
while jogador != computador:
    jogador = int(input('Tente adivinhar o número que o computador pensou de 0 a 10: '))
    palpites += 1
print('Parabéns jogador, você acertou o número que o computador pensou, cujo era o número {}\nE você precisou de {} palpites para acertar'.format(computador, palpites))
print('-'*40, ' / / ', 40*'-', '\nExercício Python 059')
'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
opção = 0
valor = 0
dellai = 5
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa\n''')
    opção = int(input('Qual será a sua opção? '))
    if opção == 1:
        valor = n1+n2
        print('O valor é {}'.format(valor))
    elif opção == 2:
        valor = n1 * n2
        print('O valor é {}'.format(valor))
    elif opção == 3:
        if n1 > n2:
            print('O primeiro valor é maior, pois ele é o {} e o menor é {}'.format(n1, n2))
        elif n1 == n2:
            print('Não existe maior, pois os dois tem o mesmo valor. Cujo é {}'.format(n1))
        else:
            print('O segundo valor é maior, pois ele é o {} e o menor é {}'.format(n2, n1))
    elif opção == 4:
        n1 = int(input('Digite o primeiro número inteiro: '))
        n2 = int(input('Digite o segundo número inteiro: '))
    elif opção == 5:
        print('O sistema irá finalizar em 5 segundos')
        while dellai != -1:
            print('{}'.format(dellai), end='')
            print(' - ' if dellai != 0 else '', end='')
            dellai -= 1
            sleep(1)
    else:
        print('Valor digitado errado')

print('\nPrograma Finalizado')
print('-'*40, ' / / ', 40*'-', '\nExercício Python 060')
#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
i = int(input('Digite um número inteiro qualquer: '))
m = i
f = 1
print('calculando {}!: '.format(i))
while m > 0:
    print('{}'.format(m), end='')
    print(' x ' if m > 1 else ' = ', end='')
    f *= m
    m -= 1
print('\33[1:32m{}\n\33[m'.format(f))
print('-'*40, ' / / ', 40*'-', '\nExercício Python 061')
#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
s = 1
while s < 11:
    print('\33[31m{}\33[m'.format(a), end='')
    print(' -> ' if s < 10 else '',end='')
    a += r
    s += 1
print('\nFIM')
print('-'*40, ' / / ', 40*'-', '\nExercício Python 062')
#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
o = int(input('Entre com um termo: '))
raz = int(input('Qual é a razão de crescimento: '))
v = 1
rep = 11
while v < rep:
    print('\33[2:35m{}\33[m'.format(o), end='')
    print(' - ' if v < (rep - 1) else '', end='')
    o += raz
    v += 1
    if v == rep:
        continuar = int(input('\n\33[31mDeseja continuar mais quantas vezes?\33[m '))
        rep += continuar
        if continuar == 0:
            print('Quantidade de repetições {}.\nPrograma finalizado'.format(rep - 1))

print('-'*40, ' / / ', 40*'-', '\nExercício Python 063')
#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
numero = int(input('Quantidade de termos da sequencia de Fibonacci: '))
fn1 = 0
fn2 = 1
contador1 = 3
print('{} - {} - '.format(fn1, fn2), end='')
while contador1 <= numero:
    fn = fn1 + fn2
    if fn % 2 == 0:
        print('\33[32m{}\33[m'.format(fn), end='')
    else:
        print('\33[33m{}\33[m'.format(fn), end='')
    print(' - ' if contador1 < numero else '', end='')
    fn1 = fn2
    fn2 = fn
    contador1 += 1
print('\nFIM')
print('-'*40, ' / / ', 40*'-', '\nExercício Python 064')

#xercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
condicao = 999
soma = digitados = entrada = media = maior = menor = 0
print('Código de parada = {}'.format(condicao))
while (condicao != entrada) or continuar == 'S':
    entrada = int(input('Digite um valor para ser somado: '))
    soma += entrada
    digitados += 1
    if entrada != 999:
        if digitados == 1:
            maior = menor = entrada
        else:
            if (entrada > maior):
                maior = entrada
            elif (entrada < menor):
                menor = entrada
    else:
        continuar = str(input('Deseza continuar [S/N] ')).upper().strip()
        soma -= 999
        digitados -= 1
media = soma/digitados
print('''\33[1mVocê digitou o código de parada.\33[m
A somatória dos valores de entrada é de \33[34m{}\33[m e o total de números digitados foram \33[34m{}\33[m.
O maior Valor foi \33[1:35m{}\33[m e o menor \33[1:35m{}\33[m'''.format(soma, digitados, maior, menor))
print('-'*40, ' / / ', 40*'-')
print(' '*30, 'FINAL DOS EXERCÍCIOS')
print('-'*40, ' / / ', 40*'-')