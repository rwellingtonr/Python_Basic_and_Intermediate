#Biblioteca
from random import randint
#Funções padrão
def divisor(txt):
    from time import sleep
    print('\033[1;36m=' * 80,'\033[m')
    print(' '*30, txt)
    print('\033[1;36m=' * 80,'\033[m')
    sleep(0.5)

def fatorial(a, show = False):
    f = 1
    for n in range(a, 0, -1):
        if show:
            print(n, end= '')
            if n > 1:
                print(' x ', end= '')
            else:
                print(' = ', end= '')
        f *= n
    return f
#Aula
divisor('INÍCIO DA AULA')
divisor('INTERACTIVE HELP')

#INTERACTIVE HELP
print('lua nova a b c','a s f' ,sep='/')
help(print)
print('-'*40)
print(input.__doc__)
divisor('DOCSTRINGS')
#DOCSTRINGS
def contador(i,f,p):
    """i = inicio da contagem
    f = final da contagem
    p = passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('\nFIM')
contador(0,100,10)
help(contador)
#PARÂMETROS OPCIONAIS
divisor('PARÂMETROS OPCIONAIS')
def somar(a = 0,b = 0,c=0):
    s = a + b + c
    print(f'O valor da soma é {s}')

somar(c = 8,b = 4)
#ESCOPO DE VARIÁVEIS
divisor('ESCOPO DE VARIÁVEIS')
def teste():
    x = 9
    print(f'\033[1;32mDentro do ambiente de teste N vale {n}\033[m')
    print(f'\033[1;32mDentro do ambiente de teste X vale {x}\033[m')

n = 2
teste()
print(f'\033[1;31mDentro do programa N vale {n}\033[m')
divisor('ESCOPO DE VARIÁVEIS 2')
def teste02(b):
    global a
    a = 8
    b += 5
    c = 3
    print(f'\033[1;32mDentro do ambiente de teste A vale {a}\033[m')
    print(f'\033[1;32mDentro do ambiente de teste B vale {b}\033[m')
    print(f'\033[1;32mDentro do ambiente de teste C vale {c}\033[m')


a = 5
teste02(a)
print(f'O valor global de a é {a}')
#RETORNANDO VALORES
divisor('RETORNANDO VALORES')
def somar_02(a = 0,b = 0,c=0):
    s = a + b + c
    return s


r1 = somar_02(randint(1, 10), randint(1, 10), randint(1, 10))
r2 = somar_02(randint(1, 10), randint(1, 10), randint(1, 10))
r3 = somar_02(randint(1, 10))
print(f'A soma do primeiro é \033[1;36m{r1}\033[m;\nA soma do segundo é \033[1;36m{r2}\033[m;\nA soma do terceiro é \033[1;36m{r3}\033[m;\nA soma total é \033[1;36m{r1+r2+r3}\033[m')
divisor('INÍCIO DOS EXERCÍCIOS')
#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
print('Exercício Python 101')
def voto(nascimento):
    from datetime import date
    voto = date.today().year - nascimento
    if voto < 16:
        return f'Com {voto} anos o voto é negado!'
    elif voto < 18 or voto > 65:
        return f'Com {voto} anos o voto é opcional!'
    else:
        return f'Com {voto} anos o voto é obrigatório'


nascimento = int(input('Qual é o ano de nascimento? '))
print(voto(nascimento))
divisor('Exercício Python 102')
#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

while True:
    continuar = input('Deseja continuar? ').lower()[0]
    if continuar == 's':
        fat = int(input('Digite um numero para fatorar: '))
        show = str(input('Deseja ver o passo a passo? ')).lower()[0]
        if show == 's':
            show = True
        else:
            show = False
        print(fatorial(fat, show))
    else:
        break
divisor('Exercício Python 103')
#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome = '', gols = False):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} na partida.')


jogador = str(input('Nome do jogaor: ')).title().strip()
gol = str(input('Quantidade de gols? '))
print(ficha(jogador, gol))
divisor('Exercício Python 104')
#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
def leiaInt(txt):
    valor = 0
    validacao = False
    while True:
        g = str(input(txt))
        if g.isnumeric():
            valor = int(g)
            validacao = True
        else:
            print('Você não digitou um número inteiro')
        if validacao:
            break

g = leiaInt('Digite um número inteiro: ')
divisor('Exercício Python 105')
'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''
def notas(nota = list(), situ = False):
    '''Função que pode receber diversas notas e tem como função informar:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)'''
    escola = {
        'quantidade': len(nota),
        'maior': max(nota),
        'menor': min(nota),
        'média': sum(nota)/len(nota)
    }
    if situ:
        if escola['média'] < 5:
            escola['situacao'] = 'Ruim'
        elif escola['média'] <= 7:
            escola['situacao'] = 'Regular'
        else:
            escola['situacao'] = 'Ótima'
    for e , s in escola.items():
        print(f'===> {str(e).title()}: {s}')


print(help(notas))
alunos = int(input('Quantas notas deseja adicionar? '))
lista = list()
for al in range(alunos):
    lista.append(int(input(f'Digite a {1 + al} nota: ')))
sim_nao = conclusao = ' '
while sim_nao not in 'sn':
    sim_nao = str(input('Deseja mostrar a situação da escola? ')).lower()[0]
if sim_nao == 's':
    conclusao = True
else:
    conclusao = False
notas(lista, conclusao)
divisor('Exercício Python 106')
#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
def ajudinha(t106):
    print('\33[1;46m', end='')
    print(help(t106))
    print('\33[m', end='')

while True:
    funcao = str(input('Digite a função que queira analisar: '))
    if funcao.upper() == 'FIM':
        break
    else:
        ajudinha(funcao)
divisor('FINAL DOS EXERCÍCIOS')
