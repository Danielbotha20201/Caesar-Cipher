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

def encrypt_text(my_input,n):
    ans = ""
    # iterate over the given text
    for i in range(len(my_input)):
        ch = my_input[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

# Main code

response = encrypt_decrypt("Would like to Encrypt or Decrypt? ")
    
if response == "encrypt":
  my_input = input("Please enter code here: ")
  n = int(input("Please enter shift key: "))
print("Plain Text is : " + my_input)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + str(encrypt_text(my_input,n)))
