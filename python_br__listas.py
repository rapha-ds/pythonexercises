"""Lista de Exercicios - Estrutura Sequencial"""
'Faça um Programa que mostre a mensagem "Alo mundo" na tela.'


def ola():
    print('Alo Mundo')


# ---------------------------------------------------------------------------------------------------
'Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].'


def print_number(number):
    print(f'O numero informado foi {number}')


# ---------------------------------------------------------------------------------------------------
'Faça um Programa que peça dois números e imprima a soma.'


def sum_two(number_01, number_02):
    print(number_01 + number_02)


# ---------------------------------------------------------------------------------------------------
'Faça um Programa que peça as 4 notas bimestrais e mostre a média.'


def media_bimestral(number_01=float, number_02=float, number_03=float, number_04=float):
    return (number_01 + number_02 + number_03 + number_04) / 4


# ---------------------------------------------------------------------------------------------------
'Faça um Programa que converta metros para centímetros.'


def conversao_metro_centimetro(number_01):
    return int(number_01 * 100)


# ----------------------------------------------------------------------------------------------------
'Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'


def area_circulo(raio):
    return 3.14 * (raio * raio)


# -----------------------------------------------------------------------------------------------------
'Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'


def area_e_dobro(lado):
    area = lado * lado
    print(f'Area: {area}')
    print()
    print(f'Dobro: {area * 2}')


# ----------------------------------------------------------------------------------------------------
'Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. '
'Calcule e mostre o total do seu salário no referido mês'


def salario_mensal(gph, horas):
    return gph * horas


# ----------------------------------------------------------------------------------------------------
'Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.'
'C = 5 * ((F-32) / 9).'


def f_to_c(value_f):
    value_c = 5 * ((value_f - 32) / 9)
    print(value_c)


# ----------------------------------------------------------------------------------------------------
'Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.'


def c_to_f(value_c):
    value_f = ((value_c * 9) / 5) + 32
    print(value_f)


# ----------------------------------------------------------------------------------------------------
'Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:'
'o produto do dobro do primeiro com metade do segundo .'
'a soma do triplo do primeiro com o terceiro.'
'o terceiro elevado ao cubo.'


def calculo_int_com_float(number_01=int, number_02=int, number_03=float):
    print(f'O produto do dobro primeiro com metade do segundo:\n{(number_01 * 2) * (number_02 / 2)}')
    print()
    print(f'A soma do triplo do primeiro com o terceiro:\n{(number_01 * 3) + number_03}')
    print()
    print(f'O terceiro elevado ao cubo:\n{number_03 ** 3}')


# ---------------------------------------------------------------------------------------------------
'Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,'
' usando a seguinte fórmula: (72.7*altura) - 58'


def peso_ideal(altura=float):
    peso = (72.7 * altura) - 58
    return peso


# ----------------------------------------------------------------------------------------------------
'Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,'
' utilizando as seguintes fórmulas:'
'Para homens: (72.7*h) - 58'
'Para mulheres: (62.1*h) - 44.7'


def peso_ideal_sexos(h):
    print(f'O peso ideal para homens de altura {h}:\n{(72.7 * h) - 58}\n')
    print(f'O peso ideal para mulheres de altura {h}:\n{(62.1 * h) - 44.7}')


# ----------------------------------------------------------------------------------------------------
"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
 de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de
  pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
  João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
   Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa 
   que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""


def multa_peixes(peso):
    if peso >= 50:
        excesso = peso - 50
        multa = excesso * 4.0
        print(f'Peso Comprado: {peso}\nPeso Excedido: {excesso}\nMulta: {multa}')
    else:
        print(f'Peso Comprado: {peso}\nMulta: 0.00')


# ----------------------------------------------------------------------------------------------------
"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
1 - salário bruto.
2 - quanto pagou ao INSS.
3 - quanto pagou ao sindicato.
4 - o salário líquido.
5 - calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""


def salario(gph, horas):
    bruto = gph * horas
    inss = bruto * (8 / 100)
    ir = bruto * (11 / 100)
    sind = bruto * (5 / 100)
    liquido = bruto - (inss + ir + sind)

    print(
        f'+ Salário Bruto : R${bruto}\n- IR (11%) : R${ir}\n- INSS (8%) : R${inss}\n- Sindicato ( 5%) : R${sind}\n= Salário Liquido : R${liquido}')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da 
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
 a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de 
 latas de tinta a serem compradas e o preço total."""


def tinta(metros_q):
    litros = metros_q / 3
    latas = 1

    if litros > 18:
        latas = litros / 18 + 1
        print(f'Latas de Tinta: {int(latas)}\nValor: R${80 * int(latas)}')
    else:
        print(f'Latas de Tinta: {latas}\nValor: R$80.00')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre 
arredonde os valores para cima, isto é, considere latas cheias."""


def tinta_barato(metros_q):
    l = metros_q / 6  # quantidade de litros

    g = l / 3.6  # quantidade de galoes
    c = l / 18  # quantidade de latas
    # sobras compras
    g_sobra = l % 3.6  # resto de galoes
    c_sobra = l % 18  # resto de latas
    print(g, c, c_sobra, g_sobra, l)
    print()

    if c_sobra < 18:
        print(f'Latas de Tinta: {int(c) + 1}\nValor: R${80 * (int(c) + 1)}')
    else:
        print(f'Latas de Tinta: {int(c)}\nValor: R${80 * int(c)}')

    print()

    if g_sobra < 3.6:
        print(f'Galoes de Tinta: {int(g) + 1}\nValor: R${25 * (int(g) + 1)}')
    else:
        print(f'Galoes de Tinta: {int(g)}\nValor: R${25 * int(g)}')

    print()
    if c_sobra < 18 and c_sobra / 3.6 <= 3:
        print(
            f'Latas de tinta: {int(c)}\nGaloes de Tinta: {int(c_sobra / 3.6) + 1}\nValor: R${(80 * int(c)) + (25 * (int(c_sobra / 3.6) + 1))}')
    else:
        print(f'Latas de Tinta: {int(c)}\nGaloes de Tinta: 0\nValor: R${80 * int(c)}')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
 Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""


