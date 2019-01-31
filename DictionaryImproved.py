# current dictionary 
itemNames = {}
validIntro = False

# checks if you want to add to your dictionary
def addToDictionary():		
	checkIF_newItems = raw_input("Add new item? 'YES' or 'NO' \n ").upper()
	if checkIF_newItems.startswith("Y"):
		newItems = raw_input("What type of item would you like to add today? \n")
		newItems_Name = raw_input("What is the value of your new item? \n")
		itemNames[newItems] = newItems_Name
		f = open('itemNames.txt', 'a+')
		f.write(str(itemNames))
		f.close()
		return True
	elif 'PRINT' in checkIF_newItems:
		print "------------------------------------------------------------------------------\n"
		log = open('itemNames.txt', 'r')
		for line in log:
			print str(log.read())
		print "These are your current items. \n\n"
		return True
	elif checkIF_newItems.startswith("N"):
		print("OKAY")
	elif 'Exit' in checkIF_newItems:
		exit()	

# checks if you want to edit your current dictionary
def check_forChanges():
	checkIf = raw_input("Change item value? 'YES' 'NO' 'EXIT' 'ADD' 'PRINT' \n").upper()
	print("\n")
	if checkIf.startswith("Y"):
		for i in itemNames.keys():
			print i
		print("\n")	
		itemChoice = raw_input("what item would you like to change the value of? \n")
		return True
		if itemChoice in itemNames.keys():
			newName = raw_input("What is the new value? \n")
			itemNames[itemChoice] = newName
			f = open('itemNames.txt', 'a+')
			f.write(str(itemNames))
			f.close()
			print("You've changed your " + itemChoice + "'s value to " + newName + ".")
			return True
		print('\n')
		return True		
	elif checkIf.startswith("N"):
		EXIT = raw_input("OKAY then, would you like to exit? ").upper()
		if EXIT.startswith('Y'):
			exit()
			return False
		elif EXIT.startswith('N'):
			check_forChanges()
		elif EXIT is 'print':
			for i in itemNames:
				print i	
				return True
	elif 'ADD' in checkIf:
		addToDictionary()
		return True
	elif 'PRINT' in checkIf:
		for i in itemNames.values():
			print i	
			return True
	elif 'EXIT' in checkIf:
		exit()
		return False

#def exitProgram():

addToDictionary()
check_forChanges()
	
"""
while not validIntro:
	check_forChanges(itemNames)
	if 'EXIT' in check_forChanges(itemNames):
		break
	elif check_forChanges(itemNames) == ".": 
		continue
	# closes or continues main loop	
while not validIntro:
	addToDictionary()
	if addToDictionary() or check_forChanges() == ".":
		continue
	if addToDictionary() or check_forChanges() == exit():
		break"""
