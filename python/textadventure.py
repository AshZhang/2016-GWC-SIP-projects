start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)
dead = False

while dead == False:
	user_input = input("Do you go left or right? left/right ")
	if user_input == "left":
		print("\nYou decide to go left. Suddenly, you are curious to know\nwhat happens if you touch the walls.") # finished the story by writing what happens
		while dead == False:
			user_input = input("Do you touch the walls? yes/no ")
			if user_input == "yes":
				print("\nYou touch the walls carefully with your index finger.\nAn electric current surges through your finger through your body, ripping through your heart.")
				dead = True
			elif user_input == "no":
				print("\nYou stay away from the walls and continue forward. Thirst sets in.")
				while dead == False:
					user_input = input("You notice the plants on the walls. Technically, the plants are not the wall, so they may be safe to touch.\nDo you try to get water from the plants? yes/no ")
					if user_input == "yes":
						print("\nYou carefully rip a piece of vine from the wall. Nothing happens to you.\nYou suck the juice from the vine, and your throat and mouth immediately swell.\nYou wonder why you even tried drinking random plant juice as you asphyxiate.")
						dead = True
					elif user_input == "no":
						print("\nYou leave the plants alone. You continue through the maze for a day and a night.\nAs you reach your limit, you come across a fountain and drink heartily.")
						dead = "alive"
					else:
						print("Please enter 'yes' or 'no'.")
			else:
				print("Please enter 'yes' or 'no'.")
	elif user_input == "right":
		print("\nYou choose to go right. You encounter a man who looks slightly...off.\nHe comes towards you, and not in a friendly way.") # finished the story writing what happens
		while dead == False:
			user_input = input("Do you choose to fight, run, or talk? ")
			if user_input == "fight":
				print("\nYou raise your fists. When the man sees you put your fists up,\nan animalistic instinct appears to trigger. Before you\ncan make a move, he strikes.")
				dead = True
			elif user_input == "run":
				print("\nYou turn around and sprint away from the man. You weave through\nthe maze, losing the man...and your bearings. You wander for a day and a night.\nThirst sets in.")
				while dead == False:
					user_input = input("You notice the plants on the walls. Technically, the plants are not the wall, so they may be safe to touch.\nDo you try to get water from the plants? yes/no ")
					if user_input == "yes":
						print("\nYou carefully rip a piece of vine from the wall. Nothing happens to you.\nYou suck the juice from the vine, and your throat and mouth immediately swell.\nYou wonder why you even tried drinking random plant juice as you asphyxiate.")
						dead = True
					elif user_input == "no":
						print("\nYou leave the plants alone. You continue through the maze for a day and a night.\nWhen you reach your limit, you collapse to the ground. You curse this maze.")
						while dead == False:
							user_input = input("Your thoughts begin to wander. You think about your previous life, the one before you woke up in the maze.\nYou grow tired. Do you continue thinking, or do you close your eyes? think/close ")
							if user_input == "think":
								print("\nYour thoughts flow like a river. You remember the times of your previous life, the times outside this maze, the times of freedom.\nAs you think, you no longer feel the cold ground underneath your back. The line between reality and your thoughts blurs, then vanishes.\nThough your body remains in the maze, you are now free.")
								dead = "escape"
							elif user_input == "close":
								print("\nYou close your eyes, welcoming the darkness that will carry you from this dreaded maze. Your last thought is one of defiance against the maze.")
								dead = True
							else:
								print("Please enter 'think' or 'close'.")
					else:
						print("Please enter 'yes' or 'no'.")
			elif user_input == "talk":
				print("\nYou raise your hands up and avoid eye contact. You tell the man your name.\nHe pauses for a moment. You ask for his name, and he runs away.")
				while dead == False:
					user_input = input("Do you try to pursue him, or do you turn the other way? pursue/leave ")
					if user_input == "pursue":
						print("\nYou run after him, but he has disappeared. You find footprints, but they lead directly into a wall.\nUpon further inspection, there is actually a door in the wall.")
						while dead == False:
							user_input = input("Do you try to enter the door? yes/no ")
							if user_input == "yes":
								print("\nYou open the door and walk into a dark room. Suddenly, you fall down a pit you could not see in the dark.\nYou land with a crunch and lie immobilized upon the floor.")
								dead = True
							elif user_input == "no":
								print("\nYou move on from the door. You wander for a while, until thirst sets in.")
								while dead == False:
									user_input = input("You notice the plants on the walls. Technically, the plants are not the wall, so they may be safe to touch.\nDo you try to get water from the plants? yes/no")
									if user_input == "yes":
										print("\nYou carefully rip a piece of vine from the wall. Nothing happens to you.\nYou suck the juice from the vine, and your throat and mouth immediately swell.\nYou wonder why you even tried drinking random plant juice as you asphyxiate.")
										dead = True
									elif user_input == "no":
										print("\nYou leave the plants alone. You continue through the maze for a day and a night.\nAs you reach your limit, you come across a fountain and drink heartily.")
										dead = "alive"
									else:
										print("Please enter 'yes' or 'no'.")
							else:
								print("Please enter yes or no.")
					elif user_input == "leave":
						print("\nYou turn the other way and walk randomly through the maze. Soon thirst sets in.")
						while dead == False:
							user_input = input("You notice the plants on the walls. Technically, the plants are not the wall, so they may be safe to touch.\nDo you try to get water from the plants? yes/no")
							if user_input == "yes":
								print("\nYou carefully rip a piece of vine from the wall. Nothing happens to you.\nYou suck the juice from the vine, and your throat and mouth immediately swell.\nYou wonder why you even tried drinking random plant juice as you asphyxiate.")
								dead = True
							elif user_input == "no":
								print("\nYou leave the plants alone. You continue through the maze for a day and a night.\nAs you reach your limit, you come across a fountain and drink heartily.")
								dead = "alive"
							else:
								print("Please enter 'yes' or 'no'.")
					else:
						print("Please enter 'pursue' or 'leave'.")
			else:
				print("\nYou are unable to make a valid decision in time. While you stand frozen, the man\ncharges at you. You feel a sharp pain in your gut; as you clutch your stomach,\nyour hand becomes slick.")
				dead = True
	else:
		print("Please enter 'left' or 'right'.")
if dead == True:
	print("\nYou find yourself on the ground. Your vision spirals into the dark void of death.")
elif dead == "alive":
	print("\nYou continue, your thirst quenched. Eventually, you reach the end of the maze and continue to freedom.")
else:
	print("You awaken. The memories of your previous life evaporate as you begin your new life...as a water flea.")
print("The end")