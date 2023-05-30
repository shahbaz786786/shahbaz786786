import csv
with open("newnew.csv",'w') as obj: # REmember that "w" mode will delete existing record if record exist
    csv_writer=csv.writer(obj, delimiter="\t")
    csv_writer.writerow(["F_name","L_name","Gender","E_mail","City"])
    csv_writer.writerow(["Shahbaz", "Ali","Male","shobi@gmail.com","Layyah"])
    csv_writer.writerow(["Nabiha ", "Komal","Fe-Male","komal@gmail.com","Layyah"])
    csv_writer.writerow(["Muhammad" , "Haseeb","Male","chhaseeb@gmail.com","Layyah"])
    csv_writer.writerow(["Janoon", "Haidar","Male","jh@gmail.com","Lahore"])



with open("newnew.csv","r") as f_obj:
    csv_reader=csv.DictReader(f_obj)

    for line in csv_reader:
        print(line)