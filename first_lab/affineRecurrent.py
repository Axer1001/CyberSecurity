import math

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
m = len(alph)


def encrypt(text, a1, b1, a2, b2):
    res = ''
    aCur, bCur = a1, b1
    for i in range(len(text)):
        if (i == 1):
            aCur, bCur = a2, b2
        elif i == 2:
            aCur, bCur = (a1 * a2) % m, (b1 + b2) % m
        elif i:
            a1, b1 = a2,b2
            a2, b2 = aCur, bCur
            aCur, bCur = (a1 * a2) % m, (b1 + b2) % m

        if text[i] == ' ':
            res += ' '
            continue
        res += alph[((aCur * alph.index(text[i]) + bCur)) % m]
    return res

def decrypt(encryptedText, a1, b1, a2, b2):
    res = ''
    aCur, bCur = a1, b1
    for i in range(len(encryptedText)):
        if (i == 1):
            aCur, bCur = a2, b2
        elif i == 2:
            aCur, bCur = (a1 * a2) % m, (b1 + b2) % m
        elif i:
            a1, b1 = a2,b2
            a2, b2 = aCur, bCur
            aCur, bCur = (a1 * a2) % m, (b1 + b2) % m
        

        if encryptedText[i] == ' ':
            res += ' '
            continue
        inverseA = pow(aCur, -1, m)
        res += alph[(inverseA * (alph.index(encryptedText[i]) - bCur)) % m]
    return res

def main():
    s = input("Enter text: ")    
    mode = int(input("Encrypt/Decrypt [1/2]: "))
    a1, b1, a2, b2 = tuple(map(int, input('Enter key pairs (a1, b1) and (a2, b2): ').split())) 
    
    if mode == 1:
        enc = encrypt(s, a1, b1, a2, b2)
        print("Encrypted: %s" % enc)
    if mode == 2:
        print("Decrypted: %s" % decrypt(s, a1, b1, a2, b2))     

if __name__ == "__main__": 
    main()
