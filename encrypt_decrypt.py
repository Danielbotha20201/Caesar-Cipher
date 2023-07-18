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