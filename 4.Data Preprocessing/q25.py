'''#25. Perform pre-processing of Play Tennis dataset (handle missing values, encoding, 
normalization, train-test split). '''

from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd

df=pd.read_csv("Mall.csv")
print(df.head())

imputer=SimpleImputer(strategy="most_frequent")
df=pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

le=LabelEncoder()
cat_col=df.select_dtypes(include="object").columns

for col in cat_col:
    df[col]=le.fit_transform(df[col])

scaler=MinMaxScaler()
num_col=df.select_dtypes(include=['number']).columns

for num in num_col:
    df[num]=scaler.fit_transform(df[[num]])


print(df)
x=df[['Age','Annual Income (k$)']]
y=df['Spending Score (1-100)']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print("training data",x_train.shape)
print("testing data",x_test.shape)
