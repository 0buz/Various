from csv import reader, writer, DictReader, DictWriter

# ==========================        Reading CSV using reader       =======================================
# with open("season-1819.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader)   #skip header
#     for row in csv_reader:
#         #print(row)     #each row is represented as a list, header included!
#         print(f"{row[2]} scored {row[4]} goals  this match.")


with open("season-1819.csv") as file:
    csv_reader = reader(file)
    data_list = list(csv_reader)  # each row is a list
    for match in data_list:
        # print(row)     #each row is represented as a list, header included!
        print(match[0])

# ===========================================================================================================


# ==========================        Reading CSV using DictReader       =======================================
with open("season-1819.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # print(row)     #each row is an orderd dictionary
        print(row["HomeTeam"])

# ===========================================================================================================


# ============================        Writing CSV using writer       =======================================
with open("season-1819_new.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(
        ['E0', '12/05/2019', 'Dummy Home', 'Dummy Away', '1', '4', 'A', '0', '2', 'A', 'D Dumm', '17', '16', '8', '9',
         '10', '10', '7', '2', '1', '0', '1', '0', '2.25', '3.75', '3.2', '2.2', '3.7', '3.1', '2.2', '3.75', '3.05',
         '2.2', '3.85', '3.21', '2.2', '3.7', '3.1', '2.2', '3.75', '3.25', '35', '2.26', '2.2', '3.9', '3.73', '3.25',
         '3.13', '33', '1.6', '1.55', '2.56', '2.44', '19', '-0.5', '2.25', '2.19', '1.78', '1.72', '2.11', '3.86',
         '3.41'])
# ===========================================================================================================


# ============================        writer exercise       =======================================
with open("season-1819.csv") as file:
    csv_reader = reader(file)
    data_list = [[s.upper() for s in row] for row in csv_reader]
    for row in data_list:
        print(row)
# ^^^"season-1819.csv" closes at this point

with open("season-1819_ALLCAPS.csv", "w") as file:
    csv_writer = writer(file)
    for row in data_list:
        csv_writer.writerow(row)

# ===========================================================================================================


# ============================        Writing CSV using DictWriter       =======================================
# fieldnames - specifies the header
# writeheader - method to write the header
# writerow - method to write the rest of the rows based on a dictionary

with open("cats.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })

# ===========================================================================================================


# ============================        DictWriter exercise      =======================================

def add_two(x):
    return int(x)+2

with open("season-1819.csv") as file:
    csv_reader = DictReader(file)
    matches=list(csv_reader)

with open("season-1819_add_two.csv","w") as file:  #adding two to FTHG
    headers=["Div","Date","HomeTeam","AwayTeam","FTHG+2","FTAG"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for match in matches:
        csv_writer.writerow({
            "Div": match["Div"],
            "Date": match["Date"],
            "HomeTeam": match["HomeTeam"],
            "AwayTeam": match["AwayTeam"],
            "FTHG+2": add_two(match["FTHG"]),
            "FTAG": match["FTAG"]
        })
# ===========================================================================================================