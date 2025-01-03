alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','x','y','z']



def encrypt(text,shift):
    encrypt_words=""
    for i in text:
        b=alphabets.index(i)+shift
        b %= len(alphabets) 
        encrypt_words+=alphabets[b]
    print(f"Here is your encrypted word {encrypt_words}.")

# encrypt(text,shift)

def decrypt(text,shift):
    decrypt_word=""
    for i in text:
        b=alphabets.index(i)-shift
        b %= len(alphabets)
        decrypt_word +=alphabets[b]
    print(f"Here is your decrpyt word {decrypt_word}.")

# decrypt(text,shift)


def caeser(direction,text,shift):
    output_text=""
    if direction=='decode':
            shift*=-1
    for i in text:
        if i not in text:
            output_text+=i
        else:
            b=alphabets.index(i)+shift
            b %=len(alphabets)
            output_text += alphabets[b]
    print(f"Here is {direction} result: {output_text}")



should_run=True 
while should_run:
    direction=input("Type 'encode' to encrypt or type 'decode' to decrypt:\n").lower()
    text=input("Type your messgae:\n").lower()
    shift= int(input("Type the shift number:\n"))

    caeser(direction,text,shift)
    message=input("Do you want to go again then type 'yes' if not then then type 'no'").lower()
    if message == 'no':
        should_run=False
        





