alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#double alhabet to handle edge cases where zzz will be out of range. This makes it llop back to A if it even goes above index 25

should_continue = True
while should_continue == True: 
    method = input("Type encrypt to Encrypt a message. Type decrypt to Decrypt a message. ").lower()
    prompt = input("Enter your message: ")
    shift = int(input("Enter the number of shifted values: "))
    shift = shift % 26

    def cipher(text, shift_amount, method):
        cipher_text=""
        if method == "decrypt":
            shift_amount *= -1
        for letter in text:
            position = alphabet.index(letter)  #will get the index of letter in the alphabet list
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter

        print(cipher_text)

    cipher(prompt, shift, method)

    continued = input("Do you want to try again? ").lower()
    if continued == "no":
        should_continue = False