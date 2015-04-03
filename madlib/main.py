#Rajmatie Arjune 
#Assignment: Madlib 
#April 2, 2015

print "Hello!! Welcome to my Madlib Game!"




def myGame():
	playerSelect = dict()
	addSelect('city', playerSelect)
	addSelect('food', playerSelect)
	addSelect('hero', playerSelect)
	game = gameFormat.format(**playerSelect)
	
	
def playerSelect(cue, dictionary):
	'''Prompt for player response using the cue string and place the cue response pair in the dictionary '''
	prompt = 'Enter a cue ' + cue + ': '
	response = input(prompt)
	dictionary [cue] = response
	myGame()
	print "Once upon a time " + myGame