def download_time(size, speed):
    time_s = size / speed
    min = time_s / 60
    spare = time_s % 6
    print(f'Estimated Time: {int(min)}m {int(spare)}s')


# -----------------------------------------------------------------------------------------------------
'Estrutura De Decisao'
# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que peça dois números e imprima o maior deles"""


def biggest(number_01, number_02):
    if number_01 > number_02:
        print(number_01)
    elif number_01 < number_02:
        print(number_02)
    else:
        print('Numeros iguais!')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""


def neg_pos(number_01):
    if number_01 > 0:
        print('Positive')
    elif number_01 < 0:
        print('Negative')
    else:
        print('Number is Zero')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
 F - Feminino, M - Masculino, Sexo Inválido."""


def sex(sexo):
    if sexo == 'M':
        print('Sexo Masculino')
    elif sexo == 'F':
        print('Sexo Feminino')
    else:
        print('Sexo Invalido')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""


def val_cons(letter):
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print('Vogal')
    else:
        print('Consoante')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez."""


def media_prova(nota_01, nota_02):
    media = (nota_01 + nota_02) / 2

    if media == 10:
        print('Aprovado com Destincao!')
    elif media >= 7.0:
        print('Aprovado!')
    else:
        print('Reprovado!')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia três números e mostre o maior deles."""


def big_a_three(number_01, number_02, number_03):
    if number_01 > number_02 and number_01 > number_03:
        print(number_01)
    elif number_02 > number_01 and number_02 > number_03:
        print(number_02)
    else:
        print(number_03)


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia três números e mostre o maior e o menor deles."""


def maior_e_menor(number_01, number_02, number_03):
    menor = 0
    maior = 0

    # if para saber o maior numero
    if number_01 > number_02 and number_01 > number_03:
        maior = number_01
    elif number_02 > number_01 and number_02 > number_03:
        maior = number_02
    else:
        maior = number_03
    # if para saber o menor numero
    if number_01 < number_02 and number_01 < number_03:
        menor = number_01
    elif number_02 < number_01 and number_02 < number_03:
        menor = number_02
    else:
        menor = number_03

    print(f'Maior: {maior}\nMenor: {menor}')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato."""


def mais_barato(number_01, number_02, number_03):
    menor = 0
    if number_01 < number_02 and number_01 < number_03:
        menor = number_01
    elif number_02 < number_01 and number_02 < number_03:
        menor = number_02
    else:
        menor = number_03

    print(f'O item mais barato: {menor}')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""


def ordem_dec(number_01, number_02, number_03):
    menor = 0
    maior = 0
    meio = 0

    # if para saber o maior numero
    if number_01 > number_02 and number_01 > number_03:
        maior = number_01
    elif number_02 > number_01 and number_02 > number_03:
        maior = number_02
    else:
        maior = number_03
    # if para saber o menor numero
    if number_01 < number_02 and number_01 < number_03:
        menor = number_01
    elif number_02 < number_01 and number_02 < number_03:
        menor = number_02
    else:
        menor = number_03
    # if para saber o numero do meio
    if menor < number_01 < maior:
        meio = number_01
    elif menor < number_02 < maior:
        meio = number_02
    else:
        meio = number_03

    print(maior, meio, menor)


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino 
ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso."""


def greeting(turno):
    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite!')
    else:
        print('Valor Invalido!')


# -----------------------------------------------------------------------------------------------------
"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
 para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
 baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento."""


def ajuste_salarial(antigo_s):
    novo_s = 0
    reajuste = 0
    percentual = 0

    if antigo_s <= 280:  # reajuste de 20%
        novo_s = antigo_s + ((antigo_s * 20) / 100)
        reajuste = novo_s - antigo_s
        percentual = 20
    elif 280 < antigo_s <= 700:  # reajuste de 15%
        novo_s = antigo_s + ((antigo_s * 15) / 100)
        reajuste = novo_s - antigo_s
        percentual = 15
    elif 700 < antigo_s < 1500:  # reajuste de 10%
        novo_s = antigo_s + ((antigo_s * 10) / 100)
        reajuste = novo_s - antigo_s
        percentual = 10
    elif antigo_s >= 1500:  # reajuste de 5%
        novo_s = antigo_s + ((antigo_s * 5) / 100)
        reajuste = novo_s - antigo_s
        percentual = 5
    else:
        print('Valor Invalido!')

    print(
        f'Salario Anterior: R${antigo_s}\nPercetual de Aumento: {percentual}%\nReajuste: R${reajuste}\nSalario Atualizado: R${novo_s}')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia um número e exiba o dia correspondente da semana.
 (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""


def dia_da_semana(number_01):
    if number_01 == 1:
        print(f'{number_01} - Domingo')
    elif number_01 == 2:
        print(f'{number_01} - Segunda-Feira')
    elif number_01 == 3:
        print(f'{number_01} - Terca-Feira')
    elif number_01 == 4:
        print(f'{number_01} - Quarta-Feira')
    elif number_01 == 5:
        print(f'{number_01} - Quinta-Feira')
    elif number_01 == 6:
        print(f'{number_01} - Sexta-Feira')
    elif number_01 == 7:
        print(f'{number_01} - Sabado')
    else:
        print('Valor Invalido!')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
 e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito 
for A, B ou C ou “REPROVADO” se o conceito for D ou E."""


