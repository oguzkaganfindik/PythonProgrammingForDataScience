#####################################################################
# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
#####################################################################
# 1) Genel Resim
# 2) Kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3) Sayısal Değişken Analizi (Analysis of Numerical Variables)
# 4) Hedef Değişken Analizi ( Analysis of Target Variable)
# 5) Korelasyon Analizi ( Analysis of Correlation)

# 1) Genel Resim

import numpy as np
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
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

def check_df(dataframe, head=5):
    print("############ Shape ############")
    print(dataframe.shape)
    print("############ Types ############")
    print(dataframe.dtypes)
    print("############ Tail ############")
    print(dataframe.tail(head))
    print("############ NA ############")
    print(dataframe.isnull().sum())
    print("############ Quantiles ############")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

df = sns.load_dataset("flights")
check_df(df)

# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)

import numpy as np
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["embarked"].value_counts()
df["sex"].unique()
df["class"].nunique()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols] #veri setindeki sayısallara ne oldu? cat_cols'un içerisinde olmayanlar.

df["survived"].value_counts() #hangi sınıftan kaçar adet var?
100 * df["survived"].value_counts() / len(df) #sınıfların yüzdelik bilgisini yazdıralım

def cat_summary(dataframe, col_name): #fonksiyona bir dataframe adı ve ismi girdiğimizde bize bu betimlemeyi yapsın
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##############################################")

cat_summary(df, "sex")

for col in cat_cols: #cat_cols'larda gez ve hepsine tek tek az önce tanımladığımız fonksiyonu uygula
    cat_summary(df, col)

# cat_summary fonksiyonuna grafik özelliğini de ekleyelim

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##############################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)

for col in cat_cols: #şimdi grafikleştirelim
    cat_summary(df, col, plot=True)

for col in cat_cols: #bool verisi genelleştirilmemiş ise, hata vermesini önlemek için:
    if df[col].dtypes == "bool":
        print("************* bool ifadesi *************")
    else:
        cat_summary(df, col, plot=True)


df["adult_male"].astype(int)

for col in cat_cols: #bool tiplerini bulup int'e dönüştür
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)


# önemli: en baştaki yolu kabul etmemiz daha tutarlı,
# yaygın kullanım bir döngüyü dışarıda yazmaktır. böylece basit ve okunabilirliği yüksek olur.
# fakat döngüyü de fonksiyonun içine yazarsak, özellikler ve eklemeler artar ve başka riskler de oluşur
# yine de yazıp farkı görelim:
# tip sorgusunu içeride yapalım ve koşulun sağlanması/sağlanmaması durumuna göre içeride biçimlendirelim:
# görüldüğü gibi yapıyı karmaşıklaştırmaktadır.

def cat_summary(dataframe, col_name, plot=False):

    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##############################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##############################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

cat_summary(df, "adult_male", plot=True)

# özetlersek: birçok işlemde direkt hızlı bir şekilde veri setlerini analiz etme imkanı sağlayacak olan
# cat_summary fonksiyonumuz budur ve bundan sonra da bunu kullanıyor olacağız:

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##############################################")

cat_summary(df, "sex")

# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]


df[["age", "fare"]].describe().T #veri setindeki bazı değişkenleri betimsel istatistiklerine erişerek analiz edelim

# age değişkeni ve fare değişkeninin sayısal değişkenler olduğunu biliyorum.
# programatik olarak veri setinin içerisinden numeric değişkenleri nasıl seçerim?

num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

# bazı değişkenler sayısal görünümde olsa da peki ya da aslında sayısal değişken değilse?
# mesela, survived, pclass gibi değişkenler.

num_cols = [col for col in num_cols if col not in cat_cols] #num_cols'un içerisinde olup cat_cols'un içerisinde olmayanları seçelim

# her veri seti geldiğinde bu şekilde(yukarıdaki cat_cols'ların yazımı) kendimizi tekrar mı edeceğiz?
# hayır, tekrar etmeyeceğiz. bu işlemler için de bir fonksiyon yazmış olacağız
# ve fonksiyona sadece dataframe verdiğimizde işlemlerin sonucunu dönecektir.

