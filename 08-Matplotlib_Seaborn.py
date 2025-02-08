#############################################
# VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN #
#############################################

# MATPLOTLIB

# Kategorik değişken: Sütun grafik => countplot bar
# Sayısal değişken: Histogram ve kutu grafik => hist, boxplot

# Kategorik Değişken Görselleştirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind='bar')
plt.show(block=True)

# Sayısal Değişken Görselleştirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show(block=True)

plt.boxplot(df["fare"])
plt.show(block=True)

# Matplotlib'in Özellikleri

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# plot

x = np.array([1, 8])
y = np.array([0, 150])

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y, 'o')
plt.show(block=True)

# marker

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')
plt.show(block=True)

plt.plot(y, marker='*')
plt.show(block=True)

markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'H', 'h']

# line

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed")
# plt.plot(y, linestyle="dashed", color='r')
# plt.plot(y, linestyle="dotted")
# plt.plot(y, linestyle="dashdot")
plt.show(block=True)

# Multiple Lines

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show(block=True)

# Labels

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
# plt.show(block=True)
# Başlık
plt.title("Bu ana başlık")

# X eksenini isimlendirme
plt.xlabel("X ekseni isimlendirmesi")
# Y eksenini isimlendirme
plt.ylabel("Y ekseni isimlendirmesi")

# grid ekleme
plt.grid()

plt.show(block=True)

# Subplots

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)


# plot 2
x = np.array([8, 8, 9, 9, 10, 10, 11, 11, 12, 12])
y = np.array([24, 25, 26, 27, 28, 29, 30, 31, 32, 33])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([4, 5, 8, 12, 15, 17, 18, 19, 21, 23])
y = np.array([27, 29, 30, 32, 34, 38, 42, 44, 45, 46])
plt.subplot(1, 3, 3)
plt.title("2")
plt.plot(x, y)

plt.show(block=True)

# SEABORN #

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show(block=True)

# Matplotlib ise:
df['sex'].value_counts().plot(kind='bar')
plt.show(block=True)

# Sayısal Değişken Görselleştirme

sns.boxplot(x=df["total_bill"])
plt.show(block=True)

df["total_bill"].hist()
plt.show(block=True)