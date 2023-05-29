# with open("shobi.txt","r") as obj:
#     content=obj.read()
#     print(content)
#
# with open("D:/test/shobi.txt", "r") as fobj:
#     con= fobj.read()
#     print(con)

"""
with open("shobi.txt","r") as obj:
    content=obj.read()
    print(content.rstrip())
"""



# Printing line by line in the file.
with open("shobi.txt",'r') as obj:
    for line in obj:
        print(line)

## Making list in file
file="shobi.txt"
with open(file,'r') as object:
    lines=object.readlines()
for i in lines:
    print(i)
 


### end lines in the file and convert into list


with open(file,'r') as fobj:
    my=fobj.readlines()
my_list= ' ' # this is last thing that is used for the contcatinating
for i in my:
    my_list += i.rstrip()    # rstrip is necessary because it removes the last ENTER
print(my_list)

## Writing the objects
""" Remember one thing if your file doesn't exist in the folder the write mofe will creat  file 
automatically in your distinct folder of the objcct
And if you write any thing in existting file thent this will delete all previous things from your file"""

with open("shobi2.txt",'w') as sho:
    sho.write('I am in \n')  # You don't need have any variable there becasue it will write only

## Append
""" To overcome th overwrite problem from the write mode we use append mode that put the digits without
any deletion """
with open('shobi2.txt','a') as shob:
    shob.write("Welcome I am here with you dear ")# No need of variable

## Read + write
"""
This is denote by the r+ and use for both cases read and wrete but write functoon sill remove 
all the things in the fiel """

with open("shobi2.txt","r+") as shobiz:
    shobiz.write("Shahbaz Ali")
    a = shobiz.read()
    print(a)