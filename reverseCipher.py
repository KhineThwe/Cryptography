#Reverse Cipher uses a pattern of reversing the string of plain text to convert as cipher text.
#The process of encryption and decryption is same.
#To decrypt cipher text, the user simply needs to reverse the cipher text to get the plain text.
#The major drawback of reverse cipher is that it is very weak. A hacker can easily break the cipher text to get the original message. Hence, reverse cipher is not considered as good option to maintain secure communication channel,.

message = 'This is program to explain reverse cipher.'
translated = '' #cipher text is stored in this variable
i = len(message) - 1

while i >= 0:
   translated = translated + message[i]
   i = i - 1
print("The cipher text is : ", translated)
