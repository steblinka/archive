import requests
for i in range (9):
    res = requests.get('https://www.vinnitsa.info/calendar?d=2022-09-0%s' % (i+1))
    res.raise_for_status()
    speechFile = open('news_%s.txt' % (i+1), 'ab')
    print('page %s done' % (i+1))
    for chunk in res.iter_content(200000):
        speechFile.write(chunk)
        speechFile.close()
        