def media_semestre(nota_01, nota_02):
    media = (nota_01 + nota_02) / 2

    if media >= 6.0:
        if 6.0 <= media < 7.5:
            print(f'Nota 01: {nota_01}\nNota 02: {nota_02}\nMedia: {media} - C')
        elif 7.5 <= media < 9.0:
            print(f'Nota 01: {nota_01}\nNota 02: {nota_02}\nMedia: {media} - B')
        else:
            print(f'Nota 01: {nota_01}\nNota 02: {nota_02}\nMedia: {media} - A')
        print('APROVADO!')
    else:
        if 4.0 <= media < 6.0:
            print(f'Nota 01: {nota_01}\nNota 02: {nota_02}\nMedia: {media} - D')
        else:
            print(f'Nota 01: {nota_01}\nNota 02: {nota_02}\nMedia: {media} - E')
        print('REPROVADO!')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
 ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;"""


def triangulo(lado_01, lado_02, lado_03):
    if lado_01 + lado_02 > lado_03 or lado_01 + lado_03 > lado_02 or lado_02 + lado_03 > lado_01:
        print(f'Os lados {lado_01}, {lado_02} e {lado_03} formam um triangulo.')
        if lado_01 == lado_02 == lado_03:
            print("Triangulo Equilatero!")
        elif lado_01 == lado_02 or lado_01 == lado_03 or lado_02 == lado_03:
            print("Triangulo Isoceles!")
        else:
            print('Triangulo Escaleno!')
    else:
        print(f'Os lados {lado_01}, {lado_02} e {lado_03} nao formam um triangulo.')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
 e continue pedindo até que o usuário informe um valor válido."""


def nota_valida():
    nota = -1
    while (nota < 0) or (nota > 10):
        nota = float(input('Informe uma nota: '))
        if (nota < 0) or (nota > 10):
            print('Nota Invalida')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações."""


def login_usuario():
    login = []
    senha = []

    while login == senha:
        login = str(input('Usuario:'))
        senha = str(input('Senha:'))
        if login == senha:
            print('ERRO! Valores Invalidos! Senha igual ao usuario!')

    print("Usuario e senha definidos!")


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""


def pessoa_info():
    nome = []
    idade = -1
    income = -2
    sexo = 'a'
    e_civ = 'e'

    while len(nome) <= 3:  # nome imput
        nome = str(input('Nome:'))
        if len(nome) <= 3:
            print('Nome Invalido! Digite um nome maior que 3 caracteres.')
    while idade < 0 or idade > 150:  # idade input
        idade = int(input('Idade:'))
        if idade < 0 or idade > 150:
            print('Idade Invalida! Digite uma idade entre 0 e 150.')
    while income < 0:  # salario input
        income = float(input('Salario:'))
        if income < 0:
            print('Salario Invalido! Digite um salario maior que zero.')
    while sexo != 'f' and sexo != 'm':  # sexo input
        sexo = str(input('Sexo:'))
        if sexo != 'f' and sexo != 'm':
            print('Sexo Invalido! Digite m = masculino ou f = feminino.')
    while e_civ != 's' and e_civ != 'c' and e_civ != 'v' and e_civ != 'd':  # e_civ input
        e_civ = str(input('Estado Civil:'))
        if e_civ != 's' and e_civ != 'c' and e_civ != 'v' and e_civ != 'd':
            print('Estado Civil Invalido! Digite "s, c, v ou d".')

    print(f'Pessoa Definida!\n Nome: {nome}\nIdade: {idade}\nSalario: {sexo}\nSexo: {sexo}\nEstado Civil: {e_civ}')


# -----------------------------------------------------------------------------------------------------
"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
 de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
  que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a
   população do país B, mantidas as taxas de crescimento."""


def cresc_pop():
    # definicao de valores de populacao e crescimento
    pop_01 = int(input('Primeira Populacao:'))
    tax_c_01 = float(input('Taxa de Crescimento:'))
    pop_02 = int(input('Segunda Populacao:'))
    tax_c_02 = float(input('Taxa de Crescimento:'))
    ano = 1

    # porcentagem de crescimento
    tax_c_01 = 1 + (tax_c_01 / 100)
    tax_c_02 = 1 + (tax_c_02 / 100)

    # calculo de anos
    while pop_01 <= pop_02:
        pop_01 *= tax_c_01
        pop_02 *= tax_c_02
        ano += 1

    # Resultado
    print(f'Anos necessarios para primeira populacao ultrapassar a segunda: {ano}.')


# -----------------------------------------------------------------------------------------------------
"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
 Valide a entrada e permita repetir a operação."""


def cresc_pop_valid():
    # define variaveis de taxa de crescimento e populacao um
    pop_01 = 0
    tax_c_01 = 0

    while pop_01 <= 0:  # informa populacao 1
        pop_01 = int(input('Primeira Populacao:'))
        if pop_01 <= 0:
            print('Digite um valor positivo para a populacao')
    while tax_c_01 <= 0:  # informa taxa de crescimento da populacao 1
        tax_c_01 = float(input('Taxa de Crescimento:'))
        if tax_c_01 <= 0:
            print('Digite um valor positivo para a taxa de crescimento')
    pop_02 = pop_01  # define populacao 2
    while pop_02 <= pop_01:  # informa populacao 2
        pop_02 = int(input('Segunda Populacao:'))
        if pop_02 <= pop_01:
            print('Populacao dois deve ser menor que populacao um')
    tax_c_02 = tax_c_01  # define taxa de crescimento populacao 2
    while tax_c_02 >= tax_c_01:  # informa taxa de crescimento populacao 2
        tax_c_02 = float(input('Taxa de Crescimento:'))
        if tax_c_02 >= tax_c_01:
            print('Percentual de crescimento da populacao dois deve ser menor que a populacao um')
    # define ano
    ano = 1
    # porcentagem de crescimento
    tax_c_01 = 1 + (tax_c_01 / 100)
    tax_c_02 = 1 + (tax_c_02 / 100)
    # calculo de anos
    while pop_01 <= pop_02:
        pop_01 *= tax_c_01
        pop_02 *= tax_c_02
        ano += 1
    # Resultado
    print(f'Anos necessarios para primeira populacao ultrapassar a segunda: {ano}.')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
 Depois modifique o programa para que ele mostre os números um ao lado do outro."""


