import queue
import requests
import threading
import sys

AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
EXTENSIONS = ['.php', '.bak', '.orig', '.inc']
TARGET = "http://testphp.vulnweb.com"
THREADS = 29
WORDLIST = "SVNDigger-all.txt"

def get_words(resume=None):

	def extend_words(word):
		if "." in word:
			words.put(f'/{word}')
		else:
			words.put(f'/{word}/')

		for extension in EXTENSIONS:
			words.put(f'/{word}{extension}')

	with open(WORDLIST) as f:
		raw_words = f.read()

	found_resume = False
	words = queue.Queue()
	for word in raw_words.split():
		if resume is not None:
			if found_resume:
				extend_words(word)
			elif word == resume:
				found_resume = True
				print(f'Resuming wordlist from: {resume}')
		else:
			print(word)
			extend_words(word)
	
	return words
