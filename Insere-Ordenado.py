def insere(lista_numero, n):
    '''dada uma lista ordenada (crescente) de números inteiros e um 
    número inteiro n, inclua n na posição correta, ou seja, de tal 
    maneira que a lista continue ordenada.'''
    lista = lista_numero
    lista.append(n)
    lista.sort()
    return lista
