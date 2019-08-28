with open("article_titles.txt") as f:
    data=f.read()

f.closed     # "with" will close the file automatically

print(data)

with open("new_file.txt", "w") as f:      #  >>>>>>> this overwrites what was in the file
    f.write("New file created by running the python command. \n")
    f.write("New line in created with the file. \n")

# with open("article_titles.txt", "w") as f:      #  >>>>>>> this overwrites what was in the file
#     f.write("My line \n")


with open("article_titles.txt", "a") as f:       # "a" append; add lines at the end of the file; always at the end
    f.write("My added line.\n")
    f.write("\nMy second added line.\n")

with open("article_titles.txt", "r+") as f:  # "r+"  read and write to a file (writing based on cursor)
    f.write("Added using r+.\n")             # r+ adds at the beginning of the file by default; overwriting whatever was there previously on the first line !!!
    f.seek(50)
    f.write("\nAdded at position 50 with r+.\n")   # r+ adds at the position with seek, overwriting whatever was there previously
    f.seek(2)
    f.write("\n<<<<Added at position 2 with r+.>>>>\n")



