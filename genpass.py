#encoding: UTF-8
import random
import sys

try:
	leng = int(sys.argv[1])
except:
	leng = 25

chars = ['a','b','c','ç','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
chars_up = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
numbers = [1,2,3,4,5,6,7,8,9,0]
especial_chars = ['\'','"','(',')','{','}','[',']','=','@','#','´','`','~','/','\\']

password = ""

for i in range(leng):
	v = random.randint(1, 4)

	if v == 1:
		password += str(random.choice(chars))
	elif v == 2:
                password += str(random.choice(chars_up))
	elif v == 3:
                password += str(random.choice(numbers))
	elif v == 4:
                password += str(random.choice(especial_chars))

print password
