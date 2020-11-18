from random import randint
nome = str(input('Qual é o seu nome? ')).title().split()
if nome[0] == 'Wellington':
    print('Que nome bonito!')
elif nome[0] == 'Ana':
    print('Seu nome é muito comum no Brasil')
else:
    print('Seu nome é normal')
print('Tenha um bom dia {}'.format(nome))
print('-'*30, '//', '-'*30)
print('\nExercício 36')
#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = int(input('Qual é o valor da casa? '))
salario = int(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos pretende pagar? '))
prestacao = casa/(12*anos)
if prestacao > salario*0.3:
    resposta = ('negado!')
else:
    resposta = ('consedido!')

print('Valor máximo da prestação R${}. Logo o empréstimo foi {}, devido a prestação de R${:.2f}/mês'.format(salario*0.3, resposta, prestacao))
print('-'*30, '//', '-'*30)
print('Exercício 37')
#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

i = randint(0, 1000)
conversao = int(input('Escolha uma base de conversão para o número aleatório\n1 para binário\n2 para octal\n3 para hexadecimal.\n'))
if conversao == 1:
    formato = 'Binário'
    n = bin(i)
elif conversao ==2:
    formato = 'Octal'
    n = oct(i)
else:
    formato = 'Hexadecimal'
    n = hex(i)
print('Número aleatório decimal: {}\nconvertido pra {} é {}'.format(i, formato, n[2:]))

print('-'*20, '/', '-'*20)
print('Exercício 38')
'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
valor1 = int(input('Primeiro valor inteiro: '))
valor2 = int(input('Segundo valor inteiro: '))
if valor1 > valor2:
    print('O primeiro valor é maior')
elif valor1 < valor2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')

print('-'*30, '//', '-'*30)
print('Exercício 39')
#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
nascimento = int(input('Qualo ano o jovem nasceu? '))
idade = 2020 - nascimento
alistamento = 18 + nascimento
if idade > 18:
    print('Você deveria ter se alisatado em {}, logo está atrasado em {} anos'.format(alistamento, 2020 - alistamento))
elif idade < 18:
    print('Você deverá se alistar em {}, faltam ainda {} anos'.format(alistamento, alistamento - 2020))
else:
    print('Você deve se alistar este ano, pois você tem ou completa 18 anos este ano')
print('-'*30, '//', '-'*30)

print('Exercício 40')
'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
n1 = float(input('Primeira Prova: '))
n2 = float(input('Segunda Prova: '))
media = ((n1+n2)/2)
if media >= 7:
    mensagem = 'Aprovado'
elif media < 5:
    mensagem = 'Reprovado'
else:
    mensagem = 'Recuperação'
print('A média foi {}. Logo o aluno está {}'.format(media, mensagem))

print('-'*30, '//', '-'*30)
print('Exencício 41')
'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
bday = int(input('Qual ano o atleta nasceu? '))
id = 2020 - bday
if id < 9:
    categoria = 'Mirim'
elif id<14:
    categoria = 'Infantil'
elif id < 19:
    categoria = 'Junior'
elif id < 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print('O atleta tem {} anos, portanto pertence a categoria {}'.format(id, categoria))

print('-'*30, '//', '-'*30)

print('Exercício 43')

'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''
peso = int(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura em cm? '))
altura = altura/100
imc = peso/(altura**2)
if imc < 18.5:
    retorno = 'abaixo do Peso'
elif imc < 25:
    retorno = 'no peso ideal'
elif imc < 30:
    retorno = 'com sobrepeso'
elif imc < 40:
    retorno = 'na obesidade. Tome cuidado!'
else:
    retorno = 'co obesidade mórbida. Procure a ajuda de um médico imdeiatamente!'
print('O IMC é {:.2f} e o você está {}'.format(imc, retorno))

print('-'*30, '//', '-'*30)
print('Exercício 44')
'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
pagamento = str(input('''Qual será o tipo de pagamento:
(a) à vista dinheiro/cheque
(b) à vista no cartão
(c) em até 2x no cartão
(d) 3x ou mais no cartão\n''')).lower().strip()
custo = float(input('Quanto custa? '))
if pagamento == 'a':
    pagar = custo*0.9
elif pagamento == 'b':
    pagar = custo*0.95
elif pagamento == 'c':
    pagar = custo
else:
    pagar = custo*1.2
print('Valor a ser pago é {}'.format(pagar))

print('-'*30, '//', '-'*30)

print('Exercício 45')
#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
jokenpo = ('Pedar' , 'Papel', 'Tesoura')
pc = randint(0, 2)
jogador = int(input('''Sua escolha:
[0] Pedra:
[1] Pepal:
[2] Tesoura\n\n'''))
if jogador == 0: #pedra
    if pc == 0:
        resultado = 'Empate, sem vencedores'
    elif pc == 1:
        resultado = 'O vencedor foi o computador'
    else:
        resultado = 'O vencedor foi o jogador'

elif jogador ==1: #papel
    if pc == 0:
        resultado = 'O vencedor foi o jogador'
    elif pc == 1:
        resultado = 'Empate, sem vencedores'
    else:
        resultado = 'O vencedor foi o computador'
else: #tesoura
    if pc == 0:
        resultado = 'O vencedor foi o computador'
    elif pc == 1:
        resultado = 'O vencedor foi o jogador'
    else:
        resultado = 'Empate, sem vencedores'

print('{}. Pois o jogador escolheu {} e o computador escolheu {}'.format(resultado, jokenpo[jogador], jokenpo[pc]))

