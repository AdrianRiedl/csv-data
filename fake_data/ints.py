import csv
import sys

size = int(sys.argv[1])

fileName = 'ints{}.csv'.format(size)

with open(fileName, mode='w', newline='\n') as file, \
        open(fileName + "_meta.csv", mode='w', newline='\n', encoding='utf-8') as meta_file:
    writer = csv.writer(file)

    header = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    # Header Row
    writer.writerow(header)

    meta = [0 for x in header]

    for i in range(1, size):
        row = [i] * 10
        for i in range(0, len(meta)):
            meta[i] += row[i]
        writer.writerow(row)

    meta_writer = csv.writer(meta_file)
    meta_writer.writerow(meta)
