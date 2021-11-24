import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
from scipy import stats
import statsmodels.formula.api as smf

df = pd.read_csv(r'C:\Users\Admin\Downloads\[HOCSAU]\exc\crabs.txt',sep = '\s+')
print(df)
plt.plot(df['postsz'],df['presz'],'o')
plt.xlabel('Postmlit size')
plt.ylabel('Premolt size')
plt.title('Postmolt vs Premost')
plt.show()
print('He so tuong quan la:')
print(pearsonr(df['postsz'],df['presz']))
#tìm phương trình dự báo
result = smf.ols('presz~postsz',df).fit()
print(result.summary())
#Phương trình hồi quy là
#premolt = -25.2137 + 1.0732*postmolt


sales_pred = result.predict()
plt.plot(df['postsz'],df['presz'],'o')
plt.plot(df['postsz'],sales_pred,'r',linewidth=2)
plt.xlabel('Postmlit size')
plt.ylabel('Premolt size')
plt.ylabel('Postmost')
plt.show()
