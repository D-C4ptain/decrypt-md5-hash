import md5

counter = 1

pass_hash = raw_input("Enter the md5 hash: ")
file      = raw_input("Enter password file name: ")

try: 
    file = open(file, "r")
except:
    print "\nThe File Was Not Found!!"
    quit()

for password in file:
    md5hash = md5.new(password.strip()).hexdigest()
print "Attempting Password Number %d: %s " % (counter, password.strip())

counter += 1

if pass_hash == md5hash:
    print "\nPassword Revealed. \nThe Password Is: %s" % password
    break

else: 
    print "\nPassword Not Found, Try A Better File."
    
