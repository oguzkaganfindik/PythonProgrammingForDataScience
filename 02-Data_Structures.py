# Veri Yapıları (Data Structures)

# Veri Yapılarına Giriş ve Hızlı Özet

# Sayılar: integer

x = 46
type(x)

# Sayılar: float

x = 10.3
type(x)

# Sayılar: complex

x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False

type(True)

5 == 4
3 == 2
1 == 1
type(3==2)

# Liste

x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

# Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.

# Sayılar (Numbers): int, float, complex

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2

# Tipleri Değiştirmek

int(b)
float(a)

c = a * b / 10
int(c)

# Karakter Dizileri (Strings)

print("John")
print('John')

"John"
name = "John"

# Çok Satırlı Karakter Dizileri

"""Veri Yapıları"""

# Karakter Dizilerinin Elemanlarına Erişmek

name
name[0]
name[3]

# Karakter Dizilerinde Slice İşlemi

name[0:2]

# String İçerisinde Karakter Sorgulamak

long_str = "Veri Yapıları: Hızlı Özet"
"veri" in long_str

"Veri" in long_str

# String (Karakter Dizisi) Metodları

dir(int)

# len

name = "john"
type(name)
type(len)

len(name)
len("oğuzkağan")

## Bir fonksiyon Class yapısı içerisinde tanımlandıysa buna method denir. Class yapısı içerisinde değilse fonksiyondur.

# upper() & lower(): küçük-büyük dönüşümleri

"miuul".upper()
"MIUUL".lower()

# type(upper())
# type(upper)

# replace: karakter değiştirir

hi = "Hello AI Era"
hi.replace("l", "p")

# split: böler

"Hello AI Era".split()

# strip: kırpar
" ofofo ".split()
"ofofo".split("o")

# capitalize: ilk harfi büyütür

"foo".capitalize()

"foo".startswith("f")

# Liste (List)

# Değiştirilebilir
# Sıralıdır. Index işlemleri yapılabilir.
# Kapsayıcıdır.

notes = [1, 2, 3, 4]
type(notes)

names = ["a", "b", "v", "d"]

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6][1]

type(not_nam[6][1])

notes[0] = 99
notes

not_nam[0:4]

# Liste Metodları (List Methods)

dir(notes)

len(notes)
len(not_nam)

# append: eleman ekler

notes

notes.append(100)

# pop: indexe göre siler

notes.pop(0)

# insert: indexe ekler

notes.insert(2, 99)
notes

# Sözlük (Dictonary)

# Değiştirilebilir
# Sırasız (3.7'den sonra sıralı olabilme özelliği kazanmıştır)
# Kapsayıcı

# key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary["CART"][1]

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["REG"]

# Key Sorgulama

"REG" in dictionary

"YSA" in dictionary

# KEY'e Göre Value'ya Erişmek

dictionary["REG"]
dictionary.get("REG")

# Value Değiştirmek

dictionary["REG"] = ["YSA", 10]

# Tüm Key'lere Erişmek

dictionary.keys()

# Tüm Value'lara Erişmek

dictionary.values()

# Tüm Çiftleri Tuple Halinde Listeye Çevirme

dictionary.items()

# Key-Value Değerini Güncellemek

dictionary.update({"REG":11})

# Yeni Key-Value Eklemek

dictionary.update({"RF":10})

# Demet (Tuple)
# Değiştirilemez
# Sıralıdır
# Kapsayıcıdır

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t = list(t)
t[0] = 99
t = tuple(t)

# Set
# Değiştirilebilir
# Sırasız + Eşsizdir
# Kapsayıcıdır

# difference() İki kümenin farkı

set1 = set([1, 2, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar
set2.difference(set1)
set2 - set1

# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

# intersection(): İki kümenin kesişimi

set1 = set([1, 2, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2

# union(): İki kümenin birleşimi

set1.union(set2)
set2.union(set1)

# isdisjoint(): İki kümenin kesişimi boş mu?

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)

# isdisjoint(): Bir küme diğer kümenin alt kümesi mi?

set1.issubset(set2)
set2.issubset(set1)

# issuperset(): Bir küme diğer kümeyi kapsıyor mu?

set2.issuperset(set1)
set1.issuperset(set2)