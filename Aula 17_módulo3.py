#Bibliotecas
from time import sleep
#Aula 17
print('='*80)
print(' '*20, 'AULA 17 - Manupulação de Listas')
print('='*80)
num = [0, 1, 2, 3]
print(num)
num[2] = 7
print(num, '- Trocado o 2 pelo 7')
num.append(9)
print(num, '- Adicionado o número 9')
num.insert(1, 10)
print(num, '- Adicionado o número 10 na 1ª posição')
print(f'O comprimento da lista é: {len(num)}')
num.sort()
print('Ordem crescente: ',num)
num.sort(reverse= True)
print('Ordem decescente: ',num)
num.pop()
print('Excluido o ultimo valor da lista: ', num)
num.remove(10)
print('Removido o número 10: ', num)
#Exemplo 2 - Lista em colunas
print('\33[36m=\33[m'*80)
valores = list(range(1,5))
for v in valores:
    print(f'O valor é: {v}')
for c, v2 in enumerate(valores):
    print(f'Na {c+1}ª posição, está o valor: {v2}')
print('Final da Lista')
#Exemplo 3 - Entrada de dados pelo teclado
print('\33[36m=\33[m'*80)
numeros = list((int(input('Valor: ')))for count in range(3))
print(numeros)
#Exemplo 4 Ligação entre listas
print('\33[36m=\33[m'*80)
print('Ligação entre listas')
a = [2, 4, 6, 8]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 3
print('\33[1:31mSubstituido o 2º valor na lista B para o valor 3 e com isso também mudou na lista A, pois elas estão entrelaçadas!\33[m')
print(f'\33[32mLista A: {a}\33[m')
print(f'\33[32mLista B: {b}\33[m')
#Exemplo 5 Cópia entre listas
print('\33[36m=\33[m'*80)
print('Cópia entre listas')
b = a[:] #por este parâmetro ele apenas cria uma cópia
a[2] = 6
print(f'\33[35mLista A: {a}\33[m')
print(f'\33[35mLista B: {b}\33[m')
print('='*80)
print(' '*20, 'INÍCIO DOS EXERCÍCIOS')
print('='*80, '\nExercício Python 078')
#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.maior = menor = maior_posicao = menor_posicao = 0
valuer = []
maior = menor = 0
for val in range (5):
    valuer.append(int(input(f'Digite um valor para {val+1} posição: ')))
    if val == 0:
        menor = maior = valuer[val]
    else:
        if valuer[val] > maior:
            maior = valuer[val]
        if valuer[val] < menor:
            menor = valuer[val]
print(f'\33[32mO maior valor digitado foi: {maior} e está na  posição: \33[m')
for i , val1 in enumerate(valuer):
    if val1 == maior:
        print(f'{i+1};', end= ' ')
print(f'\n\33[32mO menor valor digitado foi: {menor} e está na posição: \33[m')
for i, val1 in enumerate(valuer):
    if val1 == menor:
        print(f'{i+1};', end= ' ')
sleep(1)
print('\nExercício Python 079')
#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
v_valores = []
resposta = ' '
while resposta not in 'Nn':
    val_v = int(input('Digite um valor: '))
    if val_v not in v_valores:
        v_valores.append(val_v)
    else:
        print('Número já adicionado!')
        resposta = str(input('Deseja continuar [S/N]: ')).strip()
v_valores.sort()
print(f'\33[1m Números em ordem crescente:\33[m')
print('-'*30)
for num78 in range(0,len(v_valores)):
    print(f'\33[34m{num78+1:}ª posição o valor:\33[m \33[31m{v_valores[num78]:>5}\33[m')
print('-'*30)
sleep(1)
print('Exercício Python 080')
#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
entrada_l = list()
for py80 in range(5):
    num80 = int(input('Digite um número inteiro: '))
    if (py80 == 0) or (num80 > entrada_l[-1]):
        entrada_l.append(num80)
    else:
        pos80 = 0
        while pos80 < len(entrada_l):
            if num80 <= entrada_l[pos80]:
                entrada_l.insert(pos80, num80)
                break
            pos80 += 1
print(f'Números em ordem crescente: {entrada_l}')
sleep(1)
print('Exercício Python 081:')
'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
valores81 = list()
desejo = ' '
while desejo not in 'nN':
    valores81.append(int(input('Digite um valor: ')))
    desejo = str(input('Deseja continuar dititando valores? ')).strip()[0]
    if 5 in valores81:
        cinco = 'Sim'
    else:
        cinco = 'Não'
valores81.sort(reverse= True)
print(f'A) Quantidade de números digitados foi de: {len(valores81)}')
print(f'B) Lista em ordem decrescente:\n{valores81}')
print(f'O número 5 aparece na lista? {cinco}')
sleep(1)
print('Exercício Python 082')
#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista_c = list(int(input('Digite um número: '))for completa in range(3))
lista_par = []
lista_impar = []
for lista82 in range(0,len(lista_c)):
    if lista_c[lista82] % 2 == 0:
        lista_par.append(lista_c[lista82])
    else:
        lista_impar.append(lista_c[lista82])
print(f'Todos os números digitados:\n\33[32m{lista_c}\33[m')
print(f'Número pares digitados:\n\33[31m{lista_par}\33[m')
print(f'Números impares digitados:\n\33[34m{lista_impar}\33[m')
sleep(1)
print('Exercício Python 083sudo')
#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input('Digite uma expressão aritimética:\n')).strip()
if expressao.count('(') == expressao.count(')'):
    print('\033[1;42mSua expressão está correta!\33[m')
else:
    print('\033[1;101m Sua expressão está errada!\33[m')
sleep(1)
'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
print('Exercício Python 084')
nome_peso = list()
definitivo = []
c84 = menor = maior = 0
print('Início das pesquisas')
while True:
    nome_peso.append(str(input('Digite o seu nome: ')).strip().title())
    nome_peso.append(float(input('Qual é o seu peso? ')))
    if len(definitivo) == 0:
        maior = menor = nome_peso[1]
    else:
        if nome_peso[1] > maior:
            maior = nome_peso[1]
        if nome_peso[1] < menor:
            menor = nome_peso[1]
    definitivo.append(nome_peso[:])
    nome_peso.clear()
    continuacao = ' '
    while continuacao not in 'SsnN':
        continuacao = str(input('Deseja continuar? '))[0]
    if continuacao in 'Nn':
        print('Compilando os dados:')
        for contador84 in range(50):
            print('\033[1;42m ', end=' ')
            sleep(0.05)
            c84 += 1
        print('\n\33[mDados Compilados!')
        break
print(f'A) Quantas pessoas foram cadastradas?\n\033[1;32mForam cadastradas {len(definitivo)} pessoas\033[m')
print(f'B) Uma listagem com as pessoas mais pesadas:\n\033[1;32mO maior peso cadastrado foi: {maior} Kg\033[m')
for d84 in definitivo:
    if d84[1] == maior:
        print(f'- {d84[0]}')
print(f'\nC) Uma listagem com as pessoas mais leves:\n\033[1;32mO menor peso cadastrado foi: {menor} Kg\033[m')
for d84 in definitivo:
    if d84[1] == menor:
        print(f'- {d84[0]}')
print('\n', '-'*50)