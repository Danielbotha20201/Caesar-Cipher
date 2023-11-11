# Functions
def encrypt_decrypt(question):

  while True:
    response = input(question).lower()
    
    if response == "decrypt" or response == "d":
      return "decrypt"

    elif response == "encrypt" or response == "e":
      return "encrypt"

    else:
      print ("Please enter Encrypt or Decrypt")

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

# Main code

response = encrypt_decrypt("Would like to Encrypt or Decrypt? ")
    
if response == "encrypt":
  message = input("Please enter your message here: ")
  key = int(input("Please enter shift key: "))

print("Encrypted Text is : " + str(encrypt_text(message,key)))
