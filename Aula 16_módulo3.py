#TUPLAS
#Bibliotecas
from time import sleep
from random import randint
print('=='*60)
print(' '*40,'INÍCIO DA AULA')
print('=='*60)
sleep(1)
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[1:])
print(sorted(lanche))#mostra ordenado
print(40*'\33[35m/\ \33[m')
#for c in range(0, len(lanche)):
#    print(lanche[c])

#desta forma ele numera os elementos dentro de lanche, possibilitando mostrar a posição
for pos, comida in enumerate(lanche):
    print(f'\33[1:32mEu quero {comida} na posição {pos}\33[m')
print('Comi bastante!')
print(40*'\33[35m/\ \33[m')
a = 2, 4, 6, 8
b = 1, 3, 5, 7
c = a + b
print(f'Variável desordenada: {c}\nOrdenada: {sorted(c)}\nO tamanho de é {len(c)} elementos\nE quantos vezes o número 5 aparece: {c.count(5)}')
print(40*'\33[35m/\ \33[m')
pessoa = 'Wellington', 22, 'Masculino', 78
#unico jeito de apagar algo é utilizar o comando del
print(f'''Nome: {pessoa[0]}
Idade: {pessoa[1]}
Sexo: {pessoa[2]}
Peso: {pessoa[3]}''')
sleep(2)
print('=='*60)
print(' '*40,'INÍCIO DOS EXERCÍCIOS')
print('=='*60)
print('\nExercício Python 072')
#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numero = 'zero' , 'um', 'dois' , 'tres', 'quatro', 'cinco', 'seix', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseix', 'dezesete', 'dezoito', 'dezenove' , 'vinte'
print('Para encerrar o programa digite um valor maior que 20')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20:
        print('Programa finalizado!')
        break
    else:
        print(f'O número \33[32m{num}\33[m por extenso é: \33[32m{numero[num]}\33[m')
sleep(1)
print(40*'\33[35m/\ \33[m','\nExercício Python 073')
'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
times = 'Flamengo','Santos','Palmeiras', 'Grêmio', 'Athletico', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
chapeco = times.index('Chapecoense')
posicao = 0
print('a) Os 5 primeiros times.')
for pos1, team in enumerate(times[:5]):
    print(f'{pos1+1}º = {times[pos1]}')
print('\33[31m- x \33[m'*20,'\nb) Os últimos 4 colocados.')
for pos2, team2 in enumerate(times[16::1]):
    print(f'{pos2 + 17}º = {times[pos2+16]}')
print('\33[31m- x \33[m'*20, '\nc) Times em ordem alfabética.',f'\n{sorted(times)}')
print('\33[31m- x \33[m'*20, f'\nEm que posição está o time da Chapecoense?\nEstá na {chapeco}ª posição')
sleep(1)
print(40*'\33[35m/\ \33[m','\nExercício Python 074')
#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
aleatorio = (randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20) )
for post, ale in enumerate(aleatorio):
    print(f'{numero[ale]}({ale})', end='')
    print(', ' if post < 4 else '. ', end='')
print(f'\nO maior valor sorteado foi: {max(aleatorio)}\nO menor valor foi: {min(aleatorio)}')
sleep(1)
print(40*'\33[35m/\ \33[m','\nExercício Python 075')
'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
valores = tuple(int(input('Digite um valor: '))for var in range(4))
npar = (0, )
num9 = ' '
contpar = 0
for vari in (valores):
    if vari % 2 == 0:
        contpar += 1
        if contpar == 1:
            npar = (vari,)
        elif contpar > 1:
            par = (vari,)
            npar += par
if valores.count(9) > 1:
    num9 = 'vezes'
else:
    num9 = 'vez'
print('A) Quantas vezes apareceu o valor 9?', f'\n\33[32mO número 9 apareceu {valores.count(9)} {num9}\33[m' if valores.count(9) > 0 else'\n\33[32mNão apareceu o número 9\33[m')
print('B) Em que posição foi digitado o primeiro valor 3? ',f'\n\33[32mO número 3 apareceu na posição {valores.index(3)+1}\33[m' if 3 in valores else '\n\33[32mO número 3 não foi encontrado\33[m')
print('C) Quais foram os números pares?', f'\n\33[32mNúmero(s) par(es): {str(npar).strip(",")}.\33[32m' if len(str(npar)) > 4 else '\n\33[32mNão há números pares\33[m')
sleep(1)
print(40*'\33[35m/\ \33[m','\nExercício Python 076')
#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista_mercado = 'Café', 3.50, 'Feijão Branco', 0.80,'Feijão Preto', 0.80,'Grão de Bico', 1,'Tofu', 1.80,'Legumes', 1.50,'Salada', 1.70,'Detergente', 0.85
print('-'*48)
print(' '*14,'LISTA DE COMPRAS')
print('-'*48)
for mer in range (0, len(lista_mercado)):
    if mer % 2 == 0:
        print(f'Produto: \33[34m{lista_mercado[mer]:.<30}\33[m', end=' ')
    else:
        print(f'R$\33[34m {lista_mercado[mer]:>3.2f}\33[m')
print('-'*48)
sleep(1)
print(40*'\33[35m/\ \33[m','\nExercício Python 077')
#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = tuple(str(input('Digite uma palavra (sem acentos): ').lower())for pala in range(5))
print(palavras)
for vog in palavras:
    print(f'\nA palavra: \33[32m{vog:<15} \33[m Vogais: ', end= '')
    for vogais in vog:
        if vogais in 'aeiou':
            print(f' \33[32m{vogais} \33[m;', end=' ')
print('=='*60)
print(' '*40,'FIM DOS EXERCÍCIOS')
print('=='*60)

