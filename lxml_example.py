from io import BytesIO
from lxml import etree

import requests
r = requests.get("http://scanme.nmap.org")

# Read API docs at https://lxml.de/apidoc/lxml.etree.html#lxml.etree.HTMLParser.
parser = etree.HTMLParser()
# Note r.content is of type 'bytes'.
# See https://lxml.de/apidoc/lxml.etree.html#lxml.etree.parse.
root_element = etree.parse(BytesIO(r.content), parser=parser) 

# Find all "a" anchor elements.
# See https://lxml.de/apidoc/lxml.etree.html#lxml.etree._Element.
for link in root_element.findall('//a'): 
	print(f"{link.get('href')} -> {link.text}")
