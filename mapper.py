import queue
import os
import contextlib
import time
import requests
import sys
import threading
import random

FILTERED = [".jpg", ".gif", ".png", ".css"]
# Try Wordpress in a Docker container for a mapper target.
# See Docker Hub at https://hub.docker.com/_/wordpress.
TARGET = "http://localhost:8080"
THREADS = 8

web_paths = queue.Queue()
answers = queue.Queue()

def test_remote():
	while not web_paths.empty():
		path = web_paths.get()
		url = f'{TARGET}{path}'
		# See https://docs.python.org/3/library/time.html#time.sleep.
		# See https://docs.python.org/3/library/random.html#real-valued-distributions.
		time.sleep(random.uniform(0.99, 2.99)) # Try to avoid target throttling/lockout protection.
		r = requests.get(url)
		if r.status_code == 200:
			answers.put(url)
			sys.stdout.write('+')
		else:
			sys.stdout.write('x')
		sys.stdout.flush()

def run():
	threads = list()
	for i in range(THREADS):
		print(f'Spawning thread {i}.')
		t = threading.Thread(target=test_remote)
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

def gather_paths():
	for root, _, files in os.walk('.'):
		for fname in files:
			if os.path.splitext(fname)[1] in FILTERED:
				continue
			path = os.path.join(root, fname)
			if path.startswith('.'):
				path = path[1:]
			print(path)
			web_paths.put(path)

@contextlib.contextmanager
def chdir(path):
	"""
	On enter, change directory to specified path.
	On exit, change directory back to original.
	"""
	this_dir = os.getcwd()
	os.chdir(path)
	try:
		yield
	finally:
		os.chdir(this_dir)

if __name__ == '__main__':
	with chdir("/home/kali/tmp/wordpress"):
		gather_paths()
	input("Press return to continue.")

	run()
	with open('answers.txt', 'w') as f:
		while not answers.empty():
			f.write(f'{answers.get()}\n')
	print('Done.')
