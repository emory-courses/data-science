import requests

r = requests.get('http://www.cs.emory.edu/~choi')
print(r.text)