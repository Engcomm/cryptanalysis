
# ### Encryption ### #

# take msg input

msg = raw_input("Enter a msg to be encrypted : ")

# take shift input

shift = raw_input("Enter shift : ")

# letters array

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ciphertext = ""

# encryption

for i in range(0, len(msg)):  # loop over all msg characters

    if msg[i] == ' ':
        ciphertext += ' '

    elif msg[i] not in letters:  # any other character
        # print the same character
        ciphertext += msg[i]

    else:  # letter
        index = letters.index(msg[i])  # get index of character in letters

        ciphertext += letters[(index + int(shift)) % 26]

print "\nciphertext is : " + ciphertext



