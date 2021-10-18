import hashlib

flag = 0

pass_hash = input("Enter an md5 hash: ")
wordlist  = input("Enter wordlist file name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found !!")
    quit() 

for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest  = hashlib.md5(enc_wrd.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)

    if digest == pass_hash:
        print("Password Found")
        print("The password is " +word)
        flag = 1
        break
if flag == 0:
    print("Password Not Found In The List, Try A Better List")
    
