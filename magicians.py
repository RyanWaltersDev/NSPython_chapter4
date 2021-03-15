#Ryan Walters Dec3 2020 -- A program to demonstrate looping with lists

#Initial list and first for loop
magicians = ['copperfield', 'randi', 'blaine']
for magician in magicians:
    print(magician)

#Doing more with the loop
for magician in magicians:
    print(f"Wow, {magician.title()}! Your magic trick is astonishing!")
    print(f"I am certain that your next trick will be even better, "
        "{magician.title()}!\n")
print("This has been a great show so far! Thank you to everyone who came!")

#END OF PROGRAM