# dikkat: ölçeklenebilirlik ve genellenebilirlik kavramlarının asıl zorluğu,
# veri yapılarını analiz edebilecek olan fonksiyonu yazmak değildir.
# asıl zorluk, bu veri yapılarını seçebilmektir.
# programatik olarak genellenebilirlik kaygılarıyla seçebilmektir.
# kategorik ve numerik değişkenleri, sistematik bir şekilde seçebilmektir.

# numeric sütunlar için basit bir analiz foksiyonu -yazalım:

def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df, "age")

# daha fazla sayıda değişken olsaydı?

for col in num_cols: # age ve fare değişkenlerini başarılı bir şekilde ayrı ayrı ekrana yazdırdık.
    num_summary(df, col)

# grafik özellik eklemek isteseydik?

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

num_summary(df, "age", plot=True)

# Daha fazla değişkeni grafikleştirmek istersek:

for col in num_cols: # böylece diğer değişkenleri de grafikleştirdik
    num_summary(df, col, plot=True)


###########################################################
# Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi
# Bu bölümde değişkenlerin otomatik olarak yakalanması ve işlemlerin genelleştirilmesi incelenecek
# En kritik olan bölümlerden birisidir
# Bu bölümde bir fonksiyon tanımlayacağız ve aynı zamanda docstring kavramına dokunup,
# Bir fonksiyon tanımlanırken, bu fonksiyonun diğer kullanıcılar tarafından kullanılırken,
# Hangi bilgileri barındırması gerektiği konusu ele alınacaktır.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.info()

# veri seti içerisindeki kategorik değişkenleri ve numerik değişkenleri ayrı ayrı getirelim
# Ek olarak, kategorik ama kardinal değişken listesini de getirelim.
# Numerik görünümlü kategoriklerle ilgilenmiyoruz çünkü onları zaten cat_cols'un içerisine atmıştık.

# Bir değişken sayısal olsa dahi, eğer eşsiz değer sayısı 10'dan küçükse, bu bir kategorik değişkendir diyeceğiz
# Bir kategorik değişkenin eşsiz değer sayısı 20'den büyükse, buna bir kardinal değişken diyeceğiz

# Konumuz docstring. Bir fonksiyona argüman yazma konusudur
# Fonksiyonların ne görev yaptığı? Fonksiyonların nasıl kullanılabileceği?

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    -----
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_car cat_cols'un içerisinde.
    """

    # help(grab_col_names)

    # Kategorik değişken listesini oluşturacak olan bölümümüz
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # Numerik değişkenleri oluşturacak olan bölüm
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    # Raporlama bölümleri ekliyoruz

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df) # raporu alıyoruz

# bütün öğrendiklerimizi toparlayalım:

def cat_summary(dataframe, col_name): #fonksiyona bir dataframe adı ve ismi girdiğimizde bize bu betimlemeyi yapsın
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##############################################")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

for col in num_cols:
    num_summary(df, col, plot=True)

# bonus: cat_summary fonksiyonunu da plot özelliği ile biçimlendirileceği şekilde rahatça kullanılabileceği
# bir yol ele almak istersek:
# veri seti içerisindeki bool tipteki değişkenleri bulup, bunları interger'a çevirmek ve daha sonra cat_summary
# fonksiyonunu görsel özellikli olarak daha kolay şekilde kullanmaya çalışmak
df = sns.load_dataset("titanic")
df.info()
for col in df.columns: #programatik şekilde belirli bir veri yapısını, istediğimiz veri yapısına çevirdik
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##############################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

for col in cat_cols: # bütün değişkenleri grafikleştirdik
    cat_summary(df, col, plot=True)

for col in num_cols: #işlemleri tamamladık
    num_summary(df, col, plot=True)

########################################################
# 4. Hedef Değişken Analizi (Analysis of Target Veriable)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")

for col in df.columns: #programatik şekilde belirli bir veri yapısını, istediğimiz veri yapısına çevirdik
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kardinal değişken listesi

    Notes
    -----
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_car cat_cols'un içerisinde.
    """

    # help(grab_col_names)

    # Kategorik değişken listesini oluşturacak olan bölümümüz
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # Numerik değişkenleri oluşturacak olan bölüm
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    # Raporlama bölümleri ekliyoruz

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)

