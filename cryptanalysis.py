
#### Encryption ####

#take msg input

msg = raw_input("Enter a msg to be encrypted")

print msg

#take shift input

shift = raw_input("Enter shift")

print shift

# letters array

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipherText = ""


# encryption

for i in range(0,len(msg)): # loop over all msg characters

    index = letters.index(msg[i]) #get index of character in letters
    print index

    cipherText += letters[index+int(shift)]

    print cipherText





