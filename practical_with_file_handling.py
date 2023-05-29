filename= "shobi1.txt"
with open(filename,'r') as obj:
    content=obj.read()

space=''
for i in content:
    space+=i.rstrip()
print(space)

put=input("Ente you birthday ")
if put in space:
    print("Congratulation you are here ")
else:
    print("O sorry dear you are not of them ")