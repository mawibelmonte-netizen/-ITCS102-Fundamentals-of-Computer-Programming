#multiple if and elif condition

#Create a python program that would capture age group 

name = input("Please input your name ---> ")

age = int(input("Please input your age ---> "))

if age >= 0 and age <= 1:
	print("That age is considered as an INFANT")

elif age >= 1 and age <= 3:
	print("That age is considered as an TODDLER")

elif age >= 3 and age <= 5:
	print("That age is considered as an PRE-SCHOOLER")

elif age >= 6 and age <= 9:
	print("That age is considered as an CHILD")

elif age >= 10 and age <= 12:
	print("That age is considered as an PRE-TEEN")

elif age >= 13 and age <= 17:
	print("That age is considered as an TEENAGER")

elif age >= 18 and age <= 25:
	print("That age is considered as an YOUNG ADULT")

elif age >= 26 and age <= 39:
	print("That age is considered as an ADULT")

elif age >= 40 and age <= 59:
	print("That age is considered as an MIDDLE AGED ADULT")

elif age >= 60 and age <= 64:
	print("That age is considered as an MATURE ADULT")

elif age >= 65 and age <= 74:
	print("That age is considered as an SENIOR ADULT")

elif age >= 75 and age <= 84:
	print("That age is considered as an ELDERLY")

elif age >= 85 and age <= 99:
	print("That age is considered as an CENTENARIAN")

elif age >= 100 and age <= 150:
	print("That age is considered as an SUPERCENTENARIAN")

else:
	print("You are 25 feet underground")







