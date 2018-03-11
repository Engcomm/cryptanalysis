

import math

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
    lettersFrequencyPercentages.append(percentage(ciphertext.count(letter), numberOfLettersInCiphertext))

print lettersFrequencyPercentages


# The standard frequencies and percentages of English letters

standardEnglishLettersFrequenciesPercentages = [7.487792,1.295442,3.544945,3.621812,13.99891,2.183939,1.73856,
                                                4.225448,6.653554,0.269036,0.465726,3.569814,3.39121,6.741725,
                                                7.372491,2.428106,0.262254,6.140351,6.945198,9.852595,
                                                3.004612,1.157533,1.691083,0.278079, 1.643606, 0.036173]

shiftsCorrelationCoefficients = [] # to store the co-eff of each shift



for shift in range(0,26) : # 26 shifts .. ( 26 in range will be ignored )


    r = (
        26 * sum([
                     (x * y)
                     for (x, y) in zip(standardEnglishLettersFrequenciesPercentages, lettersFrequencyPercentages)
                     ])
    - sum([x for x in standardEnglishLettersFrequenciesPercentages])
    * sum([y for y in lettersFrequencyPercentages])
    )/(
        math.sqrt(
            26 * sum([math.pow(x , 2) for x in standardEnglishLettersFrequenciesPercentages])
            - math.pow( sum([x for x in standardEnglishLettersFrequenciesPercentages]) , 2)
        )
        *
        math.sqrt(
            26 * sum([math.pow(y, 2) for y in lettersFrequencyPercentages])
            - math.pow(sum([y for y in lettersFrequencyPercentages]), 2)
        )

    )

    print "r "
    print r


























'''
    if shift ==0 :
        end = ''
    else:

        end = shift  # to end the iteration over letters

    #calculate the coeff for each shift key
    r = 26 * sum([
                     (x*y) for (x,y) in zip(standardEnglishLettersFrequenciesPercentages[:] , lettersFrequencyPercentages[shift:end])
                   ])


    #add r to shiftsCorrelationCoefficients list
    shiftsCorrelationCoefficients.append(r)



print "shiftsCorrelationCoefficients "
print shiftsCorrelationCoefficients

'''







