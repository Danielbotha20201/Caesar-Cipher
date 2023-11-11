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

response = encrypt_decrypt("Would like to Encrypt or Decrypt? ")
    
if response == "decrypt":
  message = input("Please enter your encrypted message here: ")
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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