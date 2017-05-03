"""open a text file, read the text, process it using clearnwords. Count the number of occurences of each bigram word"""
from itertools import cycle
from clearnwords import cleanwords
def bigramwordfre(filepath):	
	noisewords = []
	with open('./noisewords', 'r') as n:
		for line in n:
			noisewords += line.split(',')		
	counts = {}
	with open(filepath, 'r') as f:
		for line in f:									
			words = [word for word in cleanwords(line) if word not in noisewords]
			max = len(words)
			for i in range(0,max):
				if i == max-1:
					bigramword = words[i]
				else:				
					bigramword = words[i] + ' ' + words[i+1]
				if bigramword in counts:
					counts[bigramword][0] += 1
					counts[bigramword][1] += line+'<br>'
				else:
					counts[bigramword] = [1, line+'<br>']																			
		return counts
