import numpy as np
from numpy.linalg import det
import sympy

alph = "abcdefghijklmnopqrstuvwxyz, ."
n = 0

def encrypt(text, K1, K2):
    encrypted = ''
    
    curK = K1
    for i in range(0, len(text), n):

        
        if i == n:
            curK = K2
        elif i == 2 * n:
            curK = K2.dot(K1)
        elif i:
            K1 = K2
            K2 = curK
            curK = K2.dot(K1)

        block = text[i:i+n]
        if len(block) == 0:
            break
        block = [alph.index(c) for c in block]
        while len(block) < n:
            block.append(alph.index(' '))
        
        block = np.matrix(block).T
        encArr = curK.dot(block).reshape((1,n)).tolist()[0] 
        encArr = [i % len(alph) for i in encArr]
        
        encrypted += ''.join([alph[i] for i in encArr])
    
    return encrypted            

def decrypt(text, K1, K2):
    decrypted = ''

    curK = K1

    for i in range(0, len(text), n):

        if i == n:
            curK = K2
        elif i == 2 * n:
            curK = K2.dot(K1)
        elif i:
            K1 = K2
            K2 = curK
            curK = K2.dot(K1)

        block = text[i:i+n]
        if len(block) == 0:
            break
        block = [alph.index(c) for c in block]
        while len(block) < n:
            block.append(alph.index(' '))
        
        inversedK = np.matrix(sympy.Matrix(curK).inv_mod(len(alph)))
        block = np.matrix(block).T
        encArr = inversedK.dot(block).reshape((1,n)).tolist()[0]
        encArr = [i % len(alph) for i in encArr]
        
        decrypted += ''.join([alph[i] for i in encArr])
    
    return decrypted            



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
