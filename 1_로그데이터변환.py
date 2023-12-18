import csv
from datetime import datetime

# 로그 파일 경로
log_file_path = '/Users/parkjua/PycharmProjects/python_batch_bucketstore-intern/page/data/a-access.log-20231206'

# CSV 파일 경로
csv_file_path = '20231206_log.csv'

# 로그 파일을 읽고 CSV 파일로 변환
with open(log_file_path, 'r') as log_file, open(csv_file_path, 'w', newline='') as csv_file:
    log_reader = log_file.readlines()
    csv_writer = csv.writer(csv_file)

    # CSV 파일의 헤더를 작성
    csv_writer.writerow(["IP", "Date", "Request"])

    for line in log_reader:
        # 로그 라인을 빈칸을 기준으로 분할
        parts = line.split()

        # 필요한 정보 추출
        ip = parts[0]
        date = parts[3].replace("[", "")
        date_obj = datetime.strptime(date, "%d/%b/%Y:%H:%M:%S")
        formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")
        request = parts[6]

        # 추출한 정보를 CSV 파일에 쓰기
        csv_writer.writerow([ip, formatted_date, request])

print(f"로그 파일을 {csv_file_path}로 성공적으로 변환하였습니다.")
