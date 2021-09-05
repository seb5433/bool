# A program to convert from binary to hexadecimal demonstrating the actual algorithm,
# not just using hex()
import sys
import math
import utils
import truths
import Kmap


def conversion(Bin):
    # CONVERSION A DECIMAL
    BinaryIN = Bin
    valor_dec = 0
    bin = ""
    numb = BinaryIN
    for i in range(1, (numb.__len__())+1):
        if numb[-i] == str(1):
            valor_dec = valor_dec + (2**(i-1))

    valor_hex = hex(int(valor_dec))
    valor_oct = oct(int(valor_dec))

    linea = "________________"
    print("\n\tCONVERSIONES")
    for x in range(len(BinaryIN)):
        linea = linea + "_"
    print(linea)

    print(f"Binario: \t{BinaryIN}")
    print(f'Decimal: \t{valor_dec}')
    print(f"Hexadecimal: \t{valor_hex}")
    print(f"Octal: \t{valor_oct}")


def simplificar(variables, salidas_1, no_importan=[]):
    # Función que simplifica una expresion booleana según el mapa de karnaugh
    variables = variables
    str_terms = salidas_1
    terms_not_care = no_importan
    t_minterms = [utils.Term(term) for term in str_terms]
    not_cares = [utils.Term(term) for term in terms_not_care]
    minterms = Kmap.Minterms(t_minterms, not_cares)
    resultado = minterms.simplify()
    expresion_final = []
    for x in resultado:
        count = 0
        expr = ''
        for y in str(x):
            if y == '1':
                expr = expr + variables[count]
            elif y == '0':
                expr = expr+variables[count]+"'"
            count += 1
        expresion_final.append(expr)
    expresion = ''
    count = 0
    for x in expresion_final:
        if count == 0:
            expresion = expresion + x
        else:
            expresion = expresion + ' + ' + x
        count += 1
    print(f"Función simplificada: {expresion} 🏆🥇")


def hamming():
    option = 1
    if(option == 1):  # GENERATE HAMMING CODE
        print('Inserte el mensaje en bits')
        d = input()
        data = list(d)
        data.reverse()
        c, ch, j, r, h = 0, 0, 0, 0, []

        while ((len(d)+r+1) > (pow(2, r))):
            r = r+1

        for i in range(0, (r+len(data))):
            p = (2**c)

            if(p == (i+1)):
                h.append(0)
                c = c+1

            else:
                h.append(int(data[j]))
                j = j+1

        for parity in range(0, (len(h))):
            ph = (2**ch)
            if(ph == (parity+1)):
                startIndex = ph-1
                i = startIndex
                toXor = []

                while(i < len(h)):
                    block = h[i:i+ph]
                    toXor.extend(block)
                    i += 2*ph

                for z in range(1, len(toXor)):
                    h[startIndex] = h[startIndex] ^ toXor[z]
                ch += 1

        h.reverse()
        print('El codigo Hamming es: ', end="")
        print(int(''.join(map(str, h))))

    elif(option == 2):  # DETECT ERROR IN RECEIVED HAMMING CODE
        print('Enter the hamming code received')
        d = input()
        data = list(d)
        data.reverse()
        c, ch, j, r, error, h, parity_list, h_copy = 0, 0, 0, 0, 0, [], [], []

        for k in range(0, len(data)):
            p = (2**c)
            h.append(int(data[k]))
            h_copy.append(data[k])
            if(p == (k+1)):
                c = c+1

        for parity in range(0, (len(h))):
            ph = (2**ch)
            if(ph == (parity+1)):

                startIndex = ph-1
                i = startIndex
                toXor = []

                while(i < len(h)):
                    block = h[i:i+ph]
                    toXor.extend(block)
                    i += 2*ph

                for z in range(1, len(toXor)):
                    h[startIndex] = h[startIndex] ^ toXor[z]
                parity_list.append(h[parity])
                ch += 1
        parity_list.reverse()
        error = sum(int(parity_list) * (2 ** i)
                    for i, parity_list in enumerate(parity_list[::-1]))

        if((error) == 0):
            print('There is no error in the hamming code received')

        elif((error) >= len(h_copy)):
            print('Error cannot be detected')

        else:
            print('Error is in', error, 'bit')

            if(h_copy[error-1] == '0'):
                h_copy[error-1] = '1'

            elif(h_copy[error-1] == '1'):
                h_copy[error-1] = '0'
                print('After correction hamming code is:- ')
            h_copy.reverse()
            print(int(''.join(map(str, h_copy))))

    else:
        print('Option entered does not exist')


Opcion = input(
    "Selecciona una opción: \n 1 - Evaluar una expresión con tabla de verdad\n 2 - Simplificar una expresión con mapa de Karnaugh\n 3 - Conversión\n 4 - Hamming\n")
if Opcion == '1':
    print("Inserte las variables que se utilizaran Ej(ABC): ", end="")
    variables = input()
    print("Inserte la expresión a evaluar: ", end="")
    expresion = input()
    var_list = []
    for x in variables:
        var_list.append(x)
    print(truths.Truths(var_list, [expresion]))


elif Opcion == '2':
    print("Inserte las variables que se utilizaran Ej(ABC): ", end="")
    variables = input()
    stop = True
    print("Inserte las combinaciones que dan como salida 1\nPara terminar el ciclo inserte 'f'")
    combinaciones = []
    while stop:
        val = input()
        if val != 'f':
            combinaciones.append(val)
        else:
            stop = False
    simplificar(variables, combinaciones)


elif Opcion == '3':
    correct = False
    BinaryIN = ""
    while not correct:
        BinaryIN = input('Inserte un numero binario: ')
        for value in BinaryIN:
            if value == str(1) or value == str(0):
                continue
            else:
                BinaryIN = input("Pone un numero real pai! \n")
        conversion(BinaryIN)
        correct = True
elif Opcion == '4':
    hamming()
