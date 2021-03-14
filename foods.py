#Ryan Walters Dec 9 2020 -- Copying a list of favorite foods using [:]
#Ryan Walters March 14 2021 -- 4-15 complying with PEP 8

#Initial list and printing
foods = ['tacos', 'sushi', 'burgers', 'pizza', 'wings']
print("A few of my favorite foods are:")
print(foods)

#Copying list
friends_foods = foods[:]
print("\nMy friend agrees. Their favorite foods are also:")
print(friends_foods)

#Appending these lists separately
print("\nThere's some foods only one of us likes. "
    "I will add them to their respective lists.")
foods.append('hummus')
friends_foods.append('carrots')
print("\nThe updated list of my favorite foods is:")
print(foods)
print("\nThe updated list of my friend's favorite foods is:")
print(friends_foods)

#Try it yourself 4-10
#Slice first 3 items
print("\nThe first three items in my list are:")
print(foods[:3])
print("\nThe first three items in my friend's list are:")
print(friends_foods[:3])

#Slice middle items
print("\nThe middle items of my list are:")
print(foods[1:-1])
print("\nThe middle items of my friend's list are:")
print(friends_foods[1:-1])

#Slice last three items
print("\nThe last three items of my list are:")
print(foods[-3:])
print("\nThe last three items of my friend's list are:")
print(friends_foods[-3:])

#Try it yourself 4-12 using for loops
print("\nThe complete list of my favorite foods is:")
for food in foods:
    print(food.title())
print("\nThe complete list of my friend's favorite foods is:")
for food in friends_foods:
    print(food.title())

#END OF PROGRAM
