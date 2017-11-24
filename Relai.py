
# var = 1
# var3 = 2
# var4 = 3
# var5 = 'hellow world!'
# var6 = 'i am python!'
# Print(var3 + var4)

#CONDITIONAL STATEMENT

# john_age = 14
# alex_age = 15

# if john_age > 1 and john_age <=5:
# 	print("John age is"+str(john_age))
# 	if alex_age > 1 and alex_age <=5:
# 		print("Alex age is" + str(alex_age))
# elif john_age > 5 and john_age <= 10:
# 	print("John age range 5 - 10"+str(john_age))
# 	if alex_age > 5 and alex_age <= 10:
# 		print("Alex age is" +str(alex_age))
# elif john_age > 10 and john_age <= 15:
# 	print("John range 10 - 15"+str(john_age))
# 	if alex_age > 10 and alex_age <= 15:
# 		print("Alex age is" +str(alex_age))
# else:
# 	print("John and Alex aged 15 and above")


# LOOPS
# Function Range(0, 10) list[0, 10]
# array -list
# arr = []

# items = range(0,10)
# year3_students = ['alex', 'john', 'airel' , 'joy', 'lopez', 'karl']
# year4_students = ['kevin', 'mayang', 'jason' , 'biol', 'christian']
# emp = []
# it_year_lvl = [emp,year3_students,year4_students]

# for it in it_year_lvl:
# 	for st in it:
# 		print(st)





# for x in range(0,101):
# 	if x % 2 == 0:
# 		print("even "+str(x))
# 	else:
# 		print("odd  "+str(x))


#  import random
#  name = input("enter name :")
# print(name)
#  strr = ''
# rand = random.randint(1, 10)
# while rand > 0:
# 	strr += random.choice(string.ascii_lowercase)
# 	rand-=1
#  	print(strr)

# import random
# name = input("Enter name:")
# rand = random.randint(1,10)
# print ("your name is:")

# while rand > 0:
 

#  choice = input("Guess what im thingking:")
#  choice = int(choice)
#  print(rand)
#  if rand == choice:
#   print(name+"You are correct!")
#   break
#  else:
#   print(name+"You are wrong!")
# rand-=1

import random
name = input("enter name:")
rand = random.randint(1,15)
flag = true
while flag:
	num = int(input("Guess:")
	if num == rand:
		print("Congrats!!")
		flag = false
	else:
		print("Incorrect")



