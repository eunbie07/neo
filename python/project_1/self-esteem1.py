import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ✅ 1. NanumBarunGothic 폰트 경로 직접 지정
plt.rcParams['font.family'] = 'NanumBarunGothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 부호 깨짐 방지

# ✅ 2. 데이터 불러오기
df = pd.read_csv("data.csv", low_memory=False)

# ✅ 3. 필요한 열 선택
selected_columns = [
    'Q35M1',  # 하루 평균 SNS 사용 시간
    'Q14A1', 'Q14A2', 'Q14A3', 'Q14A4', 'Q14A5',
    'Q14A6', 'Q14A7', 'Q14A8', 'Q14A9', 'Q14A10'  # 자존감 관련 문항들
]
df_selected = df[selected_columns].copy()

# ✅ 4. 자존감 점수 계산 (10개 항목 평균)
df_selected['Self_Esteem_Score'] = df_selected.loc[:, 'Q14A1':'Q14A10'].mean(axis=1)

# ✅ 5. 컬럼명 변경
df_selected.rename(columns={'Q35M1': 'SNS_Usage_Time'}, inplace=True)

# ✅ 6. 결측치 제거
df_clean = df_selected[['SNS_Usage_Time', 'Self_Esteem_Score']].dropna()

# ✅ 7. 그래프 그리기
sns.set(style='whitegrid')
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_clean, x='SNS_Usage_Time', y='Self_Esteem_Score', alpha=0.5)
sns.regplot(data=df_clean, x='SNS_Usage_Time', y='Self_Esteem_Score', scatter=False, color='green')
# plt.title('SNS 사용 시간과 자존감 점수의 관계')
plt.title('Impact of Social Media Usage Time on Self-Esteem')
plt.xlabel('Time Spent on Social Media (hours/day)')
plt.ylabel('Self-Esteem Score (Average)')
plt.tight_layout()

# ✅ 8. 그래프 파일로 저장
output_path = 'sns_vs_selfesteem.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f'✅ 그래프 저장 완료: {output_path}')

# plt.show()  # CLI 환경에서는 생략 가능
