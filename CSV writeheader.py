
import csv
with open("new.csv","r") as f_obj:
    csv__reader=csv.reader(f_obj)

    with open("shobi.csv","w") as f:

        fieldnames=['id','species','margin1','margin2','margin3']
        csv_writer=csv.DictWriter(f,fieldnames=fieldnames,delimiter="\t")
        csv_writer.writeheader()

        for line in csv__reader:
            print(line)