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

#END OF PROGRAM
