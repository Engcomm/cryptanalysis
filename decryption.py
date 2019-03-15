
# ###Decryption### #

import math

# take ciphertext input

ciphertext = raw_input("Enter a ciphertext to be decrypted : ")

# letters array

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z']

# ciphertext without special characters, numbers and spaces

lettersOnlyCiphertext = '' # to be the input to count each letter frequency

for character in ciphertext:
    if character in letters:
	lettersOnlyCiphertext += character

# define function to calculate each letter's frequency percentage

def percentage(count, total):

    return 100 * float(count) / total

lettersFrequencyPercentages = [] # to store each letter's frequency percentage

# calculate each letter's frequency percentage


#delete spaces from ciphertext
numberOfLettersInCiphertext = len(lettersOnlyCiphertext) ############## apply on ciphertext without special characters instead

for letter in letters:
    lettersFrequencyPercentages.append(percentage(lettersOnlyCiphertext.count(letter), numberOfLettersInCiphertext))

# The standard frequencies and percentages of English letters

standardEnglishLettersFrequenciesPercentages = [7.487792, 1.295442, 3.544945, 3.621812, 13.99891, 2.183939, 1.73856,
                                                4.225448, 6.653554, 0.269036, 0.465726, 3.569814, 3.39121, 6.741725,
                                                7.372491, 2.428106, 0.262254, 6.140351, 6.945198, 9.852595,
                                                3.004612, 1.157533, 1.691083, 0.278079, 1.643606, 0.036173]

# calculate correlation coefficient for each possible shift key

shiftsCorrelationCoefficients = []  # to store the co-eff of each shift key

for shift in range(0,26):  # 26 shifts .. ( 26 in range will be ignored )

    r = (
        26 * (
            sum([
                     (x * y)
                     for (x, y) in zip(standardEnglishLettersFrequenciesPercentages, lettersFrequencyPercentages[shift:])
                     #                                             #get y from the index as the shift to the last index
                     ])
            + sum([
                     (x * y)
                     for (x, y) in zip(standardEnglishLettersFrequenciesPercentages, lettersFrequencyPercentages[0:shift])
                     #                           #get y from the first index to the index before the index as the shift
                     ])
        )
    - sum([x for x in standardEnglishLettersFrequenciesPercentages])
    * (
            sum([y for y in lettersFrequencyPercentages[shift:]]) + sum([y for y in lettersFrequencyPercentages[0:shift]])
    ))/(
        math.sqrt(
            26 * sum([math.pow(x, 2) for x in standardEnglishLettersFrequenciesPercentages])
            - math.pow(sum([x for x in standardEnglishLettersFrequenciesPercentages]), 2)
        )
        *
        math.sqrt(
            26 * (
                sum([math.pow(y, 2) for y in lettersFrequencyPercentages[shift:]])
                + sum([math.pow(y, 2) for y in lettersFrequencyPercentages[0:shift]])

            )
            - math.pow(
                (
                    sum([y for y in lettersFrequencyPercentages[shift:]])
                    + sum([y for y in lettersFrequencyPercentages[0:shift]])

                ), 2
            )
        )

    )

    # add this shift's correlation coefficient to the list
    shiftsCorrelationCoefficients.append(r)


# the shift key is the key with the max value

shiftKey = shiftsCorrelationCoefficients.index(max(shiftsCorrelationCoefficients))
print " \nshiftKey : " + str(shiftKey)

# Deciphering

plaintext = ""

for i in range(0, len(ciphertext)):  # loop over all ciphertext characters

    if ciphertext[i] == ' ':  # space
        plaintext += ' '

    elif ciphertext[i] not in letters:  # any character other than letters and spaces

        # print the same character
        plaintext += ciphertext[i]

    else:  # letter
        index = letters.index(ciphertext[i])  # get index of character in letters

        plaintext += letters[index - int(shiftKey)]

# print the result
print " \nplaintext : " + plaintext

