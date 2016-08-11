import random

food_adj = ["Crispy",
            "Savory",
			"Soft",
			"Fancy",
			"Creamy",
			"Fine",
			"Special",
			"Traditional",
			"Famous",
			"Dubious",
			"Lowfat",
			"Juicy",
			"Light",
			"Spicy",
			"Low-sodium",
			"Low-calorie",
			"Gluten-Free",
			"Sugar-Free",
			"Hypoallergenic",
			"Flaky",
			"Aged",
			"Breaded",
			"Bland",
			"Flavorful",
			"Overcooked",
			"Undercooked",
			"Chewy",
			"Thick",
			"Thin",
			"Unsweetened",
			"Organic",
			"Rich",
			"Rare"]

food_style = ["Fried",
              "Boiled",
			  "Stir-Fried",
			  "Raw",
			  "Roasted",
			  "Grilled",
			  "Microwaved",
			  "Steamed",
			  "Baked",
			  "Sauteed",
			  "Smoked",
			  "Burned",
			  "Blanched",
			  "Slow-Cooked",
			  "Cured",
			  "Marinated",
			  "Frozen",
			  "Chilled",
			  "Fermented",
			  "Ground",
			  "Chopped",
			  "Seared",
			  "Dried",
			  "Braised",
			  "Pickled",
			  "Irradiated",
			  "Torched",
			  "Freeze-Dried",
			  "Pureed",
			  "Combusted",
			  "Stewed",
			  "Partially Digested",
			  "Processed"]

food_name = ["Chicken",
             "Porkchops",
			 "Steak",
			 "Salmon",
			 "Greens",
			 "Peppers",
			 "Mushrooms",
			 "Potatoes",
			 "Noodles",
			 '"Food"',
			 "Sandwich",
			 "Pasta",
			 "Lambchops",
			 "Soup",
			 "Liver",
			 "Scraps",
			 "Salad",
			 "Wild Grains",
			 "Biscuits",
			 "Shellfish",
			 "Meatballs",
			 "Casserole",
			 "Seasonal Fruit",
			 "Bones",
			 "Gruel",
			 "Frog Legs",
			 "Soylent Green",
			 "Crab",
			 "Corn",
			 "Beans",
			 "Squash",
			 "Starch",
			 "Rations"]

adj_descr = ["to a crisp",
             "with mixed spices",
			 "until soft",
			 "with high-quality ingredients",
			 "with decadent cream sauce",
			 "with patience and care",
			 "with secret spices",
			 "like Grandma used to make",
			 "with our most popular spices",
			 "until barely recognizable",
			 "with fewer lipids",
			 "to a perfect degree of juiciness",
			 "with a delicate airiness",
			 "with a fiery kick",
			 "with fewer ionic compounds",
			 "with a decreased capability to heat water when burned",
			 "with no wheat proteins",
			 "with no monosaccharides",
			 "with no histamine triggers",
			 "with a crumbly texture",
			 "and aged since 200 BCE",
			 "and coated in crunchy bread crumbs",
			 "with no discernable taste",
			 "with flavorful seasoning",
			 "for way too long",
			 "for not long enough",
			 "with a texture like gum",
			 "and piled thick",
			 "and cut thinly",
			 "with no sweeteners",
			 "with no pesticides",
			 "with a lavishly thick texture",
			 "and cooked so rare that it is thought to be extinct in the wild"]

style_descr = ["fried",
               "boiled",
			   "stir-fried",
			   "left uncooked",
			   "roasted",
			   "grilled",
			   "microwaved",
			   "steamed",
			   "baked",
			   "sauteed",
			   "smoked",
			   "charred",
			   "lightly cooked",
			   "slowly cooked",
			   "cured",
			   "cooked in savory soaking juices",
			   "frozen",
			   "chilled",
			   "fermented",
			   "minced",
			   "sliced and diced",
			   "seared",
			   "dessicated",
			   "braised",
			   "pickled",
			   "heated with thermonuclear energy",
			   "fired with a torch",
			   "freeze-dried",
			   "liquified",
			   "chemically reacted with oxygen",
			   "cooked into a slurry",
			   "partially digested",
			   "industrially processed"]

recipes = []

print("\nMenu\n")
safe = "Maybe"

for i in range (10):
	adj_index = random.randint(0, len(food_adj)-1)
	style_index = random.randint(0, len(food_style)-1)
	food_index = random.randint(0, len(food_name)-1)

	recipe = food_adj[adj_index]+" "+food_style[style_index]+" "+food_name[food_index]
	
	while recipe in recipes:
		adj_index = random.randint(0, len(food_adj)-1)
		style_index = random.randint(0, len(food_style)-1)
		food_index = random.randint(0, len(food_name)-1)
		recipe = food_adj[adj_index]+" "+food_style[style_index]+" "+food_name[food_index]
	
	safe = random.randint(0,2)
	if safe == 0:
		safe = "Yes"
	elif safe == 1:
		safe = "No"
	else:
		safe = "Maybe"
	
	print(str(i+1)+": "+recipe)
	print("   "+food_name[food_index]+" "+style_descr[style_index]+" "+adj_descr[adj_index])
	print("   Meets USDA requirements for food safety: "+safe+"\n")
	recipes.append(recipe)
	

