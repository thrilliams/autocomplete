from json import loads as parse_json
import urllib.parse as urllib

file = open('history.txt', 'a+')

history = parse_json(open('history.json').read())
for term in history:
    if term['url'].startswith('https://www.google.com/search'):
        query = urllib.parse_qs(urllib.urlparse(term['url']).query)
        if 'q' in query:
            file.write(query['q'][0] + '\n')