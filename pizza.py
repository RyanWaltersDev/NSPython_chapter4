#Ryan Walters Dec3 2020 -- Practicing for statement loops with my favorite kinds of pizza. Also expanding for Try it yourself 4-10 and 4-11

#Initial list and for statement loop with initial print
favorite_pizzas = ['sausage', 'margherita', 'pepperonni', 'greek', 
    'buffalo chicken']
for pizza in favorite_pizzas:
	print(pizza.title())
	
#New loop with a message
for pizza in favorite_pizzas:
	print(f"One of my favorite kinds of pizza is {pizza.title()}!")
print("Boy, do I sure like pizza.")

#Using a slice to print the first 3 items
print("\nThe first three items in the list are:")
for pizza in favorite_pizzas[:3]:
	print(pizza.title())

#Using a slice to print the middle 3 items
print("\nThe three items in the middle of the list are:")
for pizza in favorite_pizzas[1:4]:
	print(pizza.title())

#Using a slice to print the last 3 items
print("\nThe last three items in the list are:")
for pizza in favorite_pizzas[-3:]:
	print(pizza.title())

#Making a copy of the list Try it yourself 4-11
friend_pizzas = favorite_pizzas[:]
friend_pizzas.append("barbecue")
friend_pizzas.remove("greek")
print("\nMy friend likes most of the same pizzas. Here is their list:")
for pizza in friend_pizzas:
	print(pizza.title())

#END OF PROGRAM
