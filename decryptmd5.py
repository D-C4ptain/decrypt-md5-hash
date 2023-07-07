import pyfiglet         # Disclaimer: This script is for educational purposes only.
import sys                              
import hashlib

def disp():
    print("\n"+"*"*65) 
    print(pyfiglet.figlet_format("          Dcap-Md5"))
    print("*\t\t\t\tD-c4ptain\t\t\t\t*")
    print("*\t\t    Dcaptainkenya@gmail.com\t\t\t*")
    print("*\t      https://www.D-captainkenya.github.io\t\t*")
    print("*"*65)
    print("\nDecrypt MD5 Hashes with wordlist")
    print("\n"+"-"*50)
    args()

def usage():
    print("\nplease specify md5hash and wordlist correctly!")
    print("\nUSAGE:")
    print("\tpython crackmd5hash.py md5hash wordlistpath")
    print("EXAMPLE\n\tPython crackmd5hash.py ab334feeb31c05124cb73fa12571c2f6 /home/worldist.txt\n")
    print("\tPython crackmd5hash.py ab334feeb31c05124cb73fa12571c2f6 D:\\myfiles\welcome.txt\n")
    sys.exit(0)

def args():
    try:
        n = len(sys.argv)
        if n < 1:
            usage()
        elif n > 2:
            work(sys.argv[1], sys.argv[2])
        else:
            usage()
    except KeyboardInterrupt:
        print("\nKeyboard interrupted. \nExiting...")
        sys.exit(0)

def work(phash, wlist):
    f = False
    try:
        passfile = open (wlist, "r")
    except:
        print("Wordlist Not Found !!")
        usage()
        sys.exit(0) 
    print("working....")
    for word in passfile:
        enc_wrd = word.encode('utf-8')
        digest  = hashlib.md5(enc_wrd.strip()).hexdigest()
        if digest == phash:
            print(f"\nFound A Match for '{digest}'")
            print("The Plaintext Is: " +word)
            f = True
            break
    if f == False:
        print("\nPlaintext Not Found In Wordlist,\nTry A Different List\n")
    
if __name__ == "__main__":
    disp()
