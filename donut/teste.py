import math
import time

A = 0
B = 0
while True:
    z = [0]*1760
    b = [' ']*1760
    for j in range(0,628,int(0.07*100)):
        j /= 100
        for i in range(0,628,int(0.02*100)):
            i /= 100
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= o < 1760:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

    print('\x1b[H' + ''.join(b))
    time.sleep(0.01)
    A += 0.04
    B += 0.02
