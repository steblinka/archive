import re
for sp in range (17):
    speechFile = open(r'E:\py_files\putin\putin %s.txt' % (sp + 1), encoding='utf-8')
    speechFile1 = speechFile.read()
    with open (r'E:\putin\list_geography_int.txt', encoding='utf-8') as f: 
        countries = [row.strip() for row in f]
        for i in range(len(countries)):
            country = re.compile(countries[i])
            country_f = ze.findall(speechFile1)
            for u in counrty_f:
                p = ('%s' % (u))
                print(p)
        print('----- #%s-----' % (sp +1 ))
