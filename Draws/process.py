import pandas as pd
import settings

def star_combination_count(file=settings.RAW_FILE):
    df = pd.read_csv(file, dtype=settings.DTYPES, parse_dates=['Date'])
    count=df.groupby(['Star1','Star2']).size().to_frame('Star1-Star2 Count')
    df=pd.merge(df, count, on=['Star1','Star2']).sort_values(by='Date', ascending=False)
    return df.to_csv(settings.PROCESSED_FILE, index=False, header=True)


if __name__ == '__main__':
    star_combination_count()
