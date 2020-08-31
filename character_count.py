
def contar_caracteres(s):
    """
    Funcao que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('Raphael')
    a: 2
    h: 1
    l: 1
    p: 1
    r: 1
    >>> contar_caracteres('Renzo')
    e: 1
    n: 1
    o: 1
    r: 1
    z: 1


    :param s: string a ser contada
    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('Raphael')
    print()
    contar_caracteres('Renzo')

