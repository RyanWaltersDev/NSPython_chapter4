#Ryan Walters Dec 24 2020 -- Learning about tuples

#Defining the tuple and calling it elements to a print function
dimensions = (300, 150)
print(f"The height of the box is {dimensions[0]} inches.")
print(f"THe width of the box is {dimensions[1]} inches.")

#Using a for loop with a tuple to print the values
for dimension in dimensions:
    print(dimension)

#Assigning a new value to a tuple's variable
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)


dimensions = (400, 200)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#END OF PROGRAM
