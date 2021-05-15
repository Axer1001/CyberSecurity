import numpy as np
from numpy.linalg import det

alph = "abcdefghijklmnopqrstuvwxyz, ."
n = 0
def encrypt(text, K1, K2):
    encrypted = ''
    
    curK = K1
    for i in range(0, len(text), n):
        block = text[i:i+n]
        if len(block) == 0:
            break
        block = [alph.index(c) for c in block]
        while len(block) < n:
            block.append(alph.index(' '))
        
        block = np.matrix(block)
        encArr = block.dot(curK).tolist()[0]
        encArr = [i % len(alph) for i in encArr]
        
        encrypted += ''.join([alph[i] for i in encArr])

        if i == n:
            curK = K2
        elif i == 2 * n:
            curK = K1.dot(K2)
        else:
            curK, K1, K2 = K1.dot(K2), K2, curK
    
    return encrypted            

def inv(K):
    dt = det(K)
    inverseDt = pow(int(dt), -1, len(alph))
    
    algD = K.getI() * dt * inverseDt
    K = algD % len(alph)
    newK = []
    for r in K.A:
        r = [int(round(i)) for i in r]
        newK.append(r)
    return np.matrix(newK)

def decrypt(text, K1, K2):
    return encrypt(text, inv(K1), inv(K2))

s = input('Enter text: ')
e = int(input('Encrypt/Decrypt [0/1]: '))

n = int(input('Matrix size: '))
K1 = []
K2 = []

print('Enter key:')
for i in range(n):
    K1.append(list(map(int, input().split())))

print('Enter second key: ')
for i in range(n):
    K2.append(list(map(int, input().split())))

K1 = np.matrix(K1)
K2 = np.matrix(K2)

if e == 0:    
    print(encrypt(s, K1, K2))
elif e == 1:
    print(decrypt(s, K1, K2))
