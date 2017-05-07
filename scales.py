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

if __name__ == '__main__':
	#iter items to get chords
	for x,y in scales.items():
		print(x + '  :  ',end="")
		#iter items to get family chords
		for i in y:
			print(i,end=" ")
		print('\n')