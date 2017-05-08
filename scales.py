import random
#Declaring my scales and possible chords
scales = {
	'C':['C','Dm','Em','F','G','Am','B0'],
	'Db':['Db','Ebm','Fm','Gb','Ab','Bbm','C0'],
	'D':['D','Em','F#m','G','A','Bm','C#0'],
	'Eb':['Eb','Fm','Gm','Ab','Bb','Cm','D0'],
	'E':['E','F#m','G#m','A','B','C#m','D#0'],
	'F':['F','Gm','Am','Bb','C','Dm','E0'],
	'F#':['F#','G#m','A#m','B','C#','D#m','E#0'],
	'Gb':['Gb','Abm','Bbm','Cb','Db','Em','F#0'],
	'G':['G','Am','Bm','C','D','Em','G0'],
	'Ab':['Ab','Bbm','Cm','Db','Eb','Fm','G0'],
	'A':['A','Bm','C#m','D','E','F#m','G#0'],
	'Bb':['Bb','Cm','Dm','Eb','F','Gm','A0'],
	'B':['B','C#m','D#m','E','F#','G#m','A#0'],
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

if __name__ == '__main__':
	#show the dictiorie scales
	#iter items to get chords
	for x,y in scales.items():
		print(x + '  :  ',end="")
		#iter items to get family chords
		for i in y:
			print(i,end=" ")
		print('\n')
	#run the actual program
	#Shows the avaible chords
	for x,y in scales.items():
		print(x, end=' ')
	#Choose a chord
	chord = input('\nChoose a chord: ')
	#how many chords
	count = input('How many chords: ')
	count = int(count)
	#run the function
	print(getscales(chord,count))