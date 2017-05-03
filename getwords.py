"""function getwords(text) to take a string, parse it and return words"""
def getwords(text):
	tokens = text.split()
	return tokens
	
if __name__ == "__main__":
	raw_text = raw_input('please enter text: ')
	print getwords(raw_text)
