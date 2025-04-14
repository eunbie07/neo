import matplotlib.pyplot as plt

# 데이터 정의
labels = [
    "전혀 경험하지 않았다",
    "가끔 경험했다",
    "별로 경험하지 않았다",
    "자주 경험했다"
]
values = [23.6, 28.2, 44.7, 3.5]
average_score = 2.12

# 그래프 생성
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values)

# 제목 및 축 라벨
plt.title("SNS 사용으로 인한 스트레스 경험 비율 (2023)")
plt.ylabel("비율 (%)")
plt.ylim(0, max(values) + 10)

# 막대 위에 수치 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}%', ha='center', va='bottom')

# 평균 점수 주석
plt.text(1.5, max(values) + 5, f"평균 스트레스 점수: {average_score}", ha='center', fontsize=12, color='red')

plt.tight_layout()

# 이미지 파일로 저장 (해상도는 dpi로 조정 가능)
plt.savefig("sns_stress.png", dpi=300)

# plt.show()는 생략하면 화면에는 표시되지 않음