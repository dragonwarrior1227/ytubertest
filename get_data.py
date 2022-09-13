import pandas as pd
sheet_id = "1hNx5JNmeYTmUSMp4Ke0qHaHaGqI4TtBJ63EuWfh3eAI"
sheet_name = "Sheet1"
url = "https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}".format(sheet_id,sheet_name)
df=pd.read_csv(url)
df=df.dropna(axis=1)
print(df.head())