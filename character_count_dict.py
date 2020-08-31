def contar_caracteres(s):
    """
    Funcao que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('Raphael')
    {'a': 1, 'h': 1, 'l': 1, 'p': 1, 'r': 1}
    >>> contar_caracteres('Renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}


    :param s: string a ser contada
    """

    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem
        # ou pode se usar
        # resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('Raphael'))
    print()
    print(contar_caracteres('Renzo'))
