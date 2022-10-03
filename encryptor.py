# Import the message_to_encrypt.txt file
import pandas as pd
with open("message_to_encrypt.txt") as f:
    df = f.read()
    
df = df.strip("\n").replace("\n", "*")

p = 23
q = 29
n = p*q
r = (p-1)*(q-1)

# import math
# math.gcd(r,3)

e = 3
i = 2
# public_key: n = 667 and e = 3

d = int((i*r + 1)/e)
# private_key: d = 411

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
          "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", ".", "*"]
translation = [*range(1, 31)]

dictionary = dict(zip(letter, translation))

translate = [dictionary[i] for i in [*df]]  

cipher = [element ** e % n for element in translate]

# Save the cipher to a file called "cipher.txt"
with open('cipher.txt', 'w') as fp:
    for item in cipher:
        # write each item on a new line
        fp.write("%s\n" % item)


# Save the private key as the "private_key.txt" file
with open('private_key.txt', 'w') as f:
    f.write('{}'.format(d))
    f.close()

# Save the number n as the "n.txt" file
with open('n.txt', 'w') as f:
    f.write('{}'.format(n))
    f.close()
