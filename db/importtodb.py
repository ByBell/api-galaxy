import csv
filename = "catalogue-de-messier.csv"
file = open(filename,"rt")

try:
    reader = csv.reader(file)
    for row in reader:
	    print(row[0])
finally:
    file.close()

