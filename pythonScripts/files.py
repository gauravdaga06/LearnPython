from inventory import fruits

with open("fruits.txt", "w") as fr:
    for f_name in fruits.keys():
        fr.write(f"{f_name} \n")


with open("fruits.txt" , "r") as fr: 
    for line in fr:
        print(line.strip().upper())