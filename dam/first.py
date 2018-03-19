import csv
import operator
import copy

with open('input01.csv', 'r') as f:
    reader = csv.reader(f)
    """header = next(reader)
    headerstr = ', '.join(str(e) for e in header)
    print(headerstr.upper())
    sortedlist = sorted(reader, key=operator.itemgetter(7), reverse=False)
    for row in reader:
        print(row)
    for row in reader:
        if row[1][0] == 'A' or row[2][0]== 'P' or row[2][0]== 'E':
            print(row[1])
    for row in reader:
        row[0], row[15] = row[15],row[0]
        print(row)
    with open('nice', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(reader)"""
    readerstr = ', '.join(map(str, reader))
    for row in readerstr:
        print(readerstr)
