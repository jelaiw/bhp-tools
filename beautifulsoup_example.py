from bs4 import BeautifulSoup as bs

import requests
r = requests.get("http://scanme.nmap.org")

# Note, this uses the Python HTML parser.
# See https://beautiful-soup-4.readthedocs.io/en/latest/#installing-a-parser.
# Also, see https://beautiful-soup-4.readthedocs.io/en/latest/#beautifulsoup for data structure.
tree = bs(r.text, 'html.parser')
# See https://beautiful-soup-4.readthedocs.io/en/latest/#find-all.
for link in tree.find_all('a'):
	print(f"{link.get('href')} -> {link.text}")
