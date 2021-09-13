import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# tum sutunları goster.
pd.pandas.set_option('display.max_columns', None)


# dataframe' i ozetle
def check_df(dataframe, head=5, tail=10):
    print(f"first {head} rows : {dataframe.head(head)}")
    print("#######################################")
    print(f"last {tail} rows : {dataframe.tail(tail)}")
    print("#######################################")
    print(f"Shape : {dataframe.shape}")
    print("#######################################")
    print(f"info : {dataframe.info()}")
    print("#######################################")
    print(f"columns : {dataframe.columns}")
    print("#######################################")
    print(f"describe : {dataframe.describe().T}")


# value counts fonksiyonu
def valuecount(dataframe, colname):
    print(pd.DataFrame({colname: dataframe[colname].value_counts()}))
    print(f"unique : {dataframe[colname].unique()} \nnunique : {dataframe[colname].nunique()}")


############################
# ----- GÖREV 1 -----
###########################

###################################
# SORU 1- persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz
###################################
def load_persona():
    df = pd.read_csv("D:\VERİBİLİMİOKULU\VERİSETLERİ\persona.csv")
    return df


df = load_persona()

###################################
# SORU 2- Kaç unique SOURCE vardır? Frekansları nedir?
###################################
# q1
len(df["SOURCE"].unique())
# or
df["SOURCE"].nunique()

# q2
df["SOURCE"].value_counts()
# or
valuecount(df, "SOURCE")

###################################
# SORU 3- Kaç unique PRICE vardır?
###################################
len(df["PRICE"].unique())
# or
valuecount(df, "PRICE")
# or
df["PRICE"].nunique()

##################################
# SORU 4- Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
##################################
df["PRICE"].value_counts()
valuecount(df, "PRICE")

sns.countplot(x=df["PRICE"], data=df)
plt.show()

##################################
# SORU 5- Hangi ülkeden kaçar tane satış olmuş?
##################################
df["COUNTRY"].value_counts()
# or
valuecount(df, "COUNTRY")

sns.countplot(x=df["COUNTRY"], hue=df["SEX"], data=df)
plt.show()

##################################
# SORU 6- Ülkelere göre satışlardan toplam ne kadar kazanılmış?
##################################
df.groupby("COUNTRY").agg({"PRICE": "sum"})
df.groupby("COUNTRY").agg({"PRICE":lambda x: x.sum()})

##################################
# SORU 7- SOURCE türlerine göre göre satış sayıları nedir?
##################################
df.groupby("SOURCE").agg({"PRICE": "sum"})

##################################
# SORU 8- Ülkelere göre PRICE ortalamaları nedir
##################################
df.groupby("COUNTRY").agg({"PRICE": "mean"})

##################################
# SORU 9- SOURCE'lara göre PRICE ortalamaları nedir
##################################
df.groupby("SOURCE").agg({"PRICE": "mean"})

##################################
# SORU 10- COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
##################################
df.groupby(["SOURCE", "COUNTRY"]).agg({"PRICE": "mean"})

############################
# ----- GÖREV 2 -----

# COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
###########################
group_df = grupla(dataframe=df, colname=["COUNTRY", "SOURCE", "SEX", "AGE"], agg_colname="PRICE", agg="mean", turn=True)
# or
group_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

############################
# ----- GÖREV 3 -----

# Çıktıyı PRICE’a göre sıralayınız.
###########################
agg_df = group_df.sort_values("PRICE", ascending=False)

############################
# ----- GÖREV 4 -----

# Index’te yer alan isimleri değişken ismine çeviriniz.
###########################
agg_df = agg_df.reset_index()

############################
# ----- GÖREV 5 -----

# age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz
###########################
# example : https://pbpython.com/pandas-qcut-cut.html
bins = [0, 18, 23, 30, 40, 70]
labels = ["0_18", "19_23", "24_30", "31_40", "41_70"]


def cutt(dataframe, colname, bins, labels=None):
    if labels != None:
        cut_series = pd.cut(dataframe[colname],
                            labels=labels,
                            bins=bins)
    else:
        cut_series = pd.cut(dataframe[colname],
                            bins=bins)
    return cut_series


agg_df["AGE_CAT"] = cutt(agg_df, "AGE", bins, labels)

############################
# ----- GÖREV 6 -----

# Yeni seviye tabanlı müşterileri (persona) tanımlayınız
###########################
# collect the string and assign to variable customer_level_based
agg_df["customer_level_based"] = [col[0].upper() + "_" + col[1].upper() + "_" + col[2].upper() + "_" + col[5] for col in
                        agg_df.values]

agg_df_new = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"})
agg_df_new = agg_df_new.reset_index()

############################
# ----- GÖREV 7 -----

# Yeni müşterileri (personaları) segmentlere ayırınız
###########################

agg_df_new["SEGMENT"] = pd.qcut(agg_df_new["PRICE"], q=4, labels=["D", "C", "B", "A"])

# analysis

agg_df_new.groupby("SEGMENT").agg({"PRICE": ["mean", "min", "max", "sum"]})
segment_c = agg_df_new.loc[agg_df_new["SEGMENT"] == "C", :]
check_df(segment_c)

segment_c["customer_level_based"].unique()
segment_c["customer_level_based"].nunique()

agg_df_new.describe().T

############################
# ----- GÖREV 8 -----

# Yeni gelen müşterileri segmentlerine göre sınıflandırınız ve ne kadar gelir getirebileceğini tahmin ediniz
###########################
# PREDICT

new_user = "TUR_ANDROID_FEMALE_31_40"
new_user2 = 'FRA_IOS_FEMALE_31_40'

predict_user_1 = agg_df_new[agg_df_new["customer_level_based"] == new_user]
predict_user_2 = agg_df_new[agg_df_new["customer_level_based"] == new_user2]

print(predict_user_1)
print(predict_user_2)