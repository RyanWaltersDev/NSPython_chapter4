# Ryan Walters Feb 27 2021 -- Try it yourself 4-13 -- Using tuples to list the items in a buffet

#Initial tuple
buffet_items = ('sushi', 'lo mein', 'stir fry', 'sashimi', 'miso soup')
print("Welcome to Wasabi Buffet! Here is a list of our most popular items:")
for buffet in buffet_items:
    print(buffet.title())

#Purposefully creating a TypeError to ensure we are working with a tuple

# buffet_items[0] = 'pizza'

#TypeError produced, leaving as comment

#Modifying the menu items in the tuple
buffet_items = ('sushi', 'orange chicken', 'stir fry', 'sashimi', 
    'egg drop soup')
print("\nWelcome to Wasabi Buffet! Some of our menu items have changed:")
for buffet in buffet_items:
    print(buffet.title())

#END OF PROGRAM
