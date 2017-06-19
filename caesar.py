# task from: http://hack.engeto.com/caesar

import string
def caesar_cipher2(message, password, mode):
    words = message.split()
    abc = string.ascii_lowercase+string.ascii_uppercase
    result = ""
    if mode == 'encrypt':
        for word in words:
            for character in word:
                positionOfCharInMessage = abc.index(character)
                result += abc[(positionOfCharInMessage + password) % len(abc)]
            result += " "
        print(result[:len(result)-1])
    if mode == 'decrypt':
        for word in words:
            for character in word:
                positionOfCharInMessage = abc.index(character)
                result += abc[(positionOfCharInMessage - password) % len(abc)]
            result += " "
        print(result[:len(result)-1])

#caesar_cipher2("abcdefXYZ abcd ijklm OPQRS",50,"encrypt")
#caesar_cipher2("Python Engeto and Kiwi Hackathon", 1,'encrypt')
#print()
#caesar_cipher2("YZabcdVWX YZab ghijk MNOPQ",50,"decrypt")
#caesar_cipher2("Qzuipo Fohfup boe Ljxj Ibdlbuipo", 1,'decrypt')




def caesar_cipher_witch_special_chars(message, password, mode):
    # lower to lower, upper to upper, special character and spaces stay on original positions
    result = ""
    lowerLetters = string.ascii_lowercase
    upperLetters = string.ascii_uppercase

    if mode == 'encrypt':
        for character  in message:
            if character in lowerLetters or character in upperLetters:
                if character in lowerLetters:
                    positionOfCharInMessage = lowerLetters.index(character)
                    result += lowerLetters[(positionOfCharInMessage + password) % len(lowerLetters)]
                else:
                    # character in upper
                    positionOfCharInMessage = upperLetters.index(character)
                    result += upperLetters[(positionOfCharInMessage + password) % len(upperLetters)]
            else:
                result += character
    if mode == 'decrypt':
        for character  in message:
            if character in lowerLetters or character in upperLetters:
                if character in lowerLetters:
                    positionOfCharInMessage = lowerLetters.index(character)
                    result += lowerLetters[(positionOfCharInMessage - password) % len(lowerLetters)]
                else:
                    # character in upper
                    positionOfCharInMessage = upperLetters.index(character)
                    result += upperLetters[(positionOfCharInMessage - password) % len(upperLetters)]
            else:
                result += character




    return result

# caesar_cipher_witch_special_chars("Python Engeto and Kiwi.com Hackathon. Python FTW!!!",50,"encrypt")
# caesar_cipher_witch_special_chars("Nwrfml Clecrm ylb Igug.amk Fyaiyrfml. Nwrfml DRU!!!",50,"decrypt")

src = open("my_result.txt","r")
out = open("my_file.txt","w")
for line in src.readlines():
    #out.write(caesar_cipher_witch_special_chars(line, 50, "encrypt"))
    out.write(caesar_cipher_witch_special_chars(line, 50, "decrypt"))
src.close()
out.close()