def copy(filename1,filename2):
    with open(filename1,"r") as f1:
        text=f1.read()

    with open(filename2, "w") as f2:
        f2.write(text)

copy("story.txt","story_copy.txt" )

