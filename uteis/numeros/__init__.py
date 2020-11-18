def fatorial (n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f
def dobro(num):
    return num*2
def triplo(num):
    return 3*num

def leiaInt(inteiro):
    while True:
        try:
            numero = int(input(inteiro))
        except (ValueError, TypeError):
            print(f'O valor digitado é inválido, erro: \n\33[1:31mProblema na entrada de dados!\33[m')
            continue
        except KeyboardInterrupt:
            print(f'O valor digitado é inválido, erro: \n\33[1:31mO usuário preferiu não digitar um valor!\33[m')
            continue
        else:
            return numero

def leiaFloat(real):
    while True:
        try:
            nReal = float(input(real))
        except (TypeError, ValueError):
            print(f'O valor digitado é inválido, erro: \n\33[1:31mProblema na entrada de dados!\33[m')
        except KeyboardInterrupt:
            print(f'O valor digitado é inválido, erro: \n\33[1:31mO usuário preferiu não digitar um valor!\33[m')
        else:
            return nReal