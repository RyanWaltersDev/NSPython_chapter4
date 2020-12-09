#Ryan Walters Dec 9 2020 -- Copying a list of favorite foods using [:]

#Initial list and printing
foods = ['tacos', 'sushi', 'burgers', 'pizza', 'wings']
print("A few of my favorite foods are:")
print(foods)

#Copying list
friends_foods = foods[:]
print("\nMy friend agrees. Their favorite foods are also:")
print(friends_foods)

#Appending these lists separately
print("\nThere's some foods only one of us likes. I will add them to their respective lists.")
foods.append('hummus')
friends_foods.append('carrots')
print("\nThe updated list of my favorite foods is:")
print(foods)
print("\nThe updated list of my friend's favorite foods is:")
print(friends_foods)