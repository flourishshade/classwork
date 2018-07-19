# forloops, whileloops, augumented assignments, break, continue, switch

# 1. print the squares of mulitples of 3 between 0 and 30
# 2. print the first hundred numbers in reverse order
# 3. get a user to enter any calender year. If it is a leap year
# display text 'this is a leap year' else 'this is not a leap year'

# 4. print the multiplication tables of the odd numbers between 0 and 15


# cal_year = int(input('Enter a year: '))
# if cal_year % 4 == 0:
# 	print("{} is a leap year".format(cal_year))
# else:
# 	print("{} is not a leap year".format(cal_year))


# for i in range(30,0,-2):
# 	print(i)


# numbers = '9,222,543, 876, 9786,567'


# for char in numbers:
# 	if char == ',' or char == ' ':
# 		continue
# 	else:
# 		if int(char) % 2 == 1:
# 			print(char)
# 		else:
# 			continue

# for char in numbers:
# 	if char == ',' or char == ' ':
# 		continue
# 	else:
# 		if int(char) % 2 == 1:
# 			print(char)
# 		else:
# 			break


# for char in numbers:
# 	if char in '0123456789':
# 		print(char, end='')
# 	else:
# 		continue


# for i in range(0,31,3):
# 	print(i**2)

# augumented assignment
# even_number = 2
# # even_number = even_number + 1
# even_number += 1
# print(even_number)


# for char in range(10):
# 	char **= 2
# 	print(char)


# for char in range(10):
# 	chare = char ** 2
# 	print(chare)


# num = 3
# num += 1
# num -= 2
# num *= 2


# multiplication table
# for i in range(2,13):
# 	for j in range(1,13):
# 		print('{0} times {1} is {2}'.format(i,j,i*j), end='\t')
# 		print('')
# 	print('========'*10)

# step 1
# first loop will take 2
# second loop will take 1
# second loop will take 2 ...... 12

# second loop will take 3
# second loop will take 1
# second loop will take 2 ...... 12 


# for i in range(1,16,2):
# 	for j in range(1,13):
# 		print('{0} times {1} is {2}'.format(i,j,i*j), end='\t')
# 		print('')
# 	print('========'*10)


# for i in range(1,16):
# 	if int(i) % 2 == 1:
# 		for j in range(1,13):
# 			print('{0} times {1} is {2}'.format(i,j,i*j), end='')
# 			print('')
# 		print('========'*10)
# 	else:
# 		continue

# while loop 

# number = 0
# while number < 10:
# 	print('The number is {}'.format(number))
# 	number += 1


# for i in range(0,10):
# 	print('The number is {}'.format(i + 1))



















































