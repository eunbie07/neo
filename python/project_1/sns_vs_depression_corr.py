import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from scipy.stats import pearsonr

# ✅ 1. 한글 폰트 직접 지정 (NanumBarunGothic)
font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'  # 시스템 내 설치 확인
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# ✅ 2. 데이터 불러오기
df = pd.read_csv("data.csv", low_memory=False)

# ✅ 3. 변수명 정리 및 우울감 이진화
df.rename(columns={'Q35M1': 'SNS_Usage_Time', 'Q26A1': 'Depression'}, inplace=True)
df['Depression_Binary'] = df['Depression'].apply(lambda x: 1 if x == 1 else 0)

# ✅ 4. 상관관계 분석
df_corr = df[['SNS_Usage_Time', 'Depression_Binary']].dropna()
r, p = pearsonr(df_corr['SNS_Usage_Time'], df_corr['Depression_Binary'])

# ✅ 5. 시각화
sns.set(style='whitegrid')
plt.figure(figsize=(9, 6))

# 산점도: 우울감(0=없음, 1=있음) vs SNS 사용 시간
sns.stripplot(
    data=df_corr,
    x='Depression_Binary',
    y='SNS_Usage_Time',
    alpha=0.5,
    jitter=0.25,
    palette=['#00AAFF', '#FF5555']
)

# 회귀선
sns.regplot(
    data=df_corr,
    x='Depression_Binary',
    y='SNS_Usage_Time',
    scatter=False,
    color='green',
    line_kws={'linewidth': 2}
)

# 제목 및 라벨
plt.suptitle('Relationship Between Depression and Time Spent on SNS', fontsize=14, weight='bold', y=1.02)
plt.xlabel('Experience of Depression (0=No, 1=Yes)', fontsize=12)
plt.ylabel('Average Daily Time Spent on SNS (hours/day)', fontsize=12)

# 상관계수 표시
plt.text(
    0.5, max(df_corr['SNS_Usage_Time']) + 1,
    f"Pearson correlation: r = {r:.3f}, p-value = {p:.1e}",
    fontsize=10,
    horizontalalignment='center',
    bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white')
)

plt.tight_layout()

# ✅ 6. 그래프 저장
output_path = "sns_vs_depression_corr.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"✅ 그래프 저장 완료: {output_path}")
