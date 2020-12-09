#Ryan Walters Dec4 2020 -- Practicing slicing a list

#Initial list and slicing
players = ['mike', 'dave', 'zac', 'adam', 'april']
print(players[0:3])
print(players[2:5])
print(players[1:4])
print(players[:2])
print(players[3:])

#Using a slice in a loop
print("\nHere are the first three players on my team:")
for player in players[:3]:
	print(player.title())

print("\nHere are the last two players on my team:")
for player in players[-2:]:
	print(player.title())

#END OF PROGRAM
