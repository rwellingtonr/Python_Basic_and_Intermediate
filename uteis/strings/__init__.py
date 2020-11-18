#def padrao
def finalizacaoCapitulo(txt):
    from time import sleep
    sleep(0.6)
    print('\033[1;101m', '~' * (len(txt) + 8),'\033[m' )
    print('\033[1;101m', f'   {txt}', '     \033[m')
    print('\033[1;101m', '~' * (len(txt) + 8),'\033[m' )