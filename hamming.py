mensaje = '0110'
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
print(codigo, end="  ")
print(hamming)
count = 0
count_1 = 0
for x in hamming:
    if x == "X":
        hamming[count] = codigo[count_1]
        count_1 += 1
    count += 1
print(hamming)