def prim_e():
    number = int(input('Numero:'))
    for i in range(1, number + 1):
        print(i)


def prim_l():
    number = int(input(('Numero:')))
    for i in range(1, number + 1):
        print(i, end="")


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que leia 5 números e informe o maior número."""


def maior_5():
    for i in range(0, 5):
        numero = int(input('Informe um numero: '))
        if 'maior' in vars():
            if numero > maior:
                maior = numero
        else:
            maior = numero

    print('O maior numero que voce digitou e', maior)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que leia 5 números e informe a soma e a média dos números."""


def soma_media():
    soma = 0

    for i in range(0, 5):
        numero = int(input('informe um numero:'))
        soma += numero

    print('Soma:', soma)
    print('Media', soma / 5.0)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""


def num_entre_1_50():
    for i in range(1, 50, 2):
        print(i)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo 
compreendido por eles."""


def intervalo_inteiros():
    number_a = int(input('Numero A:'))
    number_b = int(input('Numero B:'))

    for i in range(number_a + 1, number_b):
        print(i)


# -----------------------------------------------------------------------------------------------------
"""Altere o programa anterior para mostrar no final a soma dos números."""


def intervalo_soma():
    number_a = int(input('Numero A:'))
    number_b = int(input('Numero B:'))
    soma = 0

    for i in range(number_a + 1, number_b):
        print(i)
        soma += i
    print('Soma: ', soma)


# -----------------------------------------------------------------------------------------------------
"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
 O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50"""


def tabuada_1a10():
    number = int(input('informe um numero inteiro de 1 a 10:'))

    for i in range(1, 11):
        print(f'{number} X {i} = {number * i}')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado 
ao segundo número. Não utilize a função de potência da linguagem."""


def primeiro_ao_segundo():
    base = int(input('Numero Base:'))
    expoente = int(input('Numero Expoente:'))
    base_f = base
    for i in range(1, expoente):
        base_f *= base

    print(base_f)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
 quantidade de números impares."""


def par_e_impar():
    impar = 0
    par = 0
    for i in range(0, 10):
        numero = int(input('Informe um numero: '))
        if numero % 2 == 1:
            impar += 1
        else:
            par += 1
    print(f'Par: {par}\nImpar: {impar}')


# -----------------------------------------------------------------------------------------------------
"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo."""


def fibonacci_n():
    n = 0
    while n <= 0:
        n = int(input('Termo da serie de Fibonacci desejado:'))
        if n <= 0:
            print('O termo deve ser positivo:')
    # imprime o primeiro termo
    n1 = 0
    print(n1)
    n2 = 1
    for i in range(0, n):
        print(n2)
        n3 = n1 + n2
        n1 = n2
        n2 = n3


# -----------------------------------------------------------------------------------------------------
"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
 Faça um programa que gere a série até que o valor seja maior que 500."""


def fibonacci_m500():
    n1 = 0
    print(n1)
    n2 = 1
    while n2 < 500:
        print(n2)
        n3 = n1 + n2
        n1 = n2
        n2 = n3


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120"""


def fatorial():
    number = 0
    while number <= 0:
        number = int(input('Insira um numero para ser fatorado:'))
        if number <= 0:
            print('O termo deve ser positivo:')
    produto = 1
    for i in range(1, number + 1):
        produto *= i
    print(produto)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor 
e a soma dos valores."""


def maior_menor_soma():
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Voce quer informar quantos numeros: '))
        if quantidade <= 0:
            print('Quantidade deve ser positiva!')

    soma = 0
    for i in range(0, quantidade):
        numero = int(input('Informe um numero: '))
        if 'maior' not in vars() or numero > maior:
            maior = numero

        if 'menor' not in vars() or numero < menor:
            menor = numero

        soma += numero

    print('Menor numero:', menor)
    print('Maior numero:', maior)
    print('Soma dos numeros:', soma)


# -----------------------------------------------------------------------------------------------------
"""Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""


def maior_menor_soma_1a1000():
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Voce quer informar quantos numeros: '))
        if quantidade <= 0:
            print('Quantidade deve ser positiva!')

    soma = 0
    for i in range(0, quantidade):
        numero = 1001
        while numero > 1000 or numero < 1:
            numero = int(input('Informe um numero: '))
            if numero > 1000:
                print('Digite um numero menor ou igual a 1000')
            if numero < 1:
                print('Digite um numero maior que 1')
        if 'maior' not in vars() or numero > maior:
            maior = numero

        if 'menor' not in vars() or numero < menor:
            menor = numero

        soma += numero

    print('Menor numero:', menor)
    print('Maior numero:', maior)
    print('Soma dos numeros:', soma)


# -----------------------------------------------------------------------------------------------------
"""Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e \
limitando o fatorial a números inteiros positivos e menores que 16."""


