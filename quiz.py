meal1= "spam"+ "eggs" +"beans"
meal2= "spam\neggs\nbeans"
meal3= "spam,eggs,beans"
meal4= """spam eggs beans"""
print(meal1)
print(meal2)
print(meal3)
print(meal4)
print("Terry\tJohn\tGraham\tmichael\tEric\tTerry")
first_name= "John"
last_name= "cleese"
age="78"
print(first_name +" "+last_name+" "+ age)
#what result will this program print
a=45
b=15
c=3

print(a-b/c)
#"""A banker earns a sum of 5000 monthly pays tax of 5% of his total salary at the end of the month
# write a program to determine the display how much he will be left with at the end of the month 
#after tax
#Note: please declare all your variables clearly
Total_salary= 5000
tax_rate= 0.05
Actual_tax= Total_salary*tax_rate
salary_left= Total_salary-Actual_tax
print(salary_left)





#slicing and Formartting

parrot = "Norwegian Blue"

#print(parrot[0:3])
#print(parrot[0:6])
#print(parrot[0:9:2])

#print(parrot[6:30])

#print(parrot[:]) [ no start:no end]
#print(parrot[0:6:2]) [start:end: step]
#print(parrot[0::6]) [start:no end:step]
#print(parrot[:6]) [ nostart:end]
#print(parrot[:6:2]) [no start:end: step]
#print(parrot[::2]) [nostart:noend: step]



#string formatting and replacement fields


first_name ="isaiah"
last_name = "iyede"
age = 30
type_of_food = "amala"
#print("my name is {0} {1} and i am {2} years old and i like {3}".format(first_name, last_name, age, type_of_food) )



#mystring ="abcdef"
#print(mystring[-1:-7:-1])

#print(parrot[-1:-15:-1])

#len(parrot)
#print(parrot[-1:-len(parrot)-1:-1])



#conditional flow of programs of python
#congratulatory_message = "Hurray you were successful"
#rejection_message = "Sorry try next year"

# age = rawInput("How old are you: ")
# if age >= 18:
# 	print(congratualtory_message)
# else:
# 	print(rejection_message)

a= 12
b= 5
if a % b > 3:
	print(True)
elif a % b == 2:
	print("This is the correct answer")
else:
	print(False)

# age = input("How old are you: ")
# if age >= 18:
# 	print('congratulatory_message')
# else:
# 	print('rejection_message')

  

