import mimesis
import csv
import random
import os
import sys

size = int(sys.argv[1])

person = mimesis.Person(locale='en')
genderEnum = mimesis.enums.Gender

fileName = 'persons{}.csv'.format(size)

with open(fileName, mode='w', newline='\n') as file, \
        open(fileName + "_meta.csv", mode='w', newline='\n', encoding='utf-8') as meta_file:
    writer = csv.writer(file)

    header = ['Id', 'Full Name', 'Age', 'Occupation', 'Email', 'Telephone', 'Nationality']

    # Header Row
    writer.writerow(header)

    meta = [0 for x in header]

    for i in range(0, size):
        rando = random.uniform(0, 1)
        if rando >= 0.5:
            gender = genderEnum.FEMALE
        else:
            gender = genderEnum.MALE

        row = [
            i,
            person.full_name(gender=gender),
            random.randint(0, 99),
            person.occupation(),
            person.email(),
            person.telephone(),
            person.nationality()
        ]
        # calculate the meta data
        meta[0] += int(row[0])
        meta[1] += len(row[1])
        meta[2] += int(row[2])
        meta[3] += len(row[3])
        meta[4] += len(row[4])
        meta[5] += len(row[5])
        meta[6] += len(row[6])

        writer.writerow(row)

    meta_writer = csv.writer(meta_file)
    meta_writer.writerow(meta)
