#bibliotecas globais
from uteis import numeros, strings
import moeda
#aula
strings.finalizacaoCapitulo('INÍCIO DA AULA 22')
#exemplo de fatorial
num = int(input('Digite um número inteiro: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é \033[1;32m{fat}\033[m')
print(f'O dobro do número {num} é \033[1;32m{numeros.dobro(num)}\033[m e o triplo é \033[1;32m{numeros.triplo(num)}\033[m')
strings.finalizacaoCapitulo('Exercício Python 107, 108, 109 e 110')
#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções
#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
#Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
valor = moeda.leiaValor('Digite o valor: R$ ')
aMais = moeda.acrescentar('Deseja acrescentar um valor? ')
aMenos = moeda.reduzir('Deseja reduzir em percentual? ')
formatar = moeda.formatar('Deseja formatar o dado? ')
moeda.resumo(valor,aMais, aMenos, formatar)