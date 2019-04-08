import requests
import sys

url = 'https://dze0ko3lvd.execute-api.us-east-1.amazonaws.com/prod/sum?a={}&b={}'
a = int(sys.argv[1])
b = int(sys.argv[2])
r = requests.get(url.format(a, b))
print(r.text)