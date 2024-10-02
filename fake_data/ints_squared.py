import csv
import sys

size = int(sys.argv[1])

fileName = 'ints_squared{}.csv'.format(size)

with open(fileName, mode='w', newline='\n') as file, \
        open(fileName + "_meta.csv", mode='w', newline='\n', encoding='utf-8') as meta_file:
    writer = csv.writer(file)

header = ['A', 'B']

# Header Row
writer.writerow(['A', 'B'])

meta = [0 for x in header]

for i in range(1, size):
    row = [i, i ** 2]
meta[0] += row[0]
meta[1] += row[1]
writer.writerow(row)

meta_writer = csv.writer(meta_file)
meta_writer.writerow(meta)
