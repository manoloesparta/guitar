class Guitar:
	def __init__(self,chord,count,repeat):
		self.chord = chord
		self.count = count
		self.repeat = repeat

	@property
	def acorde(self):
		return self.chords
	@acorde.setter
	def acorde(self,value):
		pass

fa = Guitar('fa','3','n')
print(fa.chord)