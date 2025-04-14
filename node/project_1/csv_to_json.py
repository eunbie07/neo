import csv
import json

# CSV 파일 경로
csv_file = 'stress.csv'
# 저장할 JSON 파일 경로
json_file = 'stress.json'

# CSV 파일 열기
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# JSON 파일로 저장
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)