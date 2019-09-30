from datetime import date
import re


def filename(fname, ftype):
    """Returns filename built as fname+current date+.ftype  e.g. rawdata20190830.csv"""
    curr_date = filter(lambda x: x != "-", str(date.today()))  # filter out dashes; this is not a str yet
    return f"{fname}{''.join(curr_date)}.{ftype}"

def remove_white_space(file):
    """Remove whitespace combination (\n followed by one or more \t) and replace with empty string."""
    with open(file,'r+') as f:
        data=f.read()
        data = re.sub(r'\n\t+','',data)
        f.seek(0)     # place cursor at the beginning
        f.write(data)
        f.truncate()  # remove and extra text left from the pre-edited version





