#Tratamentos e manipulações de cadeias de texto
frase = 'Curso em Vídeo Python'
dividido = (frase.split())
print(dividido[0][0])
print('Exercício Python 022')

'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''
print('Exercício 23')
#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
import random
numero = random.randint(0, 9999)
u = numero //1 %10
d = numero //10 %10
c = numero //100 %10
m = numero //1000 %10
print('numero {}, unidade {} , Dezena: {}, centena {}, milhar {}'.format(numero, u, d, c, m))
print('Exercício 24')

#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome da cidade: ')).strip().upper()
print('A cidade começa com o nome de Santo?\n{}'.format(cidade[:5]=='SANTO'))

print('Exercício 26')
#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
fr = str(input('Digite uma frase: ')).strip().capitalize()
print('Frase:\n{}\nQuantidade de letras "a": {}'.format(fr, fr.count('a')))

print('Exercício 27')
#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.
nome = str(input('Digite o nome completo: ')).split()
print('Primeiro nome: {}\nUltimo nome: {}'.format(nome[0], nome[-1]))




