import csv

with open('database.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[1]} {row[2].split()[0]} es del colegio {row[8]}, y su papa se llama {row[14]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
