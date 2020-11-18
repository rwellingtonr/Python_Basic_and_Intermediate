n = int(input('Digite um número de início: '))
f = int(input('Digite um número para o fim: '))
p =  int(input('Digite o passo: '))
for c in range(n, f+p, p):
    print(c)
print('Fim')
print('-'*40, ' / / ', '-'*40)
#somatória
s = 0
for j in range(0, 4):
    m = int(input('Digite um número: '))
    s += m
print('O somatório foi: {}'.format(s))
