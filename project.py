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

