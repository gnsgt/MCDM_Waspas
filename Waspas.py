import pandas as pd
import numpy as np

    #Excel dosyasını oku ve DataFrame'e dönüştür
df_excel = pd.read_excel("C:/Users/gokha/OneDrive/Masaüstü/Tez/2.1-Waspas.xlsx")
maliyet = df_excel.iloc[1:2].copy()
agirlik = df_excel.iloc[:1].copy()
df = df_excel.iloc[2:]  

satir_sayisi = df.shape[0]
sutun_sayisi = df.shape[1]
    
minmax = []
for i in range(sutun_sayisi):
    if maliyet.iloc[0, i] == "maliyet":
        minmax.append(df.iloc[:, i].min())  
    else:
        minmax.append(df.iloc[:, i].max())
        
#Normalize Islemi
normalize_df = df.copy()  # df verilerini kopyala
for i in range(sutun_sayisi):
    if maliyet.iloc[0, i] == "maliyet":
        normalize_df.iloc[:, i] = minmax[i] / df.iloc[:, i] 
    else:
        normalize_df.iloc[:, i] = df.iloc[:, i]  / minmax[i]
        

    #WSM Hesaplama
wsm = []
for j in range(satir_sayisi):
    wsm_toplam = 0
    for i in range(sutun_sayisi):
        wsm_toplam = (normalize_df.iloc[j,i] * agirlik.iloc[0,i]) + wsm_toplam
    wsm.append(wsm_toplam)
                   

    
    #WPM Hesaplama
wpm = []
for j in range(satir_sayisi):
    wpm_toplam = 1
    for i in range(sutun_sayisi):
        wpm_toplam = (normalize_df.iloc[j,i] ** agirlik.iloc[0,i]) * wpm_toplam
    wpm.append(wpm_toplam)
                   

    #Alfa = 0.05 icin WASPAS
waspas = []
for i in range(len(wpm)):
    waspas.append(wpm[i]*0.05 + wsm[i]*0.05)


    #WPM Yazdirma
for i in range(satir_sayisi):
    max_deger = max(wpm)
    max_index = wpm.index(max_deger)
    print(f"WPM Değer: {max_deger}, İndex: {max_index + 1}")
    wpm[max_index] = -99999
print("\n")
    
    #WSM Yazdirma
for i in range(satir_sayisi):
    max_deger = max(wsm)
    max_index = wsm.index(max_deger)
    print(f"WSM Değer: {max_deger}, İndex: {max_index + 1}")
    wsm[max_index] = -99999
print("\n")

    #Waspas Yazdirma
for i in range(satir_sayisi):
    max_deger = max(waspas)
    max_index = waspas.index(max_deger)
    print(f"WASPAS Değer: {max_deger}, İndex: {max_index + 1}")
    waspas[max_index] = -99999
    

