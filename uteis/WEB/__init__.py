def url():
    import urllib.request
    try:
        site = urllib.request.urlopen('http://pudim.com.br/')
    except:
        print('\33[1:31mFalha!\33[m\nImpossível de acessar o site no momento!')
    else:
        print('\33[1:32mSucesso!\33[m\nSite funcionando normalmente!')