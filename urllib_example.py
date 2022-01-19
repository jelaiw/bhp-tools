import urllib.request

url = "http://example.com"
# See https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen.
with urllib.request.urlopen(url) as response:
	content = response.read()

print(content)
