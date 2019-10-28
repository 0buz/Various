import csv

# ========== Find the maximum length from a set of words; useful for defining the max length for a datatype in Postgres db ==============
with open('ign.csv', 'r') as f:
    next(f) # skip the row containing column headers
    reader = csv.reader(f)
    # create a set to contain all score phrases
    unique_words_in_score_phrase = set()
    for row in reader:
        # add the score phrase from this row to the set
        score_phrase = row[1]
        unique_words_in_score_phrase.add(score_phrase)

lens=[]
for score_phrase in unique_words_in_score_phrase:
  lens.append(len(score_phrase))

print(max(lens))
#======================================================================================================================