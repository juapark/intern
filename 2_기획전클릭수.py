import pandas as pd

df = pd.read_csv('/Users/parkjua/PycharmProjects/python_batch_bucketstore-intern/page/20231206_log.csv')

escape_chars = r'[-[\]{}()*+?.,\\^$|#\s]'

# "/planning/detail/form?planSq=4076"을 포함하는 행 추출
matching_rows_count = df['Request'].str.contains('/planning/detail/form\?planSq=4076', na=False, regex=True).sum()


# 추출된 행 출력
print("Matching Rows:")
print(matching_rows_count)
