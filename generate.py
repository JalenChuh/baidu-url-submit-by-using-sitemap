import re
import urllib
import requests


html = urllib.request.urlopen(sitemap).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<url>).*?(?=</url>)'), html)

with open('urls.txt', 'w') as file:
  for data in result:
    print(data, file=file)
file.close()
