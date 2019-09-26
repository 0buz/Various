from datetime import date


def filename(fname, ftype):
    """Returns filename built as fname+current date+.ftype  e.g. rawdata20190830.csv"""
    curr_date = filter(lambda x: x != "-", str(date.today()))  # filter out dashes; this is not a str yet
    return f"{fname}{''.join(curr_date)}.{ftype}"