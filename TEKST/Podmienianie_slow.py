import os

dictionary = {
    " i ": "oraz",
    "oraz": "i",
    "nigdy": "prawie nigdy",
    "dlaczego": "czemu"

 }        
file_list = os.listdir(path = './data')

for x in file_list:
    print(x)

fn = input("Enter file to open from list above: ")
f =  open('./data/'+fn,"r")
f_better  = open('./improved_data/2_ '+fn,"w")

for line in f:
    for word in dictionary:
        #if dictionary.get(word):
        line = line.replace(word,dictionary.get(word))
    f_better.write(line)


f.close()
f_better.close()
