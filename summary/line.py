mylines = []
with open ('output.txt', 'rt') as myfile:
    for myline in myfile:
        mylines.append(myline)
    x = open('topegasus.txt', 'w')
    x.write(mylines[10])