# elimizdeki hedef değişkeni(survived değişkeni şu an bizim için hedef değişken)
# kategorik değişkenler ve sayısal değişkenler açısından analiz etmeliyiz.
# uğraştığımız problemlerin bir çoğunda ana odaklandığımız bir değişken vardır.
# örneğin,bir müşteri terk probleminde churn değişkeni, müşterinin bizi terk edip etmediğini gösteren değişken,
# örneğin, bir kredi risk tahmini projesinde müşterilerin ödemelerini geciktirip geciktirmediğini ifade eden değişken,
# örneğin, ev fiyat tahmini, araç fiyat tahmini probleminde, evlerin ya da araçların fiyatlarını ifade eden price değişkeni,
# gibi değişkenler odaklandığımız projelerde yüksek ihtimalle hedef değişkenlerimiz olacaktır
# ve birçok senaryoda zaten üzerinde çalışıyor olduğumuz veri setindeki, problemi ve odaklandığımız ana değişkeni biliyor oluruz.
# Dolayısıyla, "hedef değişkeni nereden anlayacağız veri setinden?" gibi bir soru çok geçerli olmayabilir. Zaten biliyor oluruz.

# Bu veri setindeki hedef değişkenimiz survived değişkenidir. Bu değişkeni analiz etmek istiyoruz.

df.head()

df["survived"].value_counts()
cat_summary(df, "survived")

# titanic veri setini incelersek, insanların hayatta kalma durumunu etkileyen şey nedir?
# bunu anlamanın yolu, değişkenleri çaprazlamaktır.
# yani bağımlı değişkene göre, diğer değişkenleri göz önünde bulundurarak analizler yapmalıyız.

## Hedef Değişkenin Kategorik Değişkenler İle Analizi ##

df.groupby("sex")["survived"].mean() # cinsiyete göre groupby'a alıp survived'in ortalamasına bakıyoruz

# female    0.742038
# male      0.188908

# kadınlar yüzde 74, erkekler yüzde 18 hayatta kalmıştır.
# kadın olmak, hayatta kalmayı direkt etkileyen bir faktör olabilir.
# iki değişkeni bir arada değerlendirdik.

# Bu işlemi bir fonksiyon ile tanımlayacak olursak:

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col, observed=False)[target].mean()}))

target_summary_with_cat(df, "survived", "sex")

for col in cat_cols: # bütün kategorik değişkenleri gezerek hedef değişkeni analiz et
    target_summary_with_cat(df, "survived", col)


##################################################
# Hedef Değişkenin Sayısal Değişkenler İle Analizi #

df.groupby("survived")["age"].mean() # groupby'a bağımlı değişkeni, Aggregation bölümüne ise sayısal değişkeni getiririz.

# Hayatta kalanların yaş ortalaması 28, hayatta kalamayanların yaş ortalaması 30 bulunur.

# 0    30.626179
# 1    28.343690
# --------------

df.groupby("survived").agg({"age":"mean"}) # yukarıdakinden farklı olarak, bu kullanım da tercih edilebilir

