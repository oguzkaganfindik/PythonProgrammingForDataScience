# PANDAS
# Veri manipülasyonu ya da veri analizi dendiğinde akla gelen ilk Python kütüphanelerinden biridir.
# Öncelikle Ekonometrik ve Finansal çalışmalar için doğmuş, daha sonra veri analitiği dendiğinde en sık kullanılan kütüphane haline gelmiştir.
# Veri analitiği genel başlığı altında, makine öğrenmesinden veri bilimine, veri analizinden derin öğrenmeye,
# Veri varsa ve Python varsa, mutlaka bir şekilde kullanacağımız kütüphanelerden birisidir.

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

# Pandas Series: Tek boyutlu ve index bilgisi barındıran veri tipi
# Pandas DataFrame: Çok boyutlu ve index bilgisi barındıran veri tipi

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(3)

# Veri Okuma (Reading Data)

import pandas as pd
df = pd.read_csv("datasets/Advertising.csv")
df.head()
# pandas cheatsheet

# Veriye Hızlı Bakış (Quick Look at Data)

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["alone"].head()
df["alone"].value_counts()

# Pandas'ta Seçim işlemleri (Selection in Pandas)

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0, axis=0).head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# df = df.drop(delete_indexes, axis=0) # işlemi kalıcı hale getirme
# df.drop(delete_indexes, axis=0, inplace=True) # işlemi kalıcı hale getirme

# Değişkeni Indexe Çevirmek

df["age"].head()
df.age.head()

df.index = df["age"]
df.drop("age", axis=1).head()
df.drop("age", axis=1, inplace=True)
df.head()

# Indexi Değişkene Çevirmek

df.index

df["age"] = df.index
df.head()
df.drop("age", axis=1, inplace=True)

df.reset_index().head()
df = df.reset_index()
df.head()

# Değişkenler Üzerinde İşlemler

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head()) #type: Series

type(df[["age"]].head()) #type: DataFrame

df[["age", "alive"]] # birden fazla değişken seçmek

col_names = ["age", "adult_male", "alive"]
df[col_names]

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head() # ~ Dışındakileri seçer

# iloc(index bilgisi vererek seçim yapma) & loc(indexlerdeki label'lara göre seçim yapar)
# DataFrame'lerde seçim işlemi için kullanılan özel yapılardır

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection
df.iloc[0:3]
df.iloc[0, 0]

# loc: label based selection

df.loc[0:3]

# Ben satırlarda 0'dan 3'e kadar gitmek istiyorum fakat sütunlardan da bir değişken seçmek istiyorum.
df.loc[0:3]

df.iloc[0:3, 0:3]
df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

# Koşullu Seçim (Conditional Selection)

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, ["age", "class"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head() #Birden fazla olan koşullar parantez içerisine alınır

df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()

# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# count()
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum
# pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean","sum"]})

df.groupby("sex").agg({"age": ["mean","sum"],"survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],"survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],"survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],"survived": "mean", "sex": "count"})


# Pivot Table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", ["embarked", "class"], observed=False)

df.head()

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", ["new_age", "class"], observed=False)

pd.set_option('display.width', 500) # Çıktının gösterim miktarını ifade eder

# Apply ve Lambda

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

(df["age"] / 10).head()
(df["age2"] / 10).head()
(df["age3"] / 10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

df[["age", "age2", "age3"]].apply(lambda x: x / 10).head() # apply ve lambda kullanarak yapalım

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head() # programatik hale getirelim

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head() # uygulandığı DataFrame'deki değerleri standartlaştıralım

# dışarıda def ile tanımlanmış bir fonksiyonu da kullanabiliriz:

def standart_scaler(col_name):
    return  (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()

# anlaşılıyor olacak ki, apply ile beraber sadece lambda'yı değil, diğer klasik fonksiyonları da kullanabiliriz.
# apply fonksiyonu bize satırlarda ya da sütunlarda elimizdeki belirli bir fonksiyonu bu satır ya da sütunlara uygulama imkanı sağlar.

# Birleştirme (Join) İşlemleri

import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var2"])
df2 = df1 + 99

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

# Merge İle Birleştirme İşlemleri

df1 = pd.DataFrame({'employees': ['John', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)