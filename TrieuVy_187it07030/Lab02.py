
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.reshape.reshape import stack

df=pd.read_csv('D:\hocsau\processed_dulieuxettuyendaihoc.csv')

#1.Hãy sắp xếp dữ liệu điểm DH1 theo thứ tự tăng dần
df_sapxep_DH1=df.sort_values(by='DH1')
#print(df_sapxep_DH1[['T1','DH1']])

#2.Hãy sắp xếp dữ liệu điểm DH2 tăng dần theo nhóm giới tính
df_nam=df[df['GT']=='M']
df_sapxep_nam_DH2=df.sort_values(by='DH2')

df_nu=df[df['GT']=='F']
df_sapxep_nu_DH2=df.sort_values(by='DH2')
#print(df_sapxep_nam_DH2[['GT','DH2']])

#3.Hãy tạo pivot-table để thống kê 
# các giá trị count, sum, mean, median, min, max, sdt, Q1, Q2 và Q3 của DH1 theo KT
df_group_DH1A=df.groupby('KT')['DH1'].agg(['count',np.sum,np.mean,np.median,np.min,np.max,np.std,lambda x: x.quantile(0.25), lambda x: x.quantile(0.5), lambda x: x.quantile(0.75) ])
df_KT=df_group_DH1A.rename(columns={'<lambda_0>':'Q1','<lambda_1>':'Q2','<lambda_2>':'Q3'})
#print(pd.pivot_table(df_group_DH1A,columns='KT'))
print(df_KT)
#4.Hãy tạo pivot-table để 
# thống kê các giá trị count, sum, mean, median, min, max, sdt, Q1, Q2 và Q3 của DH1 theo KT và KV
df_group_DH1B=df.groupby(['KT','KV'])['DH1'].agg(['count',np.sum,np.mean,np.median,np.min,np.max,np.std,lambda x: x.quantile(0.25), lambda x: x.quantile(0.5), lambda x: x.quantile(0.75)])
#print(pd.pivot_table(df_group_DH1B,columns=('KT','KV')))
df_KT_KV=df_group_DH1B.rename(columns={'<lambda_0>':'Q1','<lambda_1>':'Q2','<lambda_2>':'Q3'})
print(df_KT_KV)
#5.Hãy tạo pivot-table để thống kê các 
# giá trị count, sum, mean, median, min, max, sdt, Q1, Q2 và Q3 của DH1 theo KT, KV và DT
df_group_DH1C=df.groupby(['KT','KV','DT'])['DH1'].agg(['count',np.sum,np.mean,np.median,np.min,np.max,np.std,lambda x: x.quantile(0.25), lambda x: x.quantile(0.5), lambda x: x.quantile(0.75)])
#print(pd.pivot_table(df_group_DH1C,columns=('KT','KV','DT')))
df_KT_KV_DT=df_group_DH1C.rename(columns={'<lambda_0>':'Q1','<lambda_1>':'Q2','<lambda_2>':'Q3'})
print(df_KT_KV)
#Phần 2
#1.Hãy trình bày dữ liệu biến: GT
df_theo_GT=df.groupby('GT')['GT'].agg(['count'])
df_nam_nu_bang=pd.pivot_table(df_theo_GT,columns='GT')
print(pd.pivot_table(df_theo_GT,columns='GT'))
df_nam_nu_bang.plot.bar(stacked=True)
df_nam_nu_bang.plot.bar()
df_theo_GT.plot.pie(y='count')
#print(plt.show())
#3. Hãy trình bày dữ liệu biến DT với các học sinh là nam
df_nam=df[df['GT']=='M']
df_nam_theo_DT=df_nam.groupby('DT')['DT'].agg(['count'])
df_nam_theo_DT.plot.bar()
df_nam_DT_bang=pd.pivot_table(df_nam_theo_DT,values='count',columns='DT')
df_nam_DT_bang.plot.bar()

df_nam_DT_bang.plot.pie(subplots=True)
#print(plt.show())
df_nu=df[df['GT']=='F']
df_nu_theo_DT=df_nu.groupby('DT')['DT'].agg(['count'])

#4. Hãy trình bày dữ liệu biến KV với các học sinh là nam thuộc dân tộc Kinh, có điểm thỏa 
#mãn điều kiện (DH1 >= 5.0 và DH2 >= 4.0 và DH3 >= 4.0


df_nam_DTK_diem=df[(df['DH1']>=5.0)&(df['DH2']>=4.0)&(df['DH3']>=4.0)&(df['GT']=='M')&(df['DT']==0)]
df_nam_theo_KV=df_nam_DTK_diem.groupby('DT')['DT'].agg(['count'])
df_nam_theo_KV.plot.bar()

#print(plt.show())
#5. Hãy trình bày dữ liệu lần lượt các biến DH1, DH2, DH3 lớn hơn bằng 5.0 và thuộc khu 
#vực 2NT
df_DH1=df[(df['DH1']>=5.0)&(df['KV']=='2NT')].groupby('KV')['KV'].agg(['count'])
df_DH1.plot.bar()

df_DH2=df[(df['DH2']>=5.0)&(df['KV']=='2NT')].groupby('KV')['KV'].agg(['count'])
df_DH2.plot.bar()

