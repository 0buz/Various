import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import settings
from matplotlib.pyplot import figure
#figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

df = pd.read_csv('PastDraws.csv', dtype=settings.DTYPES, parse_dates=['Date'])
data=df[['Star1','Star2']].to_numpy()

data = data.astype('float')
data[data == 6]=np.NaN

print(data.dtype)

print(data)

for i in range(len(data)):
    for j in range(len(data)):
        if data[i,j]==6:
            data[i,j]=np.nan



print(df.iloc[2][2])
df=pd.DataFrame()

start_time=pd.to_datetime("21:00:00").time
stop_time=pd.to_datetime("14:30:00").time()

df = df[~(df['Date'].dt.time >= start_time) & ~(df['Date'].dt.time <= stop_time)]

df['Star1']=df['Star1'].astype(str).str.replace('6','0').astype(int)
print(df['Date'])

combinations = df.groupby(['Star1','Star2']).size().sort_values(ascending=False)
unstack=df.groupby(['Star1','Star2']).size().unstack(level='Star2', fill_value=0)
print(combinations.values)

index=str(combinations.index)
values=combinations.values

for co in combinations:
    print(co)

plt.hist()
cmb=combinations.plot.bar()
# for x,y in zip(index,values):
#     plt.annotate('{:.0f}'.format(y), xy=(x,y), xytext=(0,5), textcoords='offset points',ha='center')

#cmb.figure(figsize=(20,10)).show()
plt.figure(figsize=(20,10))
plt.show()

df['x']="12,3"
print(df['x'])

df['x']=pd.to_numeric(df['x'])

df.iloc[:,1:].apply(pd.to_numeric(df, downcast='integer'))
print(df['x'])

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