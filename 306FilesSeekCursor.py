#manipulate the position of the cursor with "seek"

# run the below in Console
f=open("article_titles.txt")

f.read()
f.seek(1000)    # place cursor at character 1000
f.read()    # reads from position 1000 onwards


f.readline()    #reads line by line (stops at \n)
f.readline()    # this reads another line
f.readline()    # and another one

#help(f)

f.seek(0)   #move cursor back to beginning of file
f.readlines()   # returns all lines in a list

f.close()   # close file with close() method
f.closed    # check if file is closed with closed property

