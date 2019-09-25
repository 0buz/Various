#see sup.py !!
# How to prevent running imported code (__name__ relation to __main__)

from sup import say_sup

def say_hi():
    print(f"Hi, my __name__ is {__name__}.")

say_hi()
say_sup()


#3 rows output - that is because the 1st one shows the __name__ from  whatever we imported
# to resolve this, in the import file (sup.py) we change:
# FROM:
# say_sup()
#
# TO:
# if __name__ == "__main__"
#     say_sup()
#


