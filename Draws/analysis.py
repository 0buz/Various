import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import settings



df = pd.read_csv('PastDraws.csv', dtype=settings.DTYPES, parse_dates=['Date'])
data=df[['Star1','Star2']].to_numpy()

#combinations = df[['Star1','Star2']].groupby(['Star1','Star2']).agg(['count'])
combinations = df[['Star1','Star2']].groupby(['Star1','Star2']).size()#.sort_values(ascending=False)

count=df.groupby(['Star1','Star2']).size().to_frame('Star1-Star2 Count')
df=pd.merge(df, count, on=['Star1','Star2']).sort_values(by='Date', ascending=False)

df.to_csv('PastDraws_processed.csv', index=False, header=True)


unstack=df.groupby(['Star1','Star2']).size().unstack(level='Star2', fill_value=0)

df = df.groupby(['Star1','Star2']).value_count.reset_index(name='Count')
df['Count']=df.groupby(['Star1']).size().to_frame('Count')


cmb=combinations.plot.bar()

# for x,y in zip(combinations.axes,combinations):
#     plt.annotate('{:.0f}'.format(y), xy=(x,y), xytext=(0,5), textcoords='offset points',ha='center')
#

plt.show()


# # ========================= Bar plot =============================================================
# stems = plt.stem(unique, counts, use_line_collection=True)
# plt.xticks(unique, unique)
# plt.title('Most drawn stars')
# plt.xlabel('Number')
# plt.ylabel('Count')
# for x,y in zip(unique, counts):
#     plt.annotate('{:.0f}'.format(y), xy=(x,y), xytext=(0,5), textcoords='offset points',ha='center')
#
# plt.xticks(unique)   #ticks on x-axis are the individual 'unique' numbers
# #plt.stem(unique, counts, use_line_collection=True)
#
# plt.show()
#
# #==================================================================================================

stars=np.concatenate(data)

unique, counts = np.unique(stars, return_counts=True)
print("Numbers:", unique)
print("Counts:", counts)

#
# ========================= Bar plot =============================================================
# x = np.arange(1,len(unique)+1) # the label locations; needs to start at 1, not 0
# print(x)
# bars=plt.bar(x, counts, width=0.5)
#
# plt.xticks(unique)
# #plt.yticks(counts)
# plt.title('Most drawn stars')
# plt.xlabel('Number')
# plt.ylabel('Count')
#
# def autolabel():
#     """Attach a text label above each bar, displaying its height."""
#     for bar in bars:
#         height = bar.get_height()
#         plt.annotate('{}'.format(height),
#                     xy=(bar.get_x() + bar.get_width() / 2, height),
#                     xytext=(0, 1),  # 1 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
#
# autolabel()
#
# #plt.hist(counts, unique)
#
# plt.show()
#==================================================================================================

# ========================= Stem plot =============================================================
stems = plt.stem(unique, counts, use_line_collection=True)
plt.xticks(unique, unique)
plt.title('Most drawn stars')
plt.xlabel('Number')
plt.ylabel('Count')
for x,y in zip(unique, counts):
    plt.annotate('{:.0f}'.format(y), xy=(x,y), xytext=(0,5), textcoords='offset points',ha='center')

plt.xticks(unique)   #ticks on x-axis are the individual 'unique' numbers
#plt.stem(unique, counts, use_line_collection=True)

plt.show()
#==================================================================================================


# =================== As pie chart =============================================================
# plt.pie(counts, labels=unique, autopct='%1.1f%%',
#         shadow=True, startangle=45)
# #plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()

# fig1, ax1 = plt.subplots()
# ax1.pie(counts, labels=unique, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()
#==================================================================================================