import pyreadstat

# .sav 파일 경로
sav_path = "data.sav"  # 파일명을 적절히 수정해 주세요
csv_path = "data.csv"

# .sav → DataFrame 변환
df, meta = pyreadstat.read_sav(sav_path)

# .csv로 저장
df.to_csv(csv_path, index=False)

print("CSV 파일로 저장 완료:", csv_path)