def fatorial_pos_menor16():
    number = 0
    while number <= 0 or number > 16:
        number = int(input('Insira um numero para ser fatorado:'))
        if number <= 0:
            print('O numero deve ser positivo:')
        if number > 16:
            print('O numero deve ser maior que 16')
    produto = 1

    for i in range(1, number + 1):
        produto *= i
    print(produto)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
 Um número primo é aquele que é divisível somente por ele mesmo e por 1"""


def primo():
    number = 0
    while number <= 0:
        number = int(input('Insira um numero:'))
        if number <= 0:
            print('O numero deve ser positivo')

    primo_n = True

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            primo_n = False

    if primo_n:
        print('O numeor e primo!')
    else:
        print('O numero NAO e primo')


# -----------------------------------------------------------------------------------------------------
"""Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
 por quais número ele é divisível."""


def primo_divisores():
    number = 0
    while number <= 0:
        number = int(input('Insira um numero:'))
        if number <= 0:
            print('O numero deve ser positivo')

    primo_n = True

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            primo_n = False

    if primo_n:
        print('O numeor e primo!')
    else:
        print('O numero NAO e primo')

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""


def primo_qtd_divisoes():
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(
            input('Digite o final do intervalo comecando em 1, \nvoce recebera os numeros primos deste intervalo: '))
        if quantidade <= 0:
            print('A quandidade deve ser positiva!')

    divisoes = 0
    for numero in range(1, quantidade + 1):
        primo_n = True
        for i in range(2, int(numero / 2) + 1):
            divisoes += 1
            if numero % i == 0:
                primo_n = False
                break

        if primo_n:
            print(numero)

    print('\nQuantidade de divisoes:', divisoes)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que calcule o mostre a média aritmética de N notas."""


def media_aritimetica():
    qtd_notas = 0
    while qtd_notas <= 0:
        qtd_notas = int(input('Insira quantas notas serao inseridas:'))
        if qtd_notas <= 0:
            print('Insira um numero positivo para a quantidade de notas.')

    soma = 0

    for i in range(0, qtd_notas):
        nota = float(input('informe um numero:'))
        soma += nota

    print('Media', soma / qtd_notas)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média 
de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta
 ou idosa, conforme a média calculada."""


def media_idade():
    qtd_idade = 0
    while qtd_idade <= 0:
        qtd_idade = int(input('Insira quantas notas serao inseridas:'))
        if qtd_idade <= 0:
            print('Insira um numero positivo para a quantidade de notas.')

    soma = 0

    for i in range(0, qtd_idade):
        idade = int(input('informe um numero:'))
        soma += idade

    media = int(soma / qtd_idade)

    if 0 <= media < 26:
        print(f'Turma: Jovem \nMedia: {media}')
    elif 26 <= media < 60:
        print(f'Turma: Adulta \nMedia: {media}')
    else:
        print(f'Idosa: Jovem \nMedia: {media}')


# -----------------------------------------------------------------------------------------------------
"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato."""


def numero_votos():
    qtd_votos = 0
    while qtd_votos <= 0:
        qtd_votos = int(input('Insira o numero de votos a serem inseridos:'))
        if qtd_votos <= 0:
            print('O numero de votos precisa ser positivo!')

    raph = 0
    rach = 0
    lala = 0

    for i in range(0, qtd_votos):
        voto = 0
        while voto < 1 or voto > 3:
            voto = int(input('Canditados: \n1 - Raph    2 - Rach    3 - Lala'))
            if voto < 1 or voto > 3:
                print('Insira um voto valido!')

        if voto == 1:
            raph += 1
        elif voto == 2:
            rach += 1
        else:
            lala += 1

    print(f'Numero total de Votos: {qtd_votos}\nRaph: {raph}\nRach: {rach}\nLala: {lala}')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de 
turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""


def media_alunos_turma():
    turmas = 0
    while turmas <= 0:
        turmas = int(input('Insira a a quantidade de turmas que a media sera feita: '))
        if turmas <= 0:
            print('Insira um numero positivo de turmas!')

    soma_alunos = 0

    for i in range(0, turmas):
        alunos = 0
        while alunos <= 0 or alunos > 40:
            alunos = int(input(f'Insira o numero de alunos na turma {i + 1}:'))
            if alunos <= 0 or alunos > 40:
                print('Insira um numero valido de alunos!')
        soma_alunos += alunos

    print(f'Media de alunos por turma: {int(soma_alunos / turmas)}')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o 
valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""


def colecao_cd():
    cds = 0
    while cds <= 0:
        cds = int(input('Insira o numero de CDs na colecao:'))
        if cds <= 0:
            print('Insira um numero positivo de CDs!')

    valor_cds = 0

    for i in range(0, cds):
        valor = 0
        while valor <= 0:
            valor = float(input('Insira o valor do CD:'))
            if valor <= 0:
                print('Insira um valor positivo para o CD!')
            valor_cds += valor

    print(f'Valor Total: {valor_cds}\nValor Medio: {valor_cds / cds}')


# -----------------------------------------------------------------------------------------------------
"""O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar 
o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o 
cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos 
itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa 
que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50"""


def loja_199_50itens():
    print('Loja Quase Dois - Tabela de Precos')
    for i in range(1, 51):
        print(f'{i} - R${1.99 * i}')


# -----------------------------------------------------------------------------------------------------
"""O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela
de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo 
abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
"""


def loja_paes():
    preco = 0
    while preco <= 0:
        preco = float(input('Insira o preco do pao:'))
        if preco <= 0:
            print('O preco precisa ser positivo!')

    print('Panificadora Pao de Ontem - Tabela de Precos')

    for i in range(1, 51):
        print(f'{i} - R${preco * i}')


# -----------------------------------------------------------------------------------------------------
"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja 
de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá 
receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser 
informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e 
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída 
deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 3.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
..."""


def caixa_registradora():
    soma = 0.00
    qtd = 1
    preco = 1
    while preco != 0:
        preco = float(input('Produto %d: R$' % qtd))
        soma += preco
        qtd += 1

    print("Total: R$ %.2f" % soma)
    pagamento = float(input('Dinheiro: R$'))

    print(f'Troco: R$ %.2f' % (pagamento - soma))


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120"""


