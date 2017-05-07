from scales import *
import random

def main():
	#Shows the avaible chords
	for x,y in scales.items():
		print(x, end=' ')
	#You choose a chord
	chord = input('\nChoose a chord: ')
	#Capitalize chord
	chord = chord.capitalize()
	#This chord exist?
	try:
		scales[chord]
	#If not cancel all the program
	except KeyError:
		print('That chord isnt included')
		quit()
	#How much chords are we talking about?
	count = input('How many chords: ')
	count = int(count)
	#Creating the new chord progression
	progression = []
	progression += random.sample(scales[chord],count)
	#Print progression
	for i in progression:
		print(i, end=' ')
	print('\n')

if __name__ == '__main__':
	main()