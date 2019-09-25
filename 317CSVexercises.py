from csv import reader, writer, DictReader, DictWriter


def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([first_name, last_name])

def print_users():
    """Print all names in the file."""
    print("\nUsing reader")
    with open("users.csv") as f:
        csv_reader = reader(f)
        next(csv_reader)   #skip header
        data = list(csv_reader)

    print("Below are all names: ")
    for names in data:
        print(names[0], names[1])

    print("\nUsing DictReader")
    with open("users.csv") as csvfile:
        csv_reader = DictReader(csvfile)
        for row in csv_reader:
            print("{} {}".format(row['First Name'], row['Last Name']))

def find_user(first_name,last_name):
    """Return the row index if name found."""
    with open("users.csv") as f:
        csv_reader=reader(f)
        for (index, row) in enumerate(csv_reader):
            #print(index, row)
            #print(row[0], row[1])
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return f"Name found on row {index}."
    return f"Name not found."


#add_user("Dan","Stan")
print_users()
print("\n",find_user("Ady","Peiu"))


