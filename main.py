import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, direction_value):
    if direction_value == "encode":
        cipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                shifted_index = (alphabet.index(letter) + shift_amount) % 26
                new_letter = alphabet[shifted_index]
                cipher_text += new_letter
            else:
                cipher_text += letter
        print(cipher_text)
    elif direction_value == "decode":
        decipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                shifted_index = abs(26 + alphabet.index(letter) - shift_amount) % 26
                new_letter = alphabet[shifted_index]
                decipher_text += new_letter
            else:
                decipher_text += letter
        print(decipher_text)


print(art.logo)
restart = "yes"

while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text= text, shift_amount= shift, direction_value= direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if restart == "no":
        print("Goodbye")