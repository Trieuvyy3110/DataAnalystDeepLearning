import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.graphics.gofplots import qqlineqplot as qqplot

#loat dữ liệu lên, tên file babies.txt
data = pd.read_csv(r"‪C:\Users\Admin\Downloads\[HOCSAU]\exc\babies.txt",sep="\s+")
print(data)

df_cohutthuoc=data[data['smoke']==1]

df_khonghutthuoc=data[data['smoke']==0]

data.boxplot(by='smoke',cloumn=['bwt'])

#in các giá trị thống kê
df_cohutthuoc.describe()
#Fish: phân phối chuẩn có Furtosis = 0
#Hàm trong Pandas tính Kurtosis theo Fisher
#Kurtosis(Fisher) = kurtosis(Peason)-3
#Tính Kurtosis theo Peason = Kurtosis của Fisher +3
print('Kurtosis la: ',df_cohutthuoc['bwt'].kurtosis()+3)
print('Skew la:',df_cohutthuoc['bwt'].skew())
print('Min la:',df_cohutthuoc['bwt'].min())
print('Max la:',df_cohutthuoc['bwt'].max())
print('Mean la:',df_cohutthuoc['bwt'].mean())
print('std la:',df_cohutthuoc['bwt'].std(skipna=True))
print('var la:',df_cohutthuoc['bwt'].var(skipna==True))
print('Q0%',df_cohutthuoc['bwt'].quantile(.0))
print('Q25%',df_cohutthuoc['bwt'].quantile(.25))
print('Q50%',df_cohutthuoc['bwt'].quantile(.50))
print('Q75%',df_cohutthuoc['bwt'].quantile(.75))
#IQR=Q3=Q1(Q75%-Q25%)
df_cohutthuoc.hist(column='bwt',bins=12)

df_khonghutthuoc.hist(column='bwt',bins=6)

#cách dùng thư viện matplotlib
plt.hist(df_cohutthuoc['bwt'],bins=12)
plt.show()

qqplot(df_cohutthuoc['bwt'],line='s')

qqplot(df_khonghutthuoc['bwt'],line='s') 
