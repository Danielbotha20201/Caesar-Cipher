# functions

# Encrypts users message
def encrypt_text(message,key):
    ans = ""
    # iterate over the given text
    for i in range(len(message)):
        ch = message[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + key-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + key-97) % 26 + 97)
    
    return ans
  
# Checks user has entered yes/no to a question
def yes_no(question2):

  while True:
    yes_no = input(question2).lower()
    
    if yes_no == "yes" or yes_no == "y":
        return "yes"

    elif yes_no == "no" or yes_no == "n":
        return "no"

    else:
        print ("Please enter yes or no")
    
# Checks if users wants to Encrypt or Decrypt
def encrypt_decrypt(question):
  while True:
    response = input(question).lower()

    if response == "decrypt" or response == "d":
      return "decrypt"
    elif response == "encrypt" or response == "e":
      return "encrypt"
    else:
      print ("Please enter Encrypt or Decrypt")

# Decrypts users message based of key
def decrypt():
    
    decrypted_message = ""
  
    key = int(input("Enter key to decrypt: "))
    

    for c in message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    
    print(decrypted_message)

# Main code

import string

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

response = encrypt_decrypt("Would you like to Encrypt or Decrypt? ")
    
if response == "encrypt":
  message = input("Please enter your message here: ")
  key = int(input("Please enter shift key: "))

  print("Encrypted Text is : " + str(encrypt_text(message,key)))
  

if response == "decrypt":
  
  Letters = 'abcdefghijklmnopqrstuvwxyz'
  message = input("Please enter your encrypted message here: ").lower()
 
  if yes_no("do you have the shift key? ") == "yes":
    decrypt()
    

    
  else:
     
      for key in range(len(Letters)):
         translated = ''
         for ch in message:
            if ch in Letters:
               num = Letters.find(ch)
               num = num - key
               if num < 0:
                  num = num + len(Letters)
               translated = translated + Letters[num]
            else:
               translated = translated + ch
         print('Hacking key is %s: %s' % (key, translated))

exit()