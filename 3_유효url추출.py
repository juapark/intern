import csv

file_path = '/Users/parkjua/PycharmProjects/python_batch_bucketstore-intern/pagetime/20230925체류횟수추가.csv'  # Replace with the actual file path
output_file_path = '/Users/parkjua/PycharmProjects/python_batch_bucketstore-intern/pagetime/20230925_유효url추가.csv'  # Replace with the desired output file path

# URL이 특정 키워드로 시작하는지 확인하는 함수
def starts_with_keyword(url, keywords):
    return any(url.startswith(keyword) for keyword in keywords)

# 특정 키워드로 시작하면 해당 값을 반환
def assign_visit_value(url):
    start_keywords = ['/display/mall', '/display/outlet', '/display/brand', '/display/search', '/display/lookbook', '/deal/detail', '/customer/join', '/order/form',
                      '/order/complete', '/goods/detail/form', '/planning/detail', '/mypage/order/detail', '/mypage/main/form', '/mypage/info']
    if starts_with_keyword(url, start_keywords):
        if any(param in url for param in ['planDtlSq=8398', 'planDtlSq=8397', 'planDtlSq=8396', 'planDtlSq=8395', 'planDtlSq=8394', 'planDtlSq=8393']):
            return 2
        else:
            return 1
    else:
        return 0

# CSV 파일을 읽고 'visit' 열을 업데이트
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

    # 'visit' 열 제목 추가
    rows[0].append('visit')

    # 각 행을 반복하며 URL에 따라 'visit' 열을 업데이트
    for row in rows[1:]:
        url = row[2]  # URL은 세 번째 열에 위치
        visit_value = assign_visit_value(url)
        row.append(str(visit_value))

# 업데이트된 데이터를 새 CSV 파일에 저장
with open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

print('처리 완료. 데이터는', output_file_path, '에 저장되었습니다.')


#
# # URL이 특정 키워드를 포함하는지 확인하는 함수
# def contains_keyword(url, keywords):
#     return any(keyword in url for keyword in keywords)
#
# # 특정 키워드를 포함하면 해당 값을 반환
# def assign_visit_value(url):
#     if contains_keyword(url, ['/display', '/order', '/goods/detail', '/planning']):
#         if 'planDtlSq=8398' in url:
#             return 2
#         else:
#             return 1
#     else:
#         return 0
#
# # CSV 파일을 읽고 'visit' 열을 업데이트
# with open(file_path, 'r', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     rows = list(reader)
#
#     # 'visit' 열 제목 추가
#     rows[0].append('visit')
#
#     # 각 행을 반복하며 URL에 따라 'visit' 열을 업데이트
#     for row in rows[1:]:
#         url = row[2]  # URL은 세 번째 열에 위치
#         visit_value = assign_visit_value(url)
#         row.append(str(visit_value))
#
# # 업데이트된 데이터를 새 CSV 파일에 저장
# with open(output_file_path, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(rows)
#
# print('처리 완료. 데이터는', output_file_path, '에 저장되었습니다.')
#
