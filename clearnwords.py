"""Cleanwords removes punctuation, removes words which are just numbers, convert all words to lower case and return them"""
def cleanwords(text):
	punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
	for punc_char in punctuations:
		text = text.replace(punc_char,  "")
	text = text.lower()
	tokens = text.split()
	digits = ('0','1','2','3','4','5','6','7','8','9')	
	for token in tokens:
		for char in token:
			if char not in digits:
				break
		else:
			tokens.remove(token)		
	return tokens
	
if __name__ == "__main__":	
	raw_text = raw_input('please enter text: ')
	print cleanwords(raw_text)	
