animalNames = {
	"cat":"fred",
	"dog":"solo",
	"lizard":"zard",
	"bird":"polly",
	"fish":"oscar",
}

def addToDictionary():
	for i in animalNames:
		print i
	checkIF_newAnimals = raw_input("Do you have any new animals you would like to add to your dictionary? Please type 'YES' or 'NO' or 'EXIT'\n ").upper()
	if checkIF_newAnimals.startswith("Y"):
		newAnimals = raw_input("What type of animal would you like to add today? \n")
		newAnimals_Name = raw_input("What is the name of your new animal? \n")
		animalNames[newAnimals] = newAnimals_Name
	if checkIF_newAnimals.startswith("N"):
		print("OKAY")
	if 'Exit' in checkIF_newAnimals:
		exit()
addToDictionary()

#checks if you want to edit your dictionary
def check_forChanges():
	checkIf = raw_input("Would you like to change any of you're animals names today? Please type 'YES' or 'NO' or 'EXIT' or type 'ADD' if you would like to add another animal to your dictionary. \n ").upper()
	print("\n")
	if checkIf.startswith("Y"):
		for i in animalNames.keys():
			print i
		print("\n")	
		animalChoice = raw_input("what animal would you like to change the name of? \n")
		if animalChoice in animalNames.keys():
			newName = raw_input("What is the new name? \n")
			animalNames[animalChoice] = newName
			print("You've changed your " + animalChoice + "'s name to " + newName + ".")
		print('\n')
		#prints new names
		#for i in animalNames.values():
		#	print i	
		print("\n")		

	if checkIf.startswith("N"):
		print ("OKAY then, enjoy the rest of your day. =) ")
		exit()
	if 'EXIT' in checkIf:
		exit()	
	if 'ADD' in checkIf:
		addToDictionary()
	if 'print' in checkIf:
		for i in animalNames.values():
			print i
	else:
		check_forChanges()
		

check_forChanges()


 



