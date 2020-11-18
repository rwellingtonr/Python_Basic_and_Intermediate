#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções
from babel.numbers import format_currency

def leiaValor(txt):
    valido = False
    while not valido:
        valor = str(input(txt)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'O valor digitado \33[1;31m<{valor}>\33[m é invalido')
        else:
            valido = True
            return float(valor)

def acrescentar(msg):
    verificacao = str(input(msg))
    if verificacao in 'sS':
        valor = float(input('Quantos por cento deseja acrescentar? '))
    else:
        valor = 0
    return valor

def reduzir(e):
    validacao = str(input(e))
    if validacao in 'Ss':
        reduzido = float(input('Quantos por cento deseja reduzir? '))
    else:
        reduzido = 0
    return reduzido

def formatar(s):
    from time import sleep
    validacao = False
    while not validacao:
        formatacao = str(input(s)).strip()[0]
        if formatacao in 'SsnN':
            print('Computando os dados...')
            sleep(1)
            validacao = True
        else:
            print('Comando inválido!')
    return formatacao




def aumentar(v, c, f = False):
    if f == 's':
        aum = format_currency((v * ((100 + c) / 100)), "R$", locale="pt_BR")
    else:
        aum = v
    return  aum


def dinimuir(v, p, f = False):
    if f == 's':
        dim = format_currency((v * ((100 - p) / 100)), "R$", locale="pt_BR")
    else:
        dim = v
    return dim


def dobro(v, f = False):
    if f == 's':
        dobrado = format_currency((v * 2), "R$", locale="pt_BR")
    else:
        dobrado = v
    return dobrado


def metade(v, f = False):
    if f == 's':
        meia = format_currency((v / 2), "R$", locale="pt_BR")
    else:
        meia = v
    return meia

def resumo(v, c , p , f):
    print(f'O valor informado foi: \t\033[1;36m{str(v).replace(".", ",")}\033[m')
    print(f'O dobro é: \t\033[1;32m{dobro(v, f)}\033[m')
    print(f'A metade do valor é: \t\033[1;31m{metade(v, f)}\033[m')
    if c != 0:
        print(f'A {c:.3f}% a mais no valor é: \t\033[1;32m{aumentar(v, c, f)}\033[m')
    if p != 0:
        print(f'A {p:.3f}% a menos no valor é: \t\033[1;31m{dinimuir(v, p, f)}\033[m')