def fatorial_c_output():
    number = 0
    while number <= 0:
        number = int(input('Insira um numero para ser fatorado:'))
        if number <= 0:
            print('O termo deve ser positivo:')
    produto = 1
    print('Fatorial de: %d' % number)
    print('!%d = ' % number, end="")
    for i in reversed(range(2, number + 1)):
        print('%d . ' % i, end="")

        produto *= i

    print('1 = %d' % produto, end="")


# -----------------------------------------------------------------------------------------------------
"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um 
conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, 
bem como a média das temperaturas."""


def temperaturas():
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Voce quer informar quantas temperaturas: '))
        if quantidade <= 0:
            print('Quantidade deve ser positiva!')

    soma = 0.00
    for i in range(0, quantidade):
        temperatura = 101
        while temperatura > 100 or temperatura < 1:
            temperatura = float(input('Informe uma temperatura: '))
            if temperatura > 100:
                print('Digite uma temperatura menor ou igual a 100 graus')
            if temperatura < 1:
                print('Digite uma temperatura maior que 1 graus')
        if 'maior' not in vars() or temperatura > maior:
            maior = temperatura

        if 'menor' not in vars() or temperatura < menor:
            menor = temperatura

        soma += temperatura

    print('Menor numero:', menor)
    print('Maior numero:', maior)
    print('Media das temperaturas: %.2f' % float(soma / quantidade))


# -----------------------------------------------------------------------------------------------------
"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça 
um número inteiro e determine se ele é ou não um número primo."""


def primo_second():
    number = 0
    while number <= 0:
        number = int(input('Insira um numero:'))
        if number <= 0:
            print('O numero deve ser positivo')

    primo_n = True

    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            primo_n = False

    if primo_n:
        print('O numeor e primo!')
    else:
        print('O numero NAO e primo')


# -----------------------------------------------------------------------------------------------------
"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos 
existentes entre 1 e um número inteiro informado pelo usuário"""


def primo_qtd_divisoes():
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(
            input('Digite o final do intervalo comecando em 1, \nvoce recebera os numeros primos deste intervalo: '))
        if quantidade <= 0:
            print('A quandidade deve ser positiva!')

    divisoes = 0
    for numero in range(1, quantidade + 1):
        primo_n = True
        for i in range(2, int(numero / 2) + 1):
            divisoes += 1
            if numero % i == 0:
                primo_n = False
                break

        if primo_n:
            print(numero)

    print('\nQuantidade de divisoes:', divisoes)


# -----------------------------------------------------------------------------------------------------
"""Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial."""


def tabuada_periodo():
    numero = 0
    inicio = 0
    fim = 0

    while numero <= 0:
        numero = int(input('Digite a base da tabuada:'))
        if numero <= 0:
            print('Insira um numero positivo para a base da tabuada!')
    while inicio <= 0:
        inicio = int(input('Digite o inicio da tabuada:'))
        if inicio <= 0:
            print('Digite um numero positivo para o inicio da tabuada!')
    while fim <= 0 or fim <= inicio:
        fim = int(input('Digite o fim da tabuada:'))
        if fim <= 0 or fim <= inicio:
            print('Digite um numero positivo e maior que o inico para o fim da tabuada!')

    print(f'Vou montar uma tabuada de {numero} começando em {inicio} e terminando em {fim}:')
    for i in range(inicio, fim + 1):
        print(f'{numero} X {i} = {numero * i}')


# -----------------------------------------------------------------------------------------------------
"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes 
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o 
usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos 
e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas 
e dos pesos dos clientes"""


def academia():
    codigo = -1  # variavel com conteudo do codigo do cliente
    total_clientes = 0  # variavel com o total de clientes
    soma_a = 0.0  # variavel com a soma das alturas dos clientes
    soma_p = 0.0  # variavel com a soma dos pesos dos clientes

    while codigo != 0:
        codigo = int(input('Informe o codigo do cliente:'))
        if codigo != 0:
            # input das informacoes do cliente
            altura = float(input('Informe a altura do cliente:'))
            peso = float(input('Informe o peso do cliente:'))
            # somas para futuros calculos
            total_clientes += 1
            soma_a += altura
            soma_p += peso
            # condicoes
            if 'maisAlto' not in vars() or altura > maisAlto:
                maisAlto = altura
                codico_A = codigo  # codigo do mais alto
            if 'maisBaixo' not in vars() or altura < maisBaixo:
                maisBaixo = altura
                codigo_B = codigo  # codigo do mais baixo
            if 'maisGordo' not in vars() or peso > maisGordo:
                maisGordo = peso
                codigo_G = codigo  # codigo do mais gordo
            if 'maisMagro' not in vars() or peso < maisMagro:
                maisMagro = peso
                codigo_M = codigo  # codigo do mais magro
    # print dos resultados
    print('O cliente mais alto eh %i com %f' % codico_A, maisAlto)
    print('O cliente mais baixo eh %i com %f' % codigo_B, maisBaixo)
    print('O cliente mais pesado eh %i com %f' % codigo_G, maisGordo)
    print('O cliente mais magro eh %i com %f' % codigo_M, maisMagro)
    # print das medias
    print('Media das alturas dos clientes: %.2f' % soma_a / float(total_clientes))
    print('Media dos pesos dos clientes: %.2f' % soma_p / float(total_clientes))


