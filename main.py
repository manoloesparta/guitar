from scales import *
import random

def main():
	#Shows the avaible chords
	for x,y in scales.items():
		print(x, end=' ')
	#You choose a chord
	chord = input('\nChoose a chord: ')
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
	#How much chords are we talking about?
	count = input('How many chords?')
	count = int(count)
	#Creating the new chord progression
	progression = ''
	for i in range(int(count)):
		progression += random.choice(prob_chords) + ' '
	print(progression)

if __name__ == '__main__':
	main()