def target_summary_with_cat(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")

target_summary_with_cat(df, "survived", "age")

for col in num_cols:
    target_summary_with_cat(df, "survived", col)

############################################################
# 5. Korelasyon Analizi (Analysis of Correlation)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/data.csv")
df = df.iloc[:, 1:-1] # id değişkeni ile en sondaki değişkeni istemediğimizden dolayı bunu kullandık
df.head()

# Amacımız bu veri setinde, ısı haritası aracılığı ile korelasyonlarına bakmak.
# Daha sonra yüksek korelasyonlu bir değişken setindeki, yüksek korelasyonlu değişkenlerden bazılarını dışarı bırakabilmektir.
# Dikkat: burada görülecek olan, yüksek korelasyonlu değişkenlerden birini silme konusu, her çalışmada gerekli olmayabilir.
# Sadece ihtiyacımız olduğunda yüksek korelasyonlu değişkenleri nasıl yakalarız? sorusuna yanıt arayacağız.

# Korelasyon: Değişkenlerin birbiriyle ilişkisini ifade eden bir istatistiksel ölçümdür
# -1 ile +1 arasında değerler alır. -1'e ya da +1'e yaklaştıkça ilişkinin şiddeti kuvvetlenir.
# Eğer 2 değişkenin arasındaki ilişki pozitif ise buna pozitif korelasyon denir ve bir değişkenin değeri arttıkça, diğerinin de değeri artar.
# 2 Değişken arasındaki ilişki negatifse, bir değişkenin değeri artarken, diğer değişkenin değeri azalır.
# Bu korelasyonlarda ifade edildiği üzere, 1'e yaklaştıkça ilişki kuvvetli, -1'e yaklaştıkça da ilişki şiddeti kuvvetlidir.
# -1 Negatif yönlü, +1 pozitif yönlüdür.
# 1'e ne kadar yakınsa, ilişki o kadar şiddetlidir.
# Dolayısıyla 0 civarındaki bir korelasyon değeri, korelasyon olmadığı anlamına gelir.
# Örneğin, 0 ile 0.50 arasında düşük korelasyon ya da benzer olarak 0 ile -0.50 arasında korelasyonlar düşük korelasyonlardır.
# 0.50 üzerine çıkıldıkça da korelasyonun şiddeti artmaktadır. Bu durum, daha şiddetli bir şekilde birlikte hareket edildiğini ifade eder.
# Genelde analitik çalışmalarda birbiriyle yüksek korelasyonlu olan değişkenlerin çalışmalarda bulunmamasını isteriz.
# Çünkü ikisi de zaten aynı şeyi ifade ediyor.
# Yani, örneğin, iki değişkenin yüzde 99 korelasyona sahip olması, bu iki değişkenin neredeyse aynı değişkenler olduğu anlamına gelir.
# Bu sebeple birçok çalışmada, bu değişkenlerden birisini çalışmanın dışında bırakmak isteriz.

num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]] # Numerik değişkenleri seçecek list comprehendsion yapısı

# önce bir ısı haritası oluşturacağız ve daha sonra da birbiriyle yüksek korelasyonlu olanları elemeye çalışacağız

corr = df[num_cols].corr() # bütün değişkenlerin birbirleriyle olan korelasyonları

# ısı haritası oluşturalım:

sns.set(rc={'figure.figsize':(12, 12)}) # Bu grafik 12-12 olsun
sns.heatmap(corr, cmap="RdBu")
plt.show(block=True)

# Yüksek Korelasyonlu Değişkenlerin Silinmesi #

# Korelasyonun negatif ya da pozitif olması ile ilgilenmiyoruz. Bundan dolayı hepsini mutlak değer fonksiyondan geçiriyoruz.
# Bizim için negatif ya da pozitif yönlü korelasyon aynı anlama gelmektedir.
# Bu durumun bir diğer sebebi, yazacak olduğumuz fonksiyonlarda daha kolay bir şekilde işlem yapmak istememiz.
cor_matrix = df.corr(numeric_only=True).abs()

# 1'lerden oluşan ve oluşturmuş olduğumuz matris'in boyutunda bir numpy array oluşturuyoruz.
# bu numpy array'i bool'a çeviriyoruz.
# daha sonra corr = df[num_cols].corr() ile gelen yapıya çevirmek için numpy'daki ilgili fonksiyonu kullanıyoruz.
# böylece çoklama, birbirini tekrar etme durumundan kurtulmuş olduk.
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))

# Değerlerden herhangi birisi 0.90'dan büyükse seçiyoruz.
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>0.90)]

cor_matrix[drop_list]
df.drop(drop_list, axis=1) #0.90'dan büyük olanları veri setinden siliyoruz

# şimdi öyleyse bu işlemi, her ihtiyacımız olduğunda çağırıp kullanabileceğimiz bir formatta fonksiyonlaştıralım:

def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr(numeric_only=True)
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]> corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show(block=True)
    return drop_list

high_correlated_cols(df)



### yaptığımız işlemin geçerliliğini doğrulayalım:

drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True) # veri setindeki yüksek korelasyonlu değişkenler çıkartıldı