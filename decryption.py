

####Decryption####

# take ciphertext input

ciphertext = raw_input("Enter a ciphertext to be decrypted : ")

print ciphertext

# letters array

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z']


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

numberOfLettersInCiphertext = len(''.join(ciphertext.split()))

print  numberOfLettersInCiphertext

for letter in letters:
    lettersFrequencyPercentages.append(percentage(ciphertext.count(letter), numberOfLettersInCiphertext)))

print lettersFrequencyPercentages


# The standard frequencies and percentages of English letters

standardEnglishLettersFrequenciesPercentages = [7.487792,1.295442,3.544945,3.621812,13.99891,2.183939,1.73856,
                                                4.225448,6.653554,0.269036,0.465726,3.569814,3.39121,6.741725,
                                                7.372491,2.428106,0.262254,6.140351,6.945198,9.852595,
                                                3.004612,1.157533,1.691083,0.278079, 1.643606, 0.036173]


