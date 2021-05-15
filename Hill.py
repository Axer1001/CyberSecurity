import numpy as np
from numpy.linalg import det

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
        
        block = np.matrix(block)
        encArr = block.dot(K).tolist()[0]
        encArr = [i % len(alph) for i in encArr]
        
        encrypted += ''.join([alph[i] for i in encArr])
    return encrypted            

def decrypt(text, K):
    dt = det(K)
    inverseDt = pow(int(dt), -1, len(alph))
    algD = K.getI() * dt * inverseDt
    K = algD % len(alph)
    newK = []
    for r in K.A:
        r = [int(round(i)) for i in r]
        newK.append(r)

    return encrypt(text, np.matrix(newK))
        

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
