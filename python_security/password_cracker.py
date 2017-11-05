'''
2 functions: main and testpass
- main:
	- opens the encrypted password file “passwords.txt”
	- reads the contents of each line in the password file
	- for each line, it splits out the username and the hashed password
	- for each individual hashed password, the main function calls the testPass() function that tests passwords against a dictionary file.

- testpass: 
	- takes the encrypted password as a parameter
	- returns either after finding the password or exhausting the words in the dictionary
	
	- strips out the salt from the first two characters of the encrypted password hash
	- opens the dictionary and iterates through each word in the dictionary
	- creating an encrypted password hash from the dictionary word and the salt
	- if the result matches our encrypted password hash, the function prints a message indicating the found password and returns
	- otherwise, it continues to test every word in the dictionary
'''

import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		if (cryptWord == cryptPass):
			print "[+] Found Password: "+word+"\n"
			return

	print "[-] Password Not Found.\n"
	return

def main():
	passFile = open('passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking Password For: "+user
			testPass(cryptPass)

if __name__ == "__main__": 
	main()
