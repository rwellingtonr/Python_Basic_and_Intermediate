#importação de módulos

from math import floor, sqrt
num = int(input("Digite um número: "))
raiz = sqrt(num)

print("A raiz de {} é {}".format(num, floor(raiz)))
