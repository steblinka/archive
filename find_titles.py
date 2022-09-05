import bs4
for dt in range (21):
    exampleFile = open(r'E:\py_files\Belapan\spelling\dt_ua\2021\dt_text_%s.txt' % (dt +1), encoding='utf-8')
    exampleFile1 = exampleFile.read()
    with open('dt_news_itemm_%s.txt' % (dt + 1), 'a', encoding='utf-8') as file: 
        exampleSoup = bs4.BeautifulSoup(exampleFile1, features="lxml")
        title = exampleSoup.find_all('title')
        for title in exampleSoup.find_all('title'):
           print('\n', title.text, '\n', file=file)
        text = exampleSoup.find_all('div', {'class': 'text'})
        for text in exampleSoup.find_all('div', {'class': 'text'}):
            print('\n', text.text, '\n', file=file)
        print('%s' % (dt + 1))
        
                
        
        
    
      
