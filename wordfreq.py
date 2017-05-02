"""open a text file, read the text, process it using clearnwords. Count the number of occurences of each unique word"""
from clearnwords import cleanwords
counts = {}
with open('./assignment', 'r') as f:
	for line in f:
		for word in cleanwords(line):
			if word in counts:
				counts[word] += 1
			else:
				counts[word] = 1
	print counts
