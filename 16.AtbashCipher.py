# Python program to implement Atbash Cipher

# This script uses dictionaries to lookup various alphabets
lookup_table = {'A' : 'Z' , 'B' : 'Y' , 'C' : 'X' , 'D' : 'W' , 'E' : 'V' ,
                'F' : 'U' , 'G' : 'T' , 'H' : 'S' , 'I' : 'R' , 'J' : 'Q' ,
                'K' : 'P' , 'L' : 'O' , 'M' : 'N' , 'N' : 'M' , 'O' : 'L' ,
                'P' : 'K' , 'Q' : 'J' , 'R' : 'I' , 'S' : 'H' , 'T' : 'G' ,
                'U' : 'F' , 'V' : 'E' , 'W' : 'D' , 'X' : 'C' , 'Y' : 'B' , 'Z' : 'A'}


def atbash(message) :
	cipher = ''
	for letter in message :
		# checks for space
		if (letter != ' ') :
			# adds the corresponding letter from the lookup_table
			cipher += lookup_table [letter]
		else :
			# adds space
			cipher += ' '
	
	return cipher


# Driver function to run the program
def main() :
	# encrypt the given message
	message = 'GEEKS FOR GEEKS'
	print(atbash(message.upper( )))
	
	# decrypt the given message
	message = 'TVVPH ULI TVVPH'
	print(atbash(message.upper( )))


# Executes the main function
if __name__ == '__main__' :
	main( )
