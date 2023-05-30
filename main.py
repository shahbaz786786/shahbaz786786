import csv
with open("leaf_dataset.csv","r") as obj:
    csvreader = csv.reader(obj)
    print(csvreader)
    with open("new.csv","w") as f:
        csvwriter= csv.writer(f, delimiter="\t")
        for line in csvreader:
            csvwriter.writerow(line)

        print(csvwriter)