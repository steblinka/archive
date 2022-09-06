import bs4, re
for sn in range (3):
    TGFile = open(r'C:\Users\Win 10 Pro\Downloads\Telegram Desktop\ChatExport_2022-07-31\messages%s.html' % (sn +1), encoding='utf-8')
    TGFile1 = TGFile.read()
    with open('links.txt', 'a', encoding='utf-8') as file: 
        exampleSoup = bs4.BeautifulSoup(TGFile1, features="lxml")
        links = exampleSoup.find_all('a')
        for links in exampleSoup.find_all('a'):
            print('\n', links, '\n', file=file)
linksFile = open(r'C:\Users\Win 10 Pro\Desktop\універ\digital instruments\links.txt', encoding='utf-8') 
linksFile1 = linksFile.read()
link = re.compile(r'\"(https\:\/\/.*?)/"') 
all_links = link.findall(linksFile1)
print('\n'.join(all_links))
        
        
                
        
        
    
      