df_DH3=df[(df['DH3']>=5.0)&(df['KV']=='2NT')].groupby('KV')['KV'].agg(['count'])
df_DH3.plot.bar()

#print(plt.show())

#Phần 3
#1. Trực quan dữ liệu học sinh nữ trên các nhóm XL1, XL2, XL3 dạng unstacked
df_nu_theo_XL1=df_nu.groupby(['XL1'])['XL1'].agg(['count'])
df_nu_theo_XL2=df_nu.groupby(['XL2'])['XL2'].agg(['count'])
df_nu_theo_XL3=df_nu.groupby(['XL3'])['XL3'].agg(['count'])

print(df_nu_theo_XL3)

Y_XL1=int(df_nu_theo_XL1.loc['Y',:])
TB_XL1=int(df_nu_theo_XL1.loc['TB',:])
K_XL1=int(df_nu_theo_XL1.loc['K',:])
G_XL1=int(df_nu_theo_XL1.loc['G',:])
#XS_XL1=int(df_nu_theo_XL1.loc['XS',:])
XS_XL1=0

#XL1_nu=[Y_XL1,TB_XL1,K_XL1,G_XL1,XS_XL1]
Y_XL2=int(df_nu_theo_XL2.loc['Y',:])
TB_XL2=int(df_nu_theo_XL2.loc['TB',:])
K_XL2=int(df_nu_theo_XL2.loc['K',:])
G_XL2=int(df_nu_theo_XL2.loc['G',:])
XS_XL2=0

Y_XL3=0
TB_XL3=int(df_nu_theo_XL3.loc['TB',:])
K_XL3=int(df_nu_theo_XL3.loc['K',:])
G_XL3=int(df_nu_theo_XL3.loc['G',:])
XS_XL3=0

Y=[Y_XL1,Y_XL2,Y_XL3]
TB=[TB_XL1,TB_XL2,TB_XL3]
K=[K_XL1,K_XL2,K_XL3]
G=[G_XL1,G_XL2,G_XL3]
XS=[XS_XL1,XS_XL2,XS_XL3]

index=['XL1','XL2','XL3']
df_xl_nu=pd.DataFrame({'Y':Y,'TB':TB,'K':K,'G':G,'XS':XS},index=index)
df_xl_nu.plot.bar()
df_xl_nu.plot.bar(stacked=True)
df_nu_theo_XL1.plot.pie(y='count')
df_nu_theo_XL2.plot.pie(y='count')
df_nu_theo_XL3.plot.pie(y='count')
#print(plt.show())

#2. Trực quan dữ liệu KQXT trên nhóm học sinh có khối thi A, A1, B thuộc khu vực 1, 2
#df_kqxt=df[(df['KT']==(['A','B','A1']))&(df['KV']==(['1','2']))].groupby(['KV','KT','KQXT'])['KQXT'].agg(['count'])
df_kqxt=df.loc[df.KV.isin(['1','2'])&df.KT.isin(['A','B','A1'])].groupby(['KT','KV','KQXT'])['KQXT'].agg(['count']).plot.bar()

#3. Trực quan dữ liệu số lượng thí sinh từng khu vực dựa trên từng nhóm khối thi
df_slts=df.groupby(['KT','KV'])['KT'].agg(['count']).plot.bar()

#4. Trực quan dữ liệu số lượng thí sinh đậu, rớt trên từng nhóm khối thi
df_slts4=df.groupby(['KQXT','KT'])['KT'].agg(['count']).plot.bar(stacked=True)

#5. Trực quan dữ liệu số lượng thí sinh đậu rớt trên từng nhóm khu vực.
df_slts5=df.groupby(['KQXT','KV'])['KV'].agg(['count']).plot.bar(stacked=True)

#6. Trực quan dữ liệu số lượng thí sinh đậu rớt dựa trên từng nhóm dân tộc
df_slts6=df.groupby(['KQXT','DT'])['DT'].agg(['count']).plot.bar(stacked=True)

#7. Trực quan dữ liệu số lượng thí sinh đậu rớt dựa trên từng nhóm giới tính.
df_slts7=df.groupby(['GT','KQXT'])['GT'].agg(['count']).plot.bar(stacked=True)


#Phần 4
#1. Vẽ biểu đồ đường Simple cho biến T1
df_T1=df.groupby('T1')['T1'].agg(['count']).plot()

#2.Hãy tạo biến phân loại (phanlopt1) cho môn toán (T1) như sau:
df.loc[(df['T1']<5),'phanlopt1']='Kém'
df.loc[(df['T1']>=5)&(df['T1']<7),'phanlopt1']='Trungbinh'
df.loc[(df['T1']>=7)&(df['T1']<8),'phanlopt1']='Khá'
df.loc[(df['T1']>8),'phanlopt1']='Gioi'

#3 Lập bảng tần số cho biến phanloait1
dfphanlopt1=df.groupby(['T1','phanlopt1'])[['T1','phanlopt1']].agg(['count'])

#4. Vẽ biểu đồ đường Multiple Line cho biến T1 được phân loại bởi biến phanlopt1
unstackphanlopt1=dfphanlopt1.unstack()
unstackphanlopt1['phanlopt1'].plot(ylabel='Count')

#5. Vẽ biểu đồ Drop-line cho biến T1 được phân loại bởi biến phanlopt1
unstackphanlopt1.plot.bar()
print(plt.show())



