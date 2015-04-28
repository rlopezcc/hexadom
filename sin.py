import math

f = open('sin.txt', 'a+')
for y in range(50):
    f.write(''.join([str(hex(int(math.sin(x) * 6) + 10))[2]
                     for x in range(50)]) + '\n')
