from scales import *
import random

def main():
	while True:
		#What dou yo want to do
		enter = input('1. Scales\n2. Exit\nWhat option: ')
		enter = int(enter)
		#run scales.py
		if enter == 1:
			#Shows the avaible chords
			for x,y in scales.items():
				print(x, end=' ')
			#choose a chord
			chord = input('\nChoose a chord: ')
			#how many chords
			count = input('How many chords: ')
			count = int(count)
			#run the function
			print(getscales(chord,count)+'\n')
		#exit program
		elif enter == 2:
			print('Bye.')
			break

if __name__ == '__main__':
	main()