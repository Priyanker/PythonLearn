import re
li= list()
hand = open('abc.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        li = re.findall('[0-9.]+', line)
        if len(li) > 0:
            print(li)
