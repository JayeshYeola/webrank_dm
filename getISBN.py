fp = open("./webrank/data/isbndb.json","r")
isbn10 = []
for line in fp.readlines():
    # print line
    if(len(line) > 35):
        if("ISBN:" in line):
            isbn = line[29:39]
            print isbn
            isbn10.append(isbn)

fp.close()