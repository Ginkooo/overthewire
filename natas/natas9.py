pf = open('dict')
wf = open('words.txt')


pas = dict()
wor = dict()

for line in pf:
    line = line.replace("'s", '').strip()
    pas[line] = True

for line in wf:
    line = line.strip()
    wor[line] = True


x = 0
for word in pas:
    try:
        wor[word]
    except KeyError:
        print(word)
