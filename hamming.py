
def hamming(mensaje):
    # Función que retorna la conversión de un mensaje a codigo hamming
    mensaje = mensaje
    finish = False
    hamming = []
    count = 1

    paridad_pos = 1
    pos = 1
    pos_message = 0
    while not finish:
        if pos == paridad_pos:
            # print(paridad_pos)
            paridad_pos = 2 ** count
            count += 1
            hamming.append('X')

        else:
            hamming.append(mensaje[pos_message])

            if pos_message == len(mensaje)-1:
                finish = True
            pos_message += 1

        pos += 1

    cant_paridad = count-1

    codigo = []
    for x in range(0, cant_paridad):
        # print(x)
        pos = 1
        bajados = []
        cant_1 = 0
        cant_0 = 0
        for y in hamming:
            bin_pos = []
            # print(bin(pos))
            for z in range(len(bin(pos))-1, 0, -1):
                bin_pos.append(bin(pos)[z])
            #print(bin_pos, "---", bin(pos))
            try:
                if bin_pos[x] == '1' and y != 'X':
                    if y == '1':
                        cant_1 += 1
                    else:
                        cant_0 += 1
                    bajados.append(y)
                    #print(f"Bajar {y}, en la {x} vuelta y posicion {bin(pos)}")
            except:
                pass

            pos += 1

        if cant_1 % 2 != 0:
            #print(f"Uno de paridad", end=" ")
            codigo.append("1")
        else:
            #print("Cero de paridad", end=" ")
            codigo.append("0")

        #print(f"{bajados} contiene {cant_1} unos y {cant_0} ceros")
    #print(codigo, end="  ")
    # print(hamming)
    count = 0
    count_1 = 0
    for x in hamming:
        if x == "X":
            hamming[count] = codigo[count_1]
            count_1 += 1
        count += 1
    # print(hamming)
    code = ''
    for x in codigo:
        code = code + x
    hamm = ''
    for x in hamming:
        hamm = hamm + x

    print(f"Mensaje: \t{mensaje}\nCodigo: \t{code}\nHamming: \t{hamm}")
    return mensaje, code, hamm


def get_hamming(hamming):
    # Función que toma como parametro un mensaje codificado y devuelve el mensaje corregido
    hamming = hamming
    codigo = ''
    mensaje = ''
    count = 1
    pos_potencia = 1
    pos = 1
    for x in hamming:
        #print(pos, "---", pos_potencia)
        if pos == pos_potencia:
            pos_potencia = 2**count
            count += 1
            codigo = codigo + x
        else:
            mensaje = mensaje + x
        # print(x)
        pos += 1
    # print(hamming)
    # print(f"{codigo}---{mensaje}")
    return mensaje, codigo, hamming


def comparador(codigo1, codigo2):
    # Función que compara los codigos hamming.
    count = 0
    binario = []
    for x in codigo1:

        if x == codigo2[count]:
            binario.append('0')
        else:
            binario.append('1')
        count += 1
    # print(binario)
    num_bin = ''
    count = 0
    dec = 0
    for x in binario:
        if x == '1':
            dec = (2 ** count) + dec
        count += 1
    if dec == 1:
        print("No existe error")
    else:
        print(f"Error en la posición '{dec}' ⚠")
        return dec


def corrector(mensaje, indice):
    mensaje = mensaje
    hamming = []
    for x in mensaje:
        hamming.append(x)
    for x in range(0, len(hamming)):
        if x+1 == indice:
            if hamming[x] == "1":
                hamming[x] = "0"
            else:
                hamming[x] = "1"
    mensaje = ''
    for x in hamming:
        mensaje = mensaje + x
    print(f"Mensaje corregido: {mensaje} ✔ ")
    return mensaje


if __name__ == "__main__":
    # hamming('0110')
    mensaje = get_hamming("1100100")
    codigo1 = mensaje[1]
    codigo2 = hamming(mensaje[0])[1]
    error = comparador(codigo1, codigo2)
    correcto = corrector(mensaje[2], error)
