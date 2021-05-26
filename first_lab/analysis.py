
freq = dict()
l = 0


while True:
    try:
        s = input()
    except:
        break
    for c in s:
    
        if not c.isalpha():
            continue

        if c.lower() not in freq:
            freq[c.lower()] = 0
    
        freq[c.lower()] += 1
        l += 1


for c in freq:
        freq[c] /= l

its = list(freq.items())
its.sort(key= lambda x: -x[1])

for i in its:
    print(i)
