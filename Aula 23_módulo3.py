#import
from uteis import strings, numeros, WEB

#Aula 23
strings.finalizacaoCapitulo("INÍCIO AULA 23")
try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    c = a / b
except Exception as erro:
    print(f'Infelizmente houve um erro na divisão, devido a {erro.__class__}')
else:
    print(f'O valor da divisão de {a} por {b} é {c:.1f}')
finally:
    print('Volte sempre!')
strings.finalizacaoCapitulo('Segundo Exemplo')
try:
    d = int(input('Digite o numerador: '))
    e = int(input('Digite o denominador: '))
    f = d / e
except (ValueError, TypeError):
    print('\33[1:32mTivemos problemas com os tipos de dados que você digitou!\33[m')
except (ZeroDivisionError):
    cond = str(input('Não é possivel dividir por zero!\nPosso aplicar limite? ')).lower()[0]
    if cond == 's':
        f = d / 0.00000000001
        print(f'O valor da divisão é: {f:.1f}')
else:
    print(f'O valor da divisão é: {f:.1f}')
finally:
    print('Finalizando o código!')

#Exercícios
    #Exercício 113
strings.finalizacaoCapitulo('Exercício Python 113:') #Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
#entrada de dados
n1 = numeros.leiaInt('Digite um número inteiro: ')
n2 = numeros.leiaFloat('Digite um número dentro da família dos reais: ')
print(f'O número inteiro digitado foi \33[1:32m{n1}\33[m e o real foi \33[1:32m{n2}\33[m')
#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
strings.finalizacaoCapitulo('Exercício Python 114:')
WEB.url()