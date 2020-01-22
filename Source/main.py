def writeToFile(account):
    theFile = open("accounts.txt", "a")
    theFile.write(account)
    theFile.write('\n')

def convert(username, password):
    result = username + ":" + password
    return result

while True:
    usr = input("Enter Username: ")
    psswrd = input("Enter Password: ")

    if usr == 'x':
        break
	
	
writeToFile(convert(usr, psswrd))
print("Done\n")
