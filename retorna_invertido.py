"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721."""


def retornaInvertido(valor):
    return valor[::-1]

numero = input('Informe um numero:')
print(retornaInvertido(numero))
