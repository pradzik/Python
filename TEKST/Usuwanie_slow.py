import os

bad_words = [" on "," in "," the "," why "," and "]
file_list = os.listdir(path = './data')

for x in file_list:
    print(x)

fn = input("Enter file to open from list above: ")
f =  open('./data/'+fn,"r") 
f_better  = open('./improved_data/ 1_'+fn,"w")

for line in f:
    for word in bad_words:
        line = line.replace(word,'')
    f_better.write(line)

f.close()
f_better.close()
