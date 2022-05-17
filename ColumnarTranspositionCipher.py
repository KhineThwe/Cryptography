#Transposition Cipher is a cryptographic algorithm where the order of alphabets in the plaintext is rearranged to form a cipher text.
# In this process, the actual plain text alphabets are not included.
# A simple example for a transposition cipher is columnar transposition cipher where each character in the plain text is written horizontally with specified alphabet width. The cipher is written vertically, which creates an entirely different cipher text.
# Consider the plain text hello world, and let us apply the simple columnar transposition technique as shown below
# The plain text characters are placed horizontally and the cipher text is created with vertical format as : holewdlo lr. Now, the receiver has to use the same table to decrypt the cipher text to plain text.
import math

"""
In cryptography, the TRANSPOSITION cipher is a method of encryption where the
positions of plaintext are shifted a certain number(determined by the key) that
follows a regular system that results in the permuted text, known as the encrypted
text. The type of transposition cipher demonstrated under is the ROUTE cipher.
"""


def encryptMessage(key , message) :
	cipherText = [""] * key
	for col in range(key) :
		pointer = col
		while pointer < len(message) :
			cipherText [col] += message [pointer]
			pointer += key
	return "".join(cipherText)


def decryptMessage(key , message) :
	numCols = math.ceil(len(message) / key)
	numRows = key
	numShadedBoxes = (numCols * numRows) - len(message)
	plainText = [""] * numCols
	col = 0
	row = 0
	
	for symbol in message :
		plainText [col] += symbol
		col += 1
		
		if (
				(col == numCols)
				or (col == numCols - 1)
				and (row >= numRows - numShadedBoxes)
		) :
			col = 0
			row += 1
	
	return "".join(plainText)


# def main() :
# 	message = input("Enter message: ")
# 	key = int(input("Enter key [2-%s]: " % (len(message) - 1)))
# 	mode = input("Encryption/Decryption [e/d]: ")
#
# 	if mode.lower( ).startswith("e") :
# 		text = encryptMessage(key , message)
# 	elif mode.lower( ).startswith("d") :
# 		text = decryptMessage(key , message)
#
# 	# Append pipe symbol (vertical bar) to identify spaces at the end.
# 	print("Output:\n%s" % (text + "|"))


if __name__ == "__main__" :
	# import doctest
	#
	# doctest.testmod( )
	# main( )
	while True:
		message = input("Enter message: ")
		key = int(input("Enter key [2-%s]: " % (len(message) - 1)))
		mode = input("Encryption/Decryption [e/d]: ")
		
		if mode.lower( ).startswith("e") :
			text = encryptMessage(key , message)
		elif mode.lower( ).startswith("d") :
			text = decryptMessage(key , message)
		
		# Append pipe symbol (vertical bar) to identify spaces at the end.
		print("Output:\n%s" % (text + "|"))
