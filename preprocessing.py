import json
import datetime
import os
import ast
import csv


def preprocessing_abebooksdata():
    f = open("./data/Final4.txt", "a")
    fa = open("./data/abebooksdata.json","r")

    # with open('task5.txt') as json_file:
    #     data1 = json.load(json_file)
    data = dict()

    for line in fa.readlines():
        data_line = dict()
        line = line[:len(line)-2]
        print line
        data_line = ast.literal_eval(line)
        print data_line
        test =json.dumps(data_line)
        # test = {"Publisher": ["Arthur A. Levine Books", "(2003)"], "Author": ["Rowling, J. K."], "ISBN 10": "0439554934", "ISBN 13": "9780439554930", "Book Name": ["Harry Potter and the Sorcerer's Stone - Library Edition"]}
        row = json.loads(test)
        print row
        # print row[0]
        print row['Publisher']
        data['Website'] = 'www.abebooks.com'
        if len(row['Book Name']) > 0:
            data['Book Name'] = row['Book Name'][0]
        if len(row['Author']) > 0:
            data['Author'] = row['Author'][0]
        if len(row['ISBN 10']) > 0:
            data['ISBN 10'] = row['ISBN 10']
        if len(row['ISBN 13']) > 0:
            data['ISBN 13'] = row['ISBN 13']
        if len(row['Publisher']) > 2:
            data['Publisher'] = row['Publisher'][0]
            data['Publishing year'] = row['Publisher'][1]
        else :
            if len(row['Publisher']) >0:
                data['Publisher'] = row['Publisher'][0]
        write_str = json.dumps(data)
        print write_str
        f.writelines(write_str + '\n')

    f.close()
    fa.close()


def preprocessing_bookfinder():
    f = open("./data/Final2book.txt", "a")
    fb = open("./data/bookfinder.json", "r")

    # with open('task5.txt') as json_file:
    #     data1 = json.load(json_file)
    data = dict()

    for line in fb.readlines():
        data_line = dict()
        line = line[:len(line) - 2]
        print line
        data_line = ast.literal_eval(line)
        # print data_line
        test = json.dumps(data_line)
        print test
        # test = {"Publisher": ["Arthur A. Levine Books", "(2003)"], "Author": ["Rowling, J. K."], "ISBN 10": "0439554934", "ISBN 13": "9780439554930", "Book Name": ["Harry Potter and the Sorcerer's Stone - Library Edition"]}
        row = json.loads(test)
        print row
        # print row[0]
        # print row['Publisher']
        data['Website'] = 'www.bookfinder.com'
        if len(row['Book Name']) > 0:
            data['Book Name'] = row['Book Name'][0]
        if len(row['Author']) > 0:
            data['Author'] = row['Author'][0]
        if len(row['ISBN10']) > 0:
            data['ISBN 10'] = row['ISBN10']
        if len(row['ISBN13']) > 0:
            data['ISBN 13'] = row['ISBN13']
        if len(row['Publisher']) > 2:
            data['Publisher'] = row['Publisher'][0]
            data['Cover'] = row['Publisher'][1]
            data['Language'] = row['Publisher'][2]
        else :
            if len(row['Publisher']) > 0:
                data['Publisher'] = row['Publisher'][0]

        write_str = json.dumps(data)
        print write_str
        f.writelines(write_str + '\n')

    f.close()
    fb.close()


    # for line in fb.readlines():
    #     row = json.loads(line)
    #     f.write(json.dumps("www.bookfinder.com"+','+row['Book Name']+','+row['Author']+','+row['ISBN10']+','+row['ISBN13']+','+row['Publisher'][0]+'\n'))
    # fb.close()

def preprocessing_isbn():
    fi = open("./data/isbns.json")
    f = open("./data/Final2book.txt", "a")

    for line in fi.readlines():
        row = json.loads(line)
        if row['text']=="Author":
            f.write(json.dumps('\n'+"www.isbndb.com"+','+row['value']+','))
        if(row['text']=="Full Title:"):
            f.write(json.dumps(row['value']+','))
        if (row['text'] == "ISBN"):
            f.write(json.dumps(row['value'] + ','))
        if (row['text'] == "ISBN13"):
            f.write(json.dumps(row['value'] + ','))
        if (row['text'] == "Publisher"):
            f.write(json.dumps(row['value']))
    f.close()
    fi.close()

def preprocessing_goodreads():
    f = open("./data/Finalgoodreads.txt", "a")

    dataset = open("./data/goodreads.csv", "r")
    bookrow = csv.reader(dataset)
    header = bookrow.next()

    data = dict()

    for row in bookrow:
        data['Website'] = 'https://www.goodreads.com/book'
        data['Book Name'] = row[10]
        data['Original Title'] = row[9]
        data['Author'] = row[7]
        data['ISBN 10'] = row[5]
        data['ISBN 13'] = row[6]
        data['Publishing year'] = row[8]
        data['Publiser'] = ""
        data['Language'] = row[11]
        data['Books Count'] = row[4]
        data['Average Rating'] = row[12]

        write_str = json.dumps(data)
        print write_str
        f.writelines(write_str + '\n')


    f.close()


# preprocessing_abebooksdata()
# preprocessing_bookfinder()
# preprocessing_isbn()
preprocessing_goodreads()
