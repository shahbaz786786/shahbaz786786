import csv
with open("leaf_dataset.csv","r") as obj:
    csv_reader=csv.DictReader(obj)
    for line in csv_reader:
        print(line["species"])

