import csv

file = open("example.csv")
data_raw = csv.reader(file)
data = list(data_raw)


def print_data(data):
    for line in range(len(data)):
        print(f"Id: {line[0]}\n"
              f"Title: {line[1]}\n"
              f"Year: {line[2]}\n"
              f"Rating: {line[3]}\n")


def delete_data(data, file):
    id = input("Provide the ID of movie to delete")
    for x in range(len(data)):
        if data[x][0] == id:
            accept = input("Are you sure? y/n")
            if accept == "y":
                data.pop(x)
        else:
            print("You provided wrong ID")
    return data


def add_data(data):
    id = str(len(data) + 1)
    title = input("Provide title: ")
    year = input("Provide year: ")
    rating = input("Provide rating: ")
    data.append([id, title, year, rating])
    print("Data added to database\n")
    return data


def save_data(data):
    file = open("example.csv", "w")
    save = csv.writer(file)
    save.writerows(data)



while 1:
    print(f"Welcome to movie database ;)\n"
          f"Menu:\n"
          f"show ->Show Data\n"
          f"add -> Add Data\n"
          f"del -> Delete Data\n"
          f"exit -> save and close program\n")
    x = input()
    if x == "exit":
        save_data(data)
        exit()
    elif x == "show":
        print_data(data)
    elif x == "add":
        add_data(data)
    elif x == "del":
        delete_data(data)
    else:
        print("Wrong input")

# It was working but after input data and exit I have error
# """Traceback (most recent call last):
#   File "D:/Studia/Semestr 7/Python/PRACA_Z_DANYMI/CSV.py", line 57, in <module>
#     print_data(data)
#   File "D:/Studia/Semestr 7/Python/PRACA_Z_DANYMI/CSV.py", line 10, in print_data
#     print(f"Id: {line[0]}\n"
# TypeError: 'int' object is not subscriptable"""