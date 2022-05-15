def soma(numero1, numero2, base):

    numero1 = list(numero1[::-1])
    numero2 = list(numero2[::-1])

    if len(numero1) > len(numero2):
        controle = 0
        diferenca = len(numero1) - len(numero2)

        while controle < diferenca:
            numero2.append('0')
            controle = controle + 1
    elif len(numero2) > len(numero1):
        controle = 0
        diferenca = len(numero2) - len(numero1)

        while controle < diferenca:
            numero1.append('0')
            controle = controle + 1

    j = 0
    resultado_final = []

    while j < len(numero1):
        soma = int(numero1[j]) + int(numero2[j])

        if j == len(numero1) - 1:
            if soma > 1:
                resultado = soma - 2
                resultado_final.append(resultado)
                resultado_final.append('1')
            elif soma <= 1:
                resultado_final.append(str(soma))
        else:
            if soma > 1:
                resultado = soma - 2
                novo_valor = str(int(numero1[j + 1]) + 1)
                numero1[j + 1] = novo_valor
                resultado_final.append(str(resultado))
            elif soma <= 1:
                resultado_final.append(str(soma))

        j = j + 1
    resultado_final = resultado_final[::-1]
    resultado_final = "".join(str(x) for x in resultado_final)


    return conversor(resultado_final, base)

def subtracao(numero1, numero2, base):

    if len(numero1) % 4 != 0:
        while len(numero1) % 4 != 0:
            numero1 = numero1[::-1] + '0'
        numero1 = numero1[::-1]
    
    
    if len(numero2) % 4 != 0:
        while len(numero2) % 4 != 0:
            numero2 = numero2[::-1] + '0'
        numero2 = numero2[::-1]

    numero2 = numero2.replace('1', '2')
    numero2 = numero2.replace('0', '3')
    
    numero2 = numero2.replace('2', '0')
    numero2 = numero2.replace('3', '1')

    numero2_passo2 = soma(numero2, '1', 5)

    subtracao = str(soma(numero1, numero2_passo2, 5))

    if len(subtracao) > len(numero1):
        subtracao = subtracao.replace(subtracao[0], '', 1)

    print(subtracao)
    return conversor(subtracao, base)

def multiplicacao(numero1, numero2, base):
    multiplicacoes = []
    numero1 = numero1[::-1]
    numero2 = numero2[::-1]

    for elemento in numero2:
        i = 0
        resultado = ''
        while i < len(numero1):
            resultado = resultado + str(int(elemento) * int(numero1[i]))
            i = i + 1
        
        multiplicacoes.append(resultado)


    j = 0
    while j < len(multiplicacoes):
        k = 0
        multiplicacoes[j] = multiplicacoes[j][::-1]
        while k < j:
            multiplicacoes[j] = multiplicacoes[j] + '0'
            k = k + 1
        j = j + 1

    resultado = '0'
    while len(multiplicacoes) > 0:
        resultado = soma(multiplicacoes[0], resultado, 5)
        multiplicacoes.pop(0)
    
    return conversor(resultado, base)

def conversorDecimal(numero):
    numero = numero[::-1]
    array_numero = list(numero)
    num_convertido = 0
    j = 0
    while j < len(array_numero):
        # while j < len(array_numero):
        #     if array_numero[j] == 'A' or array_numero[j] == 'a':
        #         array_numero[j] = '10'
        #     elif array_numero[j] == 'B' or array_numero[j] == 'b':
        #         array_numero[j] = '11'
        #     elif array_numero[j] == 'C' or array_numero[j] == 'c':
        #         array_numero[j] = '12'
        #     elif array_numero[j] == 'D' or array_numero[j] == 'd':
        #         array_numero[j] = '13'
        #     elif array_numero[j] == 'E' or array_numero[j] == 'e':
        #         array_numero[j] = '14'
        #     elif array_numero[j] == 'F' or array_numero[j] == 'f':
        #         array_numero[j] = '15'
        
        num_convertido = int(array_numero[j]) * (2 ** j) + num_convertido
        j = j + 1
    
    numero = numero[::-1]
    return num_convertido

def conversor(numero, base):
    match base:
        case 5:
            return numero
        case 6:
            numero = conversorDecimal(numero)
            base = 8
        case 7:
            numero = conversorDecimal(numero)
            base = 16
        case 8:
            return conversorDecimal(numero)
        case default:
            print("Opção inválida")

    num_convertido = ''
    while int(numero) > 0:
        resto = int(numero) % base

        match resto:
            case 10:
                resto = "A"
            case 11:
                resto = "B"
            case 12:
                resto = "C"
            case 13:
                resto = "D"
            case 14:
                resto = "E"
            case 15: 
                resto = "F"
        num_convertido = num_convertido + str(resto)
        numero = int(int(numero) / base)

    num_convertido = num_convertido[::-1]
    return num_convertido

def menu():
    opcao = -1
    base = 0

    while opcao != 0:
        print('Digite 1 para selecionar a operação de soma')
        print('Digite 2 para selecionar a operação de subtração')
        print('Digite 3 para selecionar a operação de multiplicação')
        print('Digite 0 para sair')

        opcao = int(input())
        if opcao == 0:
            break
        elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
            print("Opção inválida")
            menu()

        print('Digite 5 para selecionar o resultado no sistema binário')
        print('Digite 6 para selecionar o resultado no sistema octal')
        print('Digite 7 para selecionar o resultado no sistema hexadecimal')
        print('Digite 8 para selecionar o resultado no sistema decimal')
        print('Digite 0 para sair')

        base = int(input())
        if base == 0:
            break
        elif base != 5 and base != 6 and base != 7 and base != 8:
            print("Opção inválida")
            menu()

        numero1 = str(input('Digite o primeiro número da operação' + '\n'))
        numero2 = str(input('Digite o segundo número da operação' + '\n'))

        match opcao:
            case 1:
                resultado = soma(numero1, numero2, base)
                print("A soma dos números", numero1, "e", numero2, "é", resultado )
            case 2:
                resultado = subtracao(numero1, numero2, base)
                print("A subtração de", numero1, "por", numero2, "é", resultado )
            case 3:
                resultado = multiplicacao(numero1, numero2, base)
                print("A multiplicação dos números", numero1, "e", numero2, "é", resultado )
            case default:
                print("Opção inválida")
                menu()

    print("Obrigada! Até mais!")

menu()