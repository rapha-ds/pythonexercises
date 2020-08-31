"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."""


def qtdDigitos(digit):
    if digit == 0:
        return 0
    return 1 + qtdDigitos(digit // 10)

# Fluxo Principal
digito = int(input('Informe um numero inteiro:'))
print('O numero %d possui %d digitos.' % (digito, qtdDigitos(digito)))

