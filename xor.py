xor = open('xor.txt', 'a+')
for y in range(50):
    xor.write(''.join([str(hex(x ^ y))[2] for x in range(50)]) + '\n')
