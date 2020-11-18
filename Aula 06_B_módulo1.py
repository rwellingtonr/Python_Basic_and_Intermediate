n = input('digite algo: ')
print('tipo do valor: {}, é numérico? {}, está em caixa baixa? {}, pode ser impresso? {} ,qual o seu valor {}'.format(
    type(n), n.isnumeric(), n.islower(), n.isprintable(), n))
