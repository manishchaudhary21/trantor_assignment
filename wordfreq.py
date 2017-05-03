"""open a text file, read the text, process it using clearnwords. Count the number of occurences of each unique word"""
from clearnwords import cleanwords
def wordfrequency(filepath):	
	noisewords = []
	with open('./noisewords', 'r') as n:
		for line in n:
			noisewords += line.split(',')		
	counts = {}
	with open(filepath, 'r') as f:
		for line in f:
			for word in cleanwords(line):
				if word not in noisewords:				
					if word in counts:
						counts[word][0] += 1
						counts[word][1] += line+'<br>'
					else:
						counts[word] = [1, line+'<br>']
		return counts
