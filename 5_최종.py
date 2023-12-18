import pandas as pd
from datetime import datetime


# df = pd.DataFrame(data, columns=['ip', 'date', 'request', 'opp', 'visit', 'pick'])
df = pd.read_csv('/Users/parkjua/PycharmProjects/python_batch_bucketstore-intern/pagetime/추석기획전/20230925_col.csv')
print(df)


# 'pick' 값이 'o'인 경우에는 None으로 변경
df['time'] = df.apply(lambda row: None if row['pick'] == 'o' else None, axis=1)

last_p_time = None
for index, row in df.iterrows():
    if row['pick'] == 'p':
        last_p_time = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S')
    elif row['pick'] == 'n' and last_p_time is not None:
        current_n_time = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S')
        duration = current_n_time - last_p_time
        df.at[index, 'time'] = str(duration)

# 결과 출력 (ip, opp, time)
result_df = df[df['time'].notna()][['IP', 'opp', 'time']]
print(result_df)
result_df.to_csv('20230925result.csv')
print('finish')
