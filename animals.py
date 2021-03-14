#Ryan Walters Dec3 2020 -- Practicing for statement loops using a list of animals that share a similar characteristic

#Initial list and for statement loop with initial print
animal_list = ['bear', 'lion', 'shark', 'panther', 'anaconda']
for animal in animal_list:
	print(animal.title())
	
#New loop with a message
for animal in animal_list:
	print(f"If you ever come across a {animal.title()} in the wild, "
        "be alert! They might try to eat you.")
print("All of these animals are at the top of their respective food chain, "
    "and while fascinating, are very dangerous!")

#END OF PROGRAM
