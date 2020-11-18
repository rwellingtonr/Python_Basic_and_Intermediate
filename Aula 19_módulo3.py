#bibliotecas
from time import sleep
from random import randint
from operator import itemgetter
from babel.numbers import format_decimal, format_currency
from datetime import datetime
#aula
print('-+'*40)
print(' '*30, 'AULA 19')
print('-+'*40)
pessoas = {
    'nome': 'Wellington leardini ramos',
    'idade': 25, 'sexo': 'Masculino',
    'cidadania': 'Brasileira'
}
print(pessoas['nome'])
print(f'\033[1;31mO {pessoas["nome"]} tem {pessoas["idade"]} anos de idade\033[m')
print('-'*60)
print(pessoas.values())
print('-'*60)
print(pessoas.keys())
print('-'*60)
print(pessoas.items())
print('-'*60)
#deletando elemento
del pessoas['sexo']
#modificando dicionário
pessoas['nome'] = 'Wellington'
#adicionando valores
pessoas['peso'] = 80
for k,v in pessoas.items():
    print(f'{k} = {str(v).title()}')
print('-'*40)
#lista composta com dicionário
brasil = []
estado1 = {'UF': 'São Paulo', 'sigle': 'SP'}
estado2 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['UF'])
print('-'*40)
#Inserção automatizada dos valores de dicionários as listas
linguagem = dict()
programacao = list()
for p in range(3):
    linguagem['linguagem'] = str(input('Uma linguagem de programação: '))
    linguagem['extensao']  = str(input('qual a extensão: '))
    programacao.append(linguagem.copy())
print(programacao)
#for para a lista
for p1 in programacao:
    #for o dicionário
    for a, b in p1.items():
        print(f'O campo \33[32m{a}\33[m tem o valor \33[32m{b}\33[m')
    for vl in p1.values():
        print(vl, end= ' ')
    print()
#Lista de Exercícios
print('-+'*40)
print(' '*30, 'INÍCIO DOS EXERCÍCIOS')
print('-+'*40)
#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict ()
situacao = ' '
aluno['Nome'] = str(input('Nome do aluno: ')).title()
aluno['Nota'] = float(input(f'Nota do {aluno["Nome"]}: '))
if aluno['Nota'] < 7:
    situacao = 'Recuperação'
elif aluno['Nota'] < 5:
    situacao = 'Reprovado'
else:
    situacao = 'Aprovado'
aluno['Situacao'] = situacao
for a90, b90 in aluno.items():
    print(f'{a90} = {b90}')
print('-+'*40)
#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
print('EXERCÍCIO 091')
ranking = list()
jogadores = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(' '*12, f'{"== Resultado dos Jogos =="}')
for jg, nm in enumerate(ranking):
    print(f'{jg+1}º classificado foi o {nm[0]} e tirou no dado o valor {nm[1]}')
    sleep(0.4)
sleep(1)
print('\33[36m=\33[m'*80)
#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
print('Exercício Python 092')
dados_pessoais = {'nome': str(input('Nome: ')).title(),
                  'nascimento': int(input('Ano de nascimento: ')),
                  'clt': format_decimal(input('Digite o número da CLT (caso nulo, digite 0): '), locale='pt_BR')
}
dados_pessoais['idade'] = datetime.now().year - dados_pessoais['nascimento']
if dados_pessoais["clt"] != 0:
    dados_pessoais['contratacao'] = int(input(f'Em qual ano {dados_pessoais["nome"]} teve sua CLT assinada pela primeira vez? '))
    dados_pessoais['salario'] = int(input('Qual é o salário: R$ '))
    dados_pessoais['salario'] = format_currency(dados_pessoais['salario'], 'R$', locale='pt_BR')
    dados_pessoais['aposentadoria'] = (dados_pessoais['contratacao'] - dados_pessoais['nascimento'] + 35)
for ct, ps in dados_pessoais.items():
    print(f' - {str(ct).title()} = \33[92m{ps}\33[m')
sleep(1)
print('Exercício Python 093')
print('\33[36m=\33[m'*80)
#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {
    'nome': input('Nome do jogador: '),
    'partidas': int(input('Quantas partidas ele jogou? '))
}
gols = []
total93 = 0
for p93 in range(jogador['partidas']):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {p93+1}ª partida: ')))
    jogador['gols'] = gols[:]
total93 = sum(gols)
jogador['total'] = total93
print('-='*50)
print(jogador)
print('-='*50)
for nml, ml in jogador.items():
    print(f'O campo {nml} tem o valor: {ml}')
print('-='*50)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for pt, gl in enumerate(gols):
    print(f'      ==> Na {1+pt}ª partida, {jogador["nome"]} fez {gl} gols.')
print('-='*50)
sleep(1)
#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
print('Exercício Python 094')
lista94 = list()
dadosPessoais = dict()
continuar94 = ' '
soma94 = media94 = 0
mulheres = []
while continuar94 not in 'Nn':
    dadosPessoais['nome'] = input('Nome: ').title()
    while True:
        dadosPessoais['sexo'] = input('Sexo (M/F): ').upper()[0]
        if dadosPessoais['sexo'] not in 'MF':
            print('Erro 123 >> Problemas ao identidicar o sexo, favor defina o sexo como masculino (M) ou feminino (F)!')
        else:
            break
    if dadosPessoais['sexo'] == 'M':
        dadosPessoais['sexo'] = 'Masculino'
    else:
        dadosPessoais['sexo'] = 'Feminino'
        mulheres.append(dadosPessoais.copy()['nome'])
    dadosPessoais['idade'] = int(input(f'Qual a idade de {dadosPessoais["nome"]}: '))
    soma94 += dadosPessoais['idade']
    lista94.append(dadosPessoais.copy())
    dadosPessoais.clear()
    while True:
        continuar94 = input('Deseja continuar [S/N]: ')[0]
        if continuar94 in 'SsnN':
            break
        else:
            print('Erro 456 >> Problemas para identificar se precisa continuar ou não!')
media94 = soma94/len(lista94)
print(f'{"Processando os dados...": >10}')
sleep(1)
print('='*80)
'''A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
print(f'A) Quantas pessoas foram cadastradas?', f'\033[32m\n{len(lista94)} pessoas foram cadastradas no sistema\033[m' if len(lista94) > 1 else f'\n\033[32m{len(lista94)} pessoa foi cadastrada no sistema\033[m')
print(f'B) A média de idade.\n\033[32mA média de idade é de {str(media94).replace("." , ",")} anos\033[m')
print(f'C) Uma lista com as mulheres: ')
for mm in mulheres:
    print(f'\033[32m{mm: >5}\033[m')
print(f'D) Uma lista de pessoas com idade acima da média.')
for p94 in lista94:
    if p94['idade'] >= media94:
        print(f'\033[32m{p94["nome"]: >5}: {p94["idade"]}\033[m')
print('='*80)
sleep(1)
#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
gols = []
consolidado9 = []
total93 = 0
continuarSN = contN = ' '
while continuarSN not in 'Nn':
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ').title()
    jogador['partidas'] = int(input('Quantas partidas ele jogou? '))
    for p93 in range(jogador['partidas']):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {p93+1}ª partida: ')))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
        jogador['codigo'] = randint(100, 999)
    gols.clear()
    consolidado9.append(jogador.copy())
    while True:
        continuarSN = input('Deseja continuar [S/N]? ')[0]
        if continuarSN in 'SnsN':
            break
        else:
            print('Erro 757 >> falha ao identificar a ação!')
print('-='*50)
#cabeçalho
print('\033[1;47mNo.', end=' | ')
for jog in jogador.keys():
    print(f'{str(jog).title():^15}' , end=' | ')
print('\033[m')
for k95, v95 in enumerate(consolidado9): #informação dos jogadores
    print(f'{k95:^3}', end=' | ')
    for vv in v95.values():
        print(f'{str(vv):^15}', end= ' | ')
    sleep(1)
    print()
#pesquisa por código de jogador
while contN not in 'Nn':
    atleta = int(input('Qual o jogador você deseja analisar (favor, digite o código)? '))
    for at in consolidado9:
        if at['codigo'] == atleta:
            print(f'Partidas: {str(at["partidas"]):^15}')
            print(f'Gols: {str(at["gols"]):^15}')
        else:
            print('Código não cadastrado')
    while True:
        contN = str(input('Deseja analisar outro jogador? (S/N) '))[0]
        if contN in 'SsNn':
            break
        else:
            print('Erro 757 >> falha ao identificar a ação!')
print('Programa Finalizado!')
print('xX'*30)
print('Final da Aula 19!')

