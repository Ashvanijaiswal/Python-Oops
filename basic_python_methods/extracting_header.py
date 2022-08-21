with open(r'header.html','r+') as f:
    l=f.readlines()
    print(l)
    f.seek(0)
    for i,line in enumerate(l):
        if(line.find('<td>')!=-1):
            f=line.index('<td>')
            lst=line.index('</td>')
            print(line[f+4:lst])
