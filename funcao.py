def nomes(contatos):
    arquivo = open(contatos, 'r')
    contato = arquivo.read()
    arquivo.close()

    contato = contato.replace(' ', '')
    contato = contato.replace('#', ' ')
    contato = contato.replace('--', '\n')

    contato = contato.split()
    galera = dict()

    vdevinganca = ''

    cdecachorro = ''
    lol = 0

    for x in contato:
        if lol %2 == 0:
            vdevinganca = contato[lol]
        else:
            cdecachorro = contato[lol]
            galera[cdecachorro] = vdevinganca
        lol += 1
    return galera
