# Import encryptor.py
import encryptor

# Import the cipher.txt file
with open("cipher.txt") as f:
    cipher = f.readlines()
cipher = [int(x) for x in cipher]

# Import the private_key.txt file
with open("private_key.txt") as f:
    d = int(f.read())

# Import the n.txt file
with open("n.txt") as f:
    n = int(f.read())
    

# Step 4
# Decrypt the message in cipher
decrypt = [element ** d % n for element in cipher]


def get_key(val):
    """
    to return key for a list for any value
    input = value of any type
    output = keys to corresponding values from a dictionary
    """
    for key, value in encryptor.dictionary.items():
        if val == value:
            return key
 
    return "key doesn't exist"


dec_lst = []
for i in decrypt:
    dec_lst.append(get_key(i))
    
message = "".join([str(i) for i in dec_lst])
message = message.split("*")


# Save the decrypted message to a file called "decrypted_message.txt"
with open('decrypted_message.txt', 'w') as f:
    for item in message:
        # write each item on a new line
        f.write("%s\n" % item)
    f.close()
