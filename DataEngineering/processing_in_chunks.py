import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dtypes = {"posted_date": "datetime64[ns]", "created_date": "datetime64[ns]"}

# ===== optimise execution time by loading only relevant columns with usecols  =============================
lifespans = []
chunk_iter = pd.read_csv("/home/adrian/Python/ModernPython3Bootcamp/Various/DataEngineering/moma.csv", chunksize=250, dtype={"ConstituentBeginDate": "float", "ConstituentEndDate": "float"},  usecols=['ConstituentBeginDate', 'ConstituentEndDate'])
for chunk in chunk_iter:
    lifespans.append(chunk['ConstituentEndDate'] - chunk['ConstituentBeginDate'])

lifespans_dist = pd.concat(lifespans) # pd.concat to concatenate chunk results for overall df result
print(lifespans_dist)
#============================================================================================================


#================  =============================================
overall_vc = []
chunk_iter = pd.read_csv("/home/adrian/Python/ModernPython3Bootcamp/Various/DataEngineering/moma.csv", chunksize=250, usecols=['Gender'])
for chunk in chunk_iter:
    chunk_vc=chunk['Gender'].value_counts()
    overall_vc.append(chunk_vc)

combined_vc = pd.concat(overall_vc)






#============================================================================================================