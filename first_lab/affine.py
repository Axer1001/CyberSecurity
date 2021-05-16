import math

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
m = len(alph)


def encrypt(text, a, b):
    res = ''
    for i in range(len(text)):
        if text[i] == ' ':
            res += ' '
            continue
        res += alph[((a * alph.index(text[i]) + b)) % m]
    return res

def decrypt(encryptedText, a, b):
    res = ''
    inverseA = pow(a, -1, m)
    for i in range(len(encryptedText)):
        if encryptedText[i] == ' ':
            res += ' '
            continue
        res += alph[(inverseA * (alph.index(encryptedText[i]) - b)) % m]
    return res

def main():
    s = input("Enter text: ")    
    mode = int(input("Encrypt/Decrypt [1/2]: "))
    a, b = tuple(map(int, input('Enter coprime integers A and B: ').split())) 
    if math.gcd(a,b) != 1:
        print("Error: A and B are not coprime!")
        exit(1)
    if mode == 1:
        enc = encrypt(s, a, b)
        print("Encrypted: %s" % enc)
    if mode == 2:
        print("Decrypted: %s" % decrypt(s, a, b))     

if __name__ == "__main__": 
    main()
