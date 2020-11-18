nome = input('Qual o seu nome? ')
print('Prazer: {:=^20}!'.format(nome))
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
s = n1 + n2
d = n1/n2
multiplicacao =  n1 * n2
div =  n1//n2
resto = n1%n2
potencia = n1**n2
#.3f deixa com apenas 3 números após a virgula
#\n quebra a linha
print('Números inserido {} e {}.\n Valores de soma {},\n divisão {:.3f},\n divisão parcial {:},\n resto {} ,\n potência {:.2f}'.format(n1, n2, s, d, div, resto, potencia))