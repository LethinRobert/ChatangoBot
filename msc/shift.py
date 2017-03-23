import string
numbers = ""
x = 0
while x < 11:
	numbers = numbers + str(x)
	x += 1
shift = int(input("Pick shift key from 1-9"))
choice = input("would you like to encode or decode?")
letters = string.ascii_letters + string.punctuation + numbers
word = (input("Please enter text"))
print (letters)
encoded = ''
if choice == "encode":
	for letter in word:
		if letter == ' ':
			encoded = encoded + ' '
		else:
			x = letters.index(letter) + shift
			encoded = encoded + letters[x]
if choice == "decode":
	for letter in word:
		if letter == ' ':
			encoded = encoded + ' '
		else:
			x = letters.index(letter) - shift
			encoded = encoded + letters[x]
print (encoded)