# -----------------------------------------------------------------------------------------------------
"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano 
anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o 
programa permitindo que o usuário digite o salário inicial do funcionário."""


def aumento_salarial():
    salario_i = 0.0
    ano_i = 1994
    percentual = 1.5
    while salario_i <= 0.0:
        salario_i = float(input('Salario Inicial:'))
        if salario_i <= 0.0:
            print('Digite um salario inicial positivo!')
    while ano_i < 1995 or ano_i > 2020:
        ano_i = int('Ano inicial:')
        if ano_i < 1995 or ano_i > 2020:
            print('Digite um ano valido!')
    ano = ano_i
    salario_a = salario_i
    while ano <= 2020:
        print('Ano: %i Percentual: %.2f Salario: %.2f' % (ano, percentual, salario_a))
        salario_a += salario_a * (percentual / 100)
        percentual *= 2
        ano += 1

    print('Salario atual do funcionario: %.2f' % (salario_a))


# -----------------------------------------------------------------------------------------------------
'Exercicios de Listas'
# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""


def lista_num():
    numbers = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de numeros na lista:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de numeros!')
    for i in range(0, quantidade):
        numbers.append(input('Informe um numero:'))

    print(numbers)


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""


def lista_reversa():
    numbers = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de numeros na lista:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de numeros!')
    for i in range(0, quantidade):
        numbers.append(input('Informe um numero:'))

    numbers.reverse()

    print(numbers)


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""


def media__notas_l():
    notas = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de notas:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de notas!')

    for i in range(0, quantidade):
        notas.append(float(input('Informe uma nota:')))

    soma_n = 0.0
    print('\nNotas Digitadas:')
    for i in range(0, quantidade):
        print('Notas %d: %.2f' % (i, notas[i]))
        soma_n += notas[i]

    print('Media das Notas: %.2f' % (soma_n / quantidade))


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes."""


def consoantes():
    letras = []
    vogais = ['A', 'E', 'I', 'O', 'U']
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de letras:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de letras!')

    for i in range(0, quantidade):
        letras.append(input('Informe um caracter:').upper())

    total_cons = 0
    cons = []

    for i in range(0, quantidade):
        if letras[i] not in vogais:
            cons.append(letras[i])
            total_cons += 1

    print('Voce digitou %d consoantes' % total_cons)
    print(cons)


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no 
vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""


def numeros_classifica():
    numeros = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de numeros:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de numeros!')
    par = []
    impar = []

    for i in range(0, quantidade):
        numero = int(input('Informe um numero:'))
        numeros.append(numero)

    for i in range(0, quantidade):
        if numeros[i] % 2 == 0:
            par.append(numeros[i])
        else:
            impar.append(numeros[i])

    print(f'Os numeros: {numeros}')
    print(f'Numeros Pares: {par}')
    print(f'Numeros Impares: {impar}')


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada 
aluno, imprima o número de alunos com média maior ou igual a 7.0."""


def media_anual_n_alunos():
    notas = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de alunos:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de alunos!')
    # colo notas dos alunos dentro de um vetor
    for i in range(0, quantidade):
        notas_aluno = []  # cria um vetor para armazenar as notas de 1 aluno
        for j in range(0, 4):  # insere 4 notas de um aluno em um vetor
            notas_aluno.append(float(input('Informe a nota do aluno %d: ' % (i + 1))))
        notas.append(notas_aluno)  # insere vetor com notas de um aluno dentro do vetor de alunos

    alunos_media = 1
    for notas_aluno in notas:
        soma_notas = 0.0
        for nota in notas_aluno:
            soma_notas += nota
        if (soma_notas / 4.0) >= 7.0:
            alunos_media += 1

    print('%d alunos ficaram acima da media' % alunos_media)


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""


def soma_mult_n_numeros():
    numeros = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de numeros:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de numeros!')

    for i in range(0, quantidade):
        numero = int(input('Informe um numero:'))
        numeros.append(numero)
    soma = 0
    mult = 1
    for i in range(0, quantidade):
        soma += numeros[i]
        mult *= numeros[i]

    print(numeros)
    print(soma)
    print(mult)


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo 
vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""


def info_pessoas():
    pessoas = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de numeros:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de numeros!')

    for i in range(0, quantidade):
        pessoa = [input('Informe a idade da pessoa %d :' % (i + 1)),
                  (input('Informe a altura da pessoa %d :' % (i + 1)))]
        pessoas.append(pessoa)

    pessoas.reverse()

    for pessoa in pessoas:
        print('Idade: %s - Altura: %s' % (pessoa[0], pessoa[1]))


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados
 dos elementos do vetor."""


def soma_quadrados():
    numeros = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de numeros:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de numeros!')

    for i in range(0, quantidade):
        numero = int(input('Insira um numero:'))
        numeros.append(numero)
    soma_q = 0

    for i in range(0, quantidade):
        soma_q += numeros[i] ** 2
    print(soma_q)


# -----------------------------------------------------------------------------------------------------
"""Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""


def soma_vetores():
    vet1 = []
    vet2 = []
    vet3 = []

    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de numeros por vetor:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva de numeros por vetor!')

    print('Informe os numeros do primeiro vetor')
    for i in range(0, quantidade):
        vet1.append(int(input('Insira um numero:')))
    print('Informe os numeros para o segundo vetor')
    for i in range(0, quantidade):
        vet2.append(int(input('Insira um numero:')))
    for i in range(0, quantidade):
        vet3.append(vet1[i])
        vet3.append(vet2[i])

    print(vet3)


# -----------------------------------------------------------------------------------------------------
"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais 
de 13 anos possuem altura inferior à média de altura desses alunos."""


def altura_maior_13_media():
    alunos = []
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Digite a quantidade de alunos:'))
        if quantidade <= 0:
            print('Digite uma quantidade positivo de alunos!')

    for i in range(0, quantidade):
        aluno = [int(input('Informe a idade do aluno %d :' % (i + 1))),
                 float(input('Informe a altura do aluno %d :' % (i + 1)))]
        alunos.append(aluno)

    soma_altura = 0.0
    for aluno in alunos:
        soma_altura += aluno[1]

    media_altura = soma_altura / float(quantidade)

    total_alunos_acima_media = 0
    for aluno in alunos:
        if aluno[0] >= 13 and aluno[1] >= media_altura:
            total_alunos_acima_media += 1

    print('Existem %d alunos com mais de 13 anos acima da media de altura' % total_alunos_acima_media)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após 
isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em 
que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""


def temperatura_media_anual_maior():
    meses = ('Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    temperaturas = {}

    for mes in meses:
        temperaturas[mes] = float(input('Informe a temperatura media do mes de %s' % mes))

    somaTemperaturas = 0.0
    for temperatura in temperaturas.values():
        somaTemperaturas += temperatura

    mediaTemperaturaAnual = somaTemperaturas / 12.0

    print('Temperaturas acima da media anual: %.2f' % mediaTemperaturaAnual)

    for mes in meses:
        if temperaturas[mes] >= mediaTemperaturaAnual:
            print('%s - %.2f' % (mes, temperaturas[mes]))


# -----------------------------------------------------------------------------------------------------
"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa 
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 
e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""


def detetive():
    print('Programa Detetive')
    print('Responda as perguntas abaixo com S (sim) ou N (nao')

    perguntas = ('Voce telefonou para a vitima?',
                 'Voce esteve no local do crime?',
                 'Voce mora perto da vitima?',
                 'Voce devia a vitima?',
                 'Voce ja trabalhou com a vitima?')

    respostas = []

    for pergunta in perguntas:
        respostas.append(input(pergunta).upper())

    classificacao = 0
    for resposta in respostas:
        if resposta == 'S':
            classificacao += 1

    if classificacao < 2:
        print('Inocente')
    elif classificacao == 2:
        print('Suspeito')
    elif classificacao <= 4:
        print('Cumplice')
    else:
        print('Assassino')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a 
entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada 
de dados, faça:
a - Mostre a quantidade de valores que foram lidos;
b - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d - Calcule e mostre a soma dos valores;
e - Calcule e mostre a média dos valores;
f - Calcule e mostre a quantidade de valores acima da média calculada;
g - Calcule e mostre a quantidade de valores abaixo de sete;
h - Encerre o programa com uma mensagem;"""


def brincadeira_notas():
    valores = []
    valor = 0

    while valor != -1:
        valor = int(input('Informe um valor:'))
        if valor != -1:
            valores.append(valor)

    print('Quantidade de valores lidos: %d' % len(valores))
    print(valores)
    valores.reverse()
    print(valores)

    somaValores = 0
    for valor in valores:
        somaValores += valor

    mediaValores = somaValores / float(len(valores))
    print('Soma dos Valores: %d' % somaValores)
    print('Media dos Valores: %.2f' % mediaValores)

    valoresAcimaMedia = 0
    valoresAcimaSete = 0
    for valor in valores:
        if valor >= mediaValores:
            valoresAcimaMedia += 1
        if valor >= 7:
            valoresAcimaSete += 1

    print('Valores acima da media: %d' % valoresAcimaMedia)
    print('Valores acima de sete: %d' % valoresAcimaSete)


# -----------------------------------------------------------------------------------------------------
"""Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em 
comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por 
exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, 
ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos 
vendedores receberam salários nos seguintes intervalos de valores:
a - $200 - $299
b - $300 - $399
c - $400 - $499
d - $500 - $599
e - $600 - $699
f - $700 - $799
g - $800 - $899
h - $900 - $999
i - $1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados."""


def vendedores():
    salarioBase = 200
    vendors = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 10):
        valorVendas = float(input('Informe o valor das vendas do vendedor: '))
        salario = valorVendas * 0.09 + salarioBase
        indice = int(salario / 100) - 1
        if indice > 9:
            indice = 9
        elif indice < 1:
            indice = 1
        print(indice)
        vendors[indice - 1] += 1

    for i in range(0, 9):
        print('%d - %d : %d' % ((i * 100 + 200), ((i + 1) * 100 + 199), (vendors[i])))


# -----------------------------------------------------------------------------------------------------
"""Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""


def imprime_p():
    numero = 0
    while numero <= 0:
        numero = int(input('Informe um numero:'))
        if numero <= 0:
            print('Digite um numero positivo!')

    for i in range(1, numero + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print()


# -----------------------------------------------------------------------------------------------------
"""Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha."""


def imprime_n():
    numero = 0
    while numero <= 0:
        numero = int(input('Informe um numero:'))
        if numero <= 0:
            print('Digite um numero positivo!')

    for i in range(1, numero + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


# -----------------------------------------------------------------------------------------------------
"""Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos."""


def soma_termos():
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input('Informe a quantidade de termos:'))
        if quantidade <= 0:
            print('Digite uma quantidade positiva!')

    soma = 0
    for i in range(0, quantidade):
        numero = int(input('Insira um numero:'))
        soma += numero
    print(soma)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo"""


def positivo_ou_negativo(numero):
    if numero <= 0:
        print('N')
    else:
        print('P')


# -----------------------------------------------------------------------------------------------------
"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, 
que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do 
imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas."""


def soma_imposto(taxaImposto, custo):
    custo = custo + (custo * (taxaImposto / 100.0))
    return custo


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa 
deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma 
para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ 
para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar."""


def converte_hora(hora24, minuto24):
    if hora24 > 23 or hora24 < 0 or minuto24 < 0 or minuto24 > 59:
        return None
    if hora24 < 12:
        if hora24 == 0:
            hora24 = 12
        return '%02d:%02d AM' % (hora24, minuto24)
    if hora24 > 12:
        hora24 -= 12
    return '%02d:%02d AM' % (hora24, minuto24)


# -----------------------------------------------------------------------------------------------------
"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de 
uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar 
estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa 
que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá 
voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para 
a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade 
e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para 
pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de 
juros por dia de atraso."""

