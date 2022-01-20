import requests

# See https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request.
r = requests.post("https://httpbin.org/post", data={'key': 'value'})
print(r.text)

# See https://docs.python-requests.org/en/latest/user/quickstart/#passing-parameters-in-urls.
payload = {"key1": "value1", "key2": "value2"}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.url)

# See https://docs.python-requests.org/en/latest/user/quickstart/#custom-headers.
# Also, see urllib2 example on page 73.
headers = {"User-Agent": "Googlebot"}
r = requests.get("https://httpbin.org/get", headers=headers)
print(r.text)
