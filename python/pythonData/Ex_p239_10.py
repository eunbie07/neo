import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'mpg.csv'
myframe = pd.read_csv(filename, encoding='utf-8')
print(myframe['drv'].unique())
print('-' * 50)


frme01 = myframe.loc[myframe['drv'] == 'f', 'hwy']
frme01.index.name = '전륜 구동'
print(frme01.head())
print('-' * 50)

frme02 = myframe.loc[myframe['drv'] == '4', 'hwy']
frme02.index.name = '4륜 구동'
print(frme02.head())
print('-' * 50)

frme03 = myframe.loc[myframe['drv'] == 'r', 'hwy']
frme03.index.name = '후륜 구동'
print(frme03.head())
print('-' * 50)

totalframe = pd.concat([frme01, frme02, frme03], axis=1, ignore_index=True)
totalframe.columns = ['f', '4', 'r']
print(totalframe.head())
print('-' * 50)

totalframe.plot(kind='box')
plt.xlabel('구동 방식')
plt.ylabel('주행 마일 수')
plt.grid(False)
plt.title('고속도로 주행 마일 수의 상자 수염')

filename = 'Ex_p239_10.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' saved')
plt.show()
