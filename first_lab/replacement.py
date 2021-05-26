alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = [i for i in range(26)]

def encrypt(text):
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            res += ' '
            continue
        res += alph[key[alph.index(text[i].lower())]]
    return res
    
def decrypt(encryptedText):
    res = ''
    for i in range(len(encryptedText)):
        if not encryptedText[i].isalpha():
            res += ' '
            continue
        res += alph[key.index(ord(encryptedText[i]) - ord('a'))]
    return res

def main():
    s = input("Enter text: ")
    a = int(input("Encrypt/Decrypt [1/2]: "))
    global key
    key = list(map(int, input("Enter key: ").split()))
    if a == 1:
        enc = encrypt(s)
        print("Encrypted: %s" % enc)
    if a == 2:    
        print("Decrypted: %s" % decrypt(s))

if __name__ == "__main__":
    main()

