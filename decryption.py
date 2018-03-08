
import nltk

####Decryption####

# take cyphertext input

ciphertext = raw_input("Enter a cyphertext to be decrypted :")

print ciphertext

# letters array

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# get frequency of each letter in ciphertext  -> use nltk

lettersFrequency = []

for letter in letters :
    lettersFrequency.append(ciphertext.count(letter))

print lettersFrequency

def percentage(count, total):
    return 100 * float(count) / total

print percentage(ciphertext.count('a'), len(ciphertext))



