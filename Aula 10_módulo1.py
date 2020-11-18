dash = 60
from random import randint
carro = int(input("quantos anos tem o seu carro? "))
print('O carro tem {} anos,'.format(carro))
print('Carro novo' if carro <=10 else 'Carro velho')
print('-='*dash)
print('Exercicio 28')
#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

numero = randint(0, 5)
user = int(input('Qual número o computador pensou de 0 a 5? '))
print('O computador pensou no número: {} e o usuário pensou no número: {}'.format(numero, user), '. Então o usuário:', 'Acertou' if numero == user else 'Errou')
print('-='*dash)
print('Exercicio 29')
#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado! E a multa é de R${}'.format(multa))
else:
    print('A velocidade máxima é 80km/h e você está a {}km/h'.format(velocidade))
print('-='*dash)
print('Exercício 30')
#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('Par' if (numero % 2 == 0) else'Impar')
print('-='*dash)
print('Exercício 31')
#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até dash0Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual é a distancia da viagem em Km? '))
if distancia <200:
    print('O valor da víagem é: R$ {}'.format(distancia*0.5))
else:
    print('O valor da viagem é: R$ {}'.format(distancia*0.45))
print('-='*dash)
print('Exercício 32')
#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano: '))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 ==0):
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))

print('-='*dash)
print('Exercício 33')
#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Entre com o primeiro numero: '))
n2 = int(input('Entre com o segundo numero: '))
n3 = int(input('Entre com o terceiro numero: '))
menor = n1
maior = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
print('-='*dash)
print('Exercício 34')
#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salário: R$'))
if salario > 1250:
    reajuste = 0.1*salario
else:
    reajuste = 0.15*salario
salario = reajuste + salario
print('Seu salário teve um aumento de R${}. Agora, seu novo salário é R${}'.format(reajuste, salario))
print('-='*dash)
print('Exercício 35')
#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))
if (s1 < s2 + s3)and(s2 < s1+s3)and(s3< s1+s2):
    resposta = 'Sim'
    if s1 == s2 == s3:
        tipo = 'Equilátero'
    elif s1 != s2 != s3:
        tipo = 'Escaleno'
    else:
        tipo = 'Isóceles'
else:
    resposta = 'Não'
'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

print('Os segmentos são capazes de formar um triangulo? {}.\nE qual tipo de triangulo? {}'.format(resposta, tipo))
print('-='*dash,'\nFinal do Módulo 1')
