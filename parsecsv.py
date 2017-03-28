import os
import pprint
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

'''
def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(",")
        print header
        counter = 0
        for line in f:
            if counter == 10:
                break

            fields = line.split(",")
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1

    return data
'''

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data

'''
def test():
    # a simple test of your implementation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[0] == tenthline

test()
'''

if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    parse_csv(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)


# parse_file(DATAFILE)
