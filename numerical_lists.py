#Ryan Walters Dec3 2020 -- Working through the Python lessons on numerical lists

#Initial test of the range function
print("Initial test of range function:")
for value in range(1, 5):
	print(value)

#Printing 1 through 5
print("\nPrinting 1 through 5 by changing the second value to 6:")
for value in range(1, 6):
	print(value)

#Printing a range by only passing one argument
print("\nPrinting a range by only passing one argument:")
for value in range(4):
	print(value)

#Printing a range of numbers as a list
print("\nPrinting a range of numbers as a list:")
numbers = list(range(1, 6))
print(numbers)

#Using a third argument in the range() function
print("\nUsing a third argument in the range() function to skip numbers with:")
numbers = list(range(2, 11, 2))
print(numbers)
print("\nAnother example:")
numbers = list(range(4, 30, 5))
print(numbers)

#Using the range() function to print squares into an empty list
print("\nUsing the range() function to print squares into an empty list:")
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

#Producing the same effect but without the second variable
print("\nProducing the same effect without using the second variable:")
squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)

#Using min(), max(), and sum() functions with a list of numbers
print("\nUsing min(), max(), and sum() functions with a list of numbers:")
numbers_list = []
for numbers in range(0, 41, 4):
	numbers_list.append(numbers)
print(numbers_list)
print(f"The smallest number in the list is {min(numbers_list)}.")
print(f"The largest number in the list is {max(numbers_list)}.")
print(f"The sum of all the numbers in the list is {sum(numbers_list)}.")

#Producing the same result from the range function in the earlier square function but with a list comprehension
print("\nProducing the same result from the earlier range function with squares, but using a list comprehension:")
sqaures = [value**2 for value in range(1, 11)]
print(squares)

#Using a list comprehension to affect a range of numbers with a simple equation
print("\nUsing a list comprehension to affect a range of numbers with a simple equation:")
numbers = [value+3-1 for value in range(1, 5)]
print(numbers)

#Try it yourself 4-3 counting to twenty
print("\nUsing a for loop and a list function to print a list that counts to twenty in two different ways:")
twenty_list = []
for twenty in range(1, 21):
	twenty_list.append(twenty)
print(twenty_list)
twenty_list = list(range(1, 21))
print(twenty_list)

#Try it yourself 4-6 odd numbers (4-4 and 4-5 will be in the million.py project)
print("\nUsing the third argument of the range() function to list only odd numbers 1 throught 20 with a for loop and a list function:")
twenty_odd_list = []
for twenty_odd in range(1, 21, 2):
	twenty_odd_list.append(twenty_odd)
print(twenty_odd_list)
twenty_odd_list = list(range(1, 21, 2))
print(twenty_odd_list)

#Try it yourself 4-7 a list of the multiples from 3 to thirty
print("\nUsing a for loop and a list function to count the multiples of 3 from 3 to 30:")
threes_list = []
for three in range(3, 31, 3):
	threes_list.append(three)
print(threes_list)
threes_list = list(range(3, 31, 3))
print(threes_list)

#Try it yourself 4-8 and 4-9 printing a list of the first 10 cubes
print("\nUsing a for loop and list comprehension to print the first 10 cubes in two different ways:")
cubes_list = []
for cube in range(1, 11):
	cubes_list.append(cube**3)
print(cubes_list)
cubes_list = [cube**3 for cube in range(1, 11)]
print(cubes_list)

#END OF PROGRAM
