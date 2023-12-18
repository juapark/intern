import pandas as pd
file_path = '/Users/parkjua/PycharmProjects/python_batch_bucketstore-intern/pagetime/추석기획전/20230925_visit.csv'

df = pd.read_csv(file_path)
print(df)
# df2 = df[df['visit']==2]
# df2.to_csv('df2.csv')

indices_to_keep = []
for i in range(len(df) - 1):
    if df['visit'].iloc[i] == 2:
        if df['IP'].iloc[i] == df['IP'].iloc[i + 1] and df['opp'].iloc[i] == df['opp'].iloc[i + 1]:
            if df['visit'].iloc[i + 1] == 1:
                df.at[i, 'pick'] = 'p'
                df.at[i + 1, 'pick'] = 'n'
                indices_to_keep.extend([i, i+1])
        else:
            df.at[i, 'pick'] = 'o'
            indices_to_keep.extend([i])
df_filtered = df.iloc[indices_to_keep]
# 결과 출력
print(df_filtered)
df_filtered.to_csv('20230925_col.csv', index=None)
print('finish')


# df['pick'] = 'o'  # 기본적으로 'o' 할당
# indices_to_keep = []
# for i in range(len(df) - 1):
#     if df['IP'].iloc[i] == df['IP'].iloc[i + 1] and df['opp'].iloc[i] == df['opp'].iloc[i + 1]:
#         if df['visit'].iloc[i] == 2:
#             if df['visit'].iloc[i + 1] == 1:
#                 df.at[i, 'pick'] = 'p'
#                 df.at[i + 1, 'pick'] = 'n'
#                 indices_to_keep.extend([i, i + 1])
#             else:
#                 df.at[i, 'pick'] = 'o'
#                 indices_to_keep.extend([i])
# df_filtered = df.iloc[indices_to_keep]
# print(df_filtered)
# df_filtered.to_csv('체류시간추출컬럼추가.csv')
# df['pick'] = 'o'
#
# indices_to_keep = []
# for i in range(len(df) - 1):
#     if df['visit'].iloc[i] == 2:
#         if df['visit'].iloc[i] == 2 and df['visit'].iloc[i + 1] == 1:
#             df.at[i, 'pick'] = 'p'
#             df.at[i + 1, 'pick'] = 'n'
#             indices_to_keep.extend([i, i+1])
#         else:
#             df.at[i, 'pick'] = 'o'
#             indices_to_keep.extend([i])
# df_filtered = df.iloc[indices_to_keep]
# # 결과 출력
# print(df_filtered)
# df_filtered.to_csv('체류시간추출컬럼추가.csv')



# indices_to_keep = []
# for i in range(len(df) - 1):
#     if df['visit'].iloc[i] == 2:
#         indices_to_keep.extend([i])
#     if df['visit'].iloc[i] == 2 and df['visit'].iloc[i + 1] == 1:
#         indices_to_keep.extend([i, i + 1])
#
# df_filtered = df.iloc[indices_to_keep]
#
# # 'pick' 컬럼 생성
# df_filtered['pick'] = df_filtered.apply(lambda row: 'p' if row['visit'] == 2 else 'n', axis=1)
#
# # 결과 출력
# print(df_filtered)
# df_filtered.to_csv('체류시간추출컬럼추가.csv')
