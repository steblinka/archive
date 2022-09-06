import requests, time
with open (r'E:\py_files\pravda_21\pravda_links.txt') as file:
    urls = [row.strip() for row in file]    
    for i in range(len(urls)):
        print('%s' % (i+1))
        res = requests.get(urls[i])
        try:
            res.raise_for_status()
        except Exception as exc:
            print('сторінка не існує %s' % (exc))
        pravdaFile = open('pravda_text_%s.txt' % (i+1), 'ab')
        for chunk in res.iter_content(200000):
            pravdaFile.write(chunk)
            pravdaFile.close()
            time.sleep(5)
            

        
