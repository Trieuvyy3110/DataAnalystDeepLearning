import pandas as pd 
dh=pd.read_csv(r'C:\Users\Admin\Downloads\[HOCSAU]\dulieuxettuyendaihoc.csv') 
print(dh.head(10)) 
print(dh.tail(10))
#câu4
print(dh['DT'].isna().sum()) 
dh['DT'].fillna(0,inplace=True) 
#câu5
dh['T1'].fillna(dh['T1'].mean(),inplace=False)
#câu 6

def fill(col):
       return dh[col].fillna(dh[col].mean(),inplace=False)  


#câu 7
print(dh.dtypes) 
dh.dtypes==float 

dh['TBM1']=(dh['T1']*2 + dh['L1'] + dh['H1'] + dh['S1'] + dh['V1']*2 + dh['X1'] +dh['D1'] + dh['N1'])/10
dh['TBM2']=(dh['T2']*2 + dh['L2'] + dh['H2'] + dh['S2'] + dh['V2']*2 + dh['X2'] +dh['D2'] + dh['N2'])/10
dh['TBM3']=(dh['T6']*2 + dh['L6'] + dh['H6'] + dh['S6'] + dh['V6']*2 + dh['X6'] +dh['D6'] + dh['N6'])/10
 
print(dh.isnull().values.any()) 
#câu 8
for i in ["1","2","3"]:
       dh.loc[dh['TBM'+i]<= 5 ,'XL'+i]='Y'
       dh.loc[(5<dh['TBM'+i])& (dh['TBM'+i]<= 6.5) ,'XL'+i]='TB'
       dh.loc[(6.5<dh['TBM'+i]) & (dh['TBM'+i]<= 8) ,'XL'+i]='K'
       dh.loc[(8<dh['TBM'+i]) & (dh['TBM'+i]<= 9) ,'XL'+i]='G'
       dh.loc[9<dh['TBM'+i],'XL'+i]='XS'

#Câu 9
for i in ["1","2","3"]:
       dh['US_TBM'+i]=dh['TBM'+i]/10*4
print(dh.head())
#Câu 10
for i in dh['KT'].unique():
       dh.loc[(i=='A'or i=='A1')&(((dh['DH1']*2+dh['DH2']+dh['DH3'])/4)>=5),'KQXT']=1
       dh.loc[(i=='A'or i=='A1')&(((dh['DH1']*2+dh['DH2']+dh['DH3'])/4)<5),'KQXT']=0
       dh.loc[(i=='B')&(((dh['DH1']*2+dh['DH2']+dh['DH3'])/4)>=5),'KQXT']=1
       dh.loc[(i=='B')&(((dh['DH1']*2+dh['DH2']+dh['DH3'])/4)<5),'KQXT']=0
       dh.loc[(i!='A'or i!='A1'or i!='B')&(((dh['DH1']*2+dh['DH2']+dh['DH3'])/4)>=5),'KQXT']=1
       dh.loc[(i!='A'or i!='A1'or i!='B')&(((dh['DH1']*2+dh['DH2']+dh['DH3'])/4)<5),'KQXT']=0
 
dh.to_csv(r'C:\Users\Admin\Downloads\[HOCSAU]\processed_dulieuxettuyendaihoc.csv')
#Câu lệnh cuối cùng là dùng để chuyển các dữ liệu đã được thao tác sang file processed_dulieuxettuyendaihoc.csv

