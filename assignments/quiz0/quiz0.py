import requests

r = requests.get('http://www.cs.emory.edu/~choi')
with open('quiz0.html', 'w') as fout:
    fout.write(r.text)