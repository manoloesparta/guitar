import random
#Declaring my scales and possible chords
scales = {
	'C':['C','Dm','Em','F','G','Am'],
	'Db':['Db','Ebm','Fm','Gb','Ab','Bbm'],
	'D':['D','Em','F#m','G','A','Bm'],
	'Eb':['Eb','Fm','Gm','Ab','Bb','Cm'],
	'E':['E','F#m','G#m','A','B','C#m'],
	'F':['F','Gm','Am','Bb','C','Dm'],
	'F#':['F#','G#m','A#m','B','C#','D#m'],
	'Gb':['Gb','Abm','Bbm','Cb','Db','Em'],
	'G':['G','Am','Bm','C','D','Em'],
	'Ab':['Ab','Bbm','Cm','Db','Eb','Fm'],
	'A':['A','Bm','C#m','D','E','F#m'],
	'Bb':['Bb','Cm','Dm','Eb','F','Gm'],
	'B':['B','C#m','D#m','E','F#','G#m'],
}

def getscales(chord,count):
	#Capitalize chord
	chord = chord[0].upper() + chord[1:].lower()
	#This chord exist?
	try:
		scales[chord]
	#If not cancel all the program
	except KeyError:
		print('That chord isnt included')
		quit()
	#Assign the probably chosen chords
	prob_chords = scales[chord]
	#Creating the new chord progression
	progression = ''
	for i in range(int(count)):
		progression += random.choice(prob_chords) + ' '
	#return my progression
	return progression

def actual_runner():
	#run the actual program
	#Shows the avaible chords
	for x,y in scales.items():
		print(x, end=' ')
	#Choose a chord
	chord = input('\nChoose a chord: ')
	#Repeat chords?
	repeat = input('Want to chords repeat (y/n): ')
	if not (repeat != 'y' or repeat != 'n'):
		print('Dont have that option')
	#how many chords
	count = input('How many chords: ')
	try:
		count = int(count)
	except ValueError:
		print('That doesnt is a number')
		quit()
	#run the function
	return getscales(chord,count)

if __name__ == '__main__':
	#show the dictiorie scales
	#iter items to get chords
	for x,y in scales.items():
		print(x + '  :  ',end="")
		#iter items to get family chords
		for i in y:
			print(i,end=" ")
		print('\n')