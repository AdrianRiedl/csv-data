import csv
import sys

size = int(sys.argv[1])

fileName = 'ints{}.tsv'.format(size)

with open(fileName, mode='w', newline='\n') as file, \
        open(fileName + "_meta.tsv", mode='w', newline='\n', encoding='utf-8') as meta_file:
    writer = csv.writer(file, delimiter='\t', lineterminator='\n')

    header = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    meta = [0 for x in header]

    for i in range(1, size):
        row = [i] * 10
        for i in range(0, len(meta)):
            meta[i] += row[i]
        writer.writerow(row)

    meta_writer = csv.writer(meta_file)
    meta_writer.writerow(meta)
