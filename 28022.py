from math import *

a = [1]*100000
def sang():
    a[0] = 0; a[1] = 0
    for i in range(2,isqrt(100000)+1):
        if(a[i]==1):
            for j in range(i*i, 100000, i):
                a[j] = 0

if __name__ == '__main__':
    sang()
    print('(2,3)', end = ' ')
    for i in range(10001):
        if(a[i]==1 and a[i+2]==1):
            print('(',i,',',i+2,')', sep = '',end = ' ')
        