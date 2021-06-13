import numpy as np
from numpy.linalg import det
import sympy

alph = "abcdefghijklmnopqrstuvwxyz, ."
n = 0
def encrypt(text, K):
    encrypted = ''

    for i in range(0, len(text), n):
        block = text[i:i+n]
        if len(block) == 0:
            break
        block = [alph.index(c) for c in block]
        while len(block) < n:
            block.append(alph.index(' '))
        
        block = np.matrix(block).T
        encArr = K.dot(block).reshape((1,n)).tolist()[0]
        encArr = [i % len(alph) for i in encArr]
        
        encrypted += ''.join([alph[i] for i in encArr])
    return encrypted            

def decrypt(text, K):
    K = sympy.Matrix(K)
    return encrypt(text, np.matrix(K.inv_mod(len(alph))))
        

s = input('Enter text: ')
e = int(input('Encrypt/Decrypt [0/1]: '))

n = int(input('Matrix size: '))
K = []
print('Enter key:')
for i in range(n):
    K.append(list(map(int, input().split())))
    
K = np.matrix(K)
if e == 0:    
    print(encrypt(s, K))
elif e == 1:
    print(decrypt(s, K))
