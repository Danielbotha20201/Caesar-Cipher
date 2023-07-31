def encrypt_decrypt(question):

  while True:
    response = input(question).lower()
    
    if response == "decrypt" or response == "d":
      return "decrypt"

    elif response == "encrypt" or response == "e":
      return "encrypt"

    else:
      print ("Please enter Encrypt or Decrypt")

def encrypt_text(input,n):
    ans = ""
    # iterate over the given text
    for i in range(len(input)):
        ch = input[i]
        
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


response = encrypt_decrypt("Would like to Encrypt or Decrypt? ")
    
if response == "encrypt":
  print("encrypt goes here")
  
  input = input().lower()
n = 1
print("Plain Text is : " + input)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(input,n))
