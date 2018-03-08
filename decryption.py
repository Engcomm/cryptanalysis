
import nltk

####Decryption####

# take cyphertext input

ciphertext = raw_input("Enter a cyphertext to be decrypted :")

print ciphertext

# letters array

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


## get frequency of each letter in ciphertext

lettersFrequency = [] # to store each letter frequency in ciphertext

# calculate each letter frequency
for letter in letters :
    lettersFrequency.append(ciphertext.count(letter))

print lettersFrequency

#define function to calculate each letter's frequency percentage
def percentage(count, total):
    return 100 * float(count) / total

lettersFrequencyPercentages = [] #to store each letter's frequency percentage

#calculate each letter's frequency percentage
for letter in letters:
    lettersFrequencyPercentages.append(percentage(ciphertext.count(letter), len(ciphertext)))

print lettersFrequencyPercentages



