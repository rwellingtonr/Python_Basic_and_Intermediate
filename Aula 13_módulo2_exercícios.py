#Bicliotecas a serem importadas
from time import sleep
print('='*90,'\n', ' '*30,'INÍCIO DOS EXERCÍCIOS')
print('='*90,'\nExercício Python 046')
#Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
for fogos in range(10, 0, -1):
    print(fogos)
    sleep(1) #função sleep acrescenta um delay ao sistema
print('BUMM! '*5)
print('-'*40, ' / / ', 40*'-', '\nExercício Python 047')
#Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for par in range(1, 50+1):
    if par %2 == 0:
        print(par)

print('-'*40, ' / / ', 40*'-','\nExercício Python 048')
#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
for soma in range(0, 501):
    if soma %3 ==0:
        print(soma)
        s += soma
print('A somatória dos valores é: ', s)
print('-'*40, ' / / ', 40*'-','\nExercício Python 049')
#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número para fazer a tabuada: '))
for t in range(0, 11):
    print('{} x {} = {}'.format(num, t, num*t))
print('-'*40, ' / / ', 40*'-','\nExercício Python 050')
#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
e = 0
for p in range(0, 7):
    m = int(input('Digite um número: '))
    if m % 2 ==0:
        e += m
print('O valor da somatória é: ', e)

print('-'*40, ' / / ', 40*'-','\nExercício Python 051')
#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('O primeiro número: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + 10 * razao
for b in range(primeiro, decimo, razao):
    print('{} '.format(b), end='-> ')
print('FIM.')
print('-'*40, ' / / ', 40*'-','\nExercício Python 052')
#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
primo = int(input('Verifique se o número é primo: '))
total = 0
for o in range(1, primo+1):
    if primo % o == 0:
        print('\33[1:31m', o,end=' ')
        total += 1
    else:
        print('\33[m', o,end=' ')
if total < 3:
    ç = 'é número primo'
else:
    ç = 'não é número primo'
print('\n\33[mO número {} foi dividido {} vezes por isso ele {}'.format(primo, total, ç))

print('-'*40, ' / / ', 40*'-','\nExercício Python 053')
#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Escreva uma frase:\n')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''
for letra in range(len(juntos) - 1, -1, -1):
    inverso += juntos[letra]
if juntos == inverso:
    z = 'é um palíndromo'
else:
    z = 'não é palíndromo'
print('Frase digitada {}\nFrase: {}'.format(z, frase))
print(juntos, '------',inverso)

print('-'*40, ' / / ', 40*'-','\nExercício Python 054')
#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maiores = 0
menores = 0
for pessoas in range(0, 7):
    nascimento = int(input('Data de nascimento: '))
    if (2020 - nascimento) >= 18:
        maiores += 1
    else:
        menores +=1
print('Num grupo de 7 pessoas {} são maiores de idade e {} são menores de idade'.format(maiores, menores))
print('-'*40, ' / / ', 40*'-','\nExercício Python 055')
#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesado = 0
leve = 0
for a in range(1, 6):
    peso = float(input('O peso da {}º pessoa é: '.format(a)))
    if a ==1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
print('O mais pesado tem {}Kg\nO mais leve tem {}Kg'.format(pesado, leve))

print('-'*40, ' / / ', 40*'-','\nExercício Python 056')
#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
id = 0
media = 0
velho = 0
nome_homem_mais_velho = ''
mulher20 = 0
mulherx = 0
for g in range(1, 5):
    print('--------- {}ª Pessoa ---------'.format(g))
    nome = str(input('Nome da {}ª pessoa: '.format(g))).strip().title()
    sexo = str(input('Sexo (Masculino ou Feminino): ')).strip().lower()
    idade = int(input('Idade: '))
    id += idade
    if g == 1 and sexo == 'masculino' :
        nome_homem_mais_velho = nome
        velho = idade
    if sexo == 'masculino' and idade > velho:
        nome_homem_mais_velho = nome
        velho = idade
    if sexo == 'feminino' and idade < 20:
        mulher20 += 1
    if sexo == 'feminino' and idade >= 20:
        mulherx += 1

media = id/4
print('O nome do homem mais velho é {} e ele tem {} anos'.format(nome_homem_mais_velho, velho))
print('A média de idade do grupo entrevistado é: {}'.format(media))
print('O grupo tem {} mulheres com menos de 20 anos e {} maiores de 20'.format(mulher20, mulherx))

print('='*90,'\n', ' '*30,'FINAL DOS EXERCÍCIOS')
print('='*90)