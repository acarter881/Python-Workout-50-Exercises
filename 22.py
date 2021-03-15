#! python3
import csv

def passwd_to_csv(f1,f2):
    rowList = []
    with open(f1, 'r') as pword:
        for row in pword:
            if row.startswith('#') or row.split() == '':
                pass
            else:
                rowList.append((row.split(':')[0], row.split(':')[2]))
    with open(f2, 'w', newline='') as myObj:
        output = csv.writer(myObj)
        output.writerows(rowList)

passwd_to_csv('unixStyle.txt', 'Lol.csv')
