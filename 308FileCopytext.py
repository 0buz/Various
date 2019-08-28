def copy(filename1,filename2):
    with open(filename1,"r") as f1:
        text=f1.read()

    with open(filename2, "w") as f2:
        f2.write(text)

def copy_and_reverse(filename1, filename2):
    with open(filename1,"r") as f1:
        text=f1.read()

    with open(filename2, "w") as f2:
        f2.write(text[::-1])

def statistics(filename1):
    with open(filename1,"r") as f1:
        text=f1.read()
        f1.seek(0)
        lines=f1.readlines()

    words = text.split()
    return {
        "lines":len(lines),
        "words":len(words),
        "characters":len(text)
            }

def find_and_replace(filename,find,replace):
    with open(filename, "r+") as f:
        text=f.read()
        updated_text=text.replace(find, replace)
        f.seek(0)
        f.write(updated_text)
        f.truncate()

#copy("story.txt","story_copy.txt" )
#copy_and_reverse("story.txt", "story_reverse.txt")
#print(statistics("story.txt"))

find_and_replace("story_copy.txt","Alice","Adrian")

