from queue import Queue
from lxml import etree
from io import BytesIO

WORDLIST = '/home/kali/repos/SecLists/Passwords/Software/cain-and-abel.txt'

def get_words():
	with open(WORDLIST) as f:
		raw_words = f.read()

	words = Queue()
	for word in raw_words.split():
		words.put(word)

	return words

def get_params(content):
	params = dict()
	parser = etree.HTMLParser()
	tree = etree.parse(BytesIO(content), parser=parser)
	for element in tree.findall('//input'):
		name = element.get('name')
		if name is not None:
			params[name] = element.get('value', None)
	
	return params
