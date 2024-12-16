import csv
import random
import sys

if "--help" in sys.argv:
    print(
        "Usage: python3 ints_null.py <number of rows (integer)> <number of columns (integer)> <percentage of null values (integer between 0 and 100)>")

size = int(sys.argv[1])

columns = int(sys.argv[2])
assert columns > 0

percentage = int(sys.argv[3])
assert 0 <= percentage <= 100

fileName = 'ints_null{}.csv'.format(size)

numberOfNotNullValues = int(size * (100 - percentage) / 100)

with open(fileName, mode='w') as file:
    writer = csv.writer(file, lineterminator='\n')

    header = range(0, columns)

    columnData = []

    for i in range(0, numberOfNotNullValues):
        columnData.append(str(i))
    for i in range(numberOfNotNullValues, size):
        columnData.append("NULL")

    tableData = [columnData.copy() for i in range(0, columns)]
    for col in tableData:
        random.shuffle(col)

    for i in range(0, len(tableData[0])):
        row = [col[i] for col in tableData]
        writer.writerow(row)
