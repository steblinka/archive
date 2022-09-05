import re
headlinesFile = open(r'E:\dt\dt_march.txt', encoding='utf-8') 
headlinesFile1 = headlinesFile.read()
name_1 = re.compile(r'Зеленськ') 
head = name_1.findall(headlinesFile1)
box = ('\n'.join(head))
total = box.count('Зеленськ')
print('Зеленський:', total)
