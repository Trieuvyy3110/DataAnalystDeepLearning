import pandas as pd
colum_names = ["Id", "Name","Age","Weight","m0006","m0612","m1218","f0006","f0612","f1218"]
df = pd.read_csv(r"C:\Users\Admin\Downloads\[HOCSAU]\exc\patient_heart_rate.csv", names = colum_names)
print(df.head())


df[['Firstname','Lastname']] = df['Name'].str.split(expand = True)
df = df.drop('Name',axis = 1)
print(df)


weight = df['Weight']

for i in range (0,len(weight)):
    x = str(weight[i])
    if "lbs" in x[-3:]:
        x = x[:-3:]
        float_x = float(x)
        y = int(float_x/2.2)
        y = str(y)+"kgs"
        weight[i] = y
print(df)

df.dropna(how = "all",inplace = True)
print(df)


df = df.drop_duplicates(subset = ['Firstname','Lastname','Age','Weight'])
print(df)

df.Firstname.replace({r'[^\x00-\x7F]+':''},regex =True , inplace = True)
df.Lastname.replace({r'[^\x00-\x7F]+':''},regex =True , inplace = True)
print(df)



