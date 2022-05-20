"""
ÖDEV3 = 
Matris boyutunu kullanıcının 
belirlediği ve girdileri rastgele 
bir aralıktan seçilen bir matris 
oluşturup elde edilen
matrisin rankını ve 
determinantını ekrana yazdırınız.

"""

import numpy as np
import random

k = 0

while k == 0:


    matrisDegerleri = random.randint(0, 10)

    satirSayisi = int(input("Satır sayisi gir.\n"))

    sutunSayisi = int(input("\nSutün sayisi gir.\n"))


    A = [] ## BU BENİM MATRİSİM

    for i in range(satirSayisi): ## ilk döngüde satir sayilari arasinda geziyorum.
        temp = [] ## matrisin icindeki listeyi olusturdum.
        for j in range (sutunSayisi): ## ikinci dongude sutunlar arasi geziyorum.
            temp.append(0)  ## sutun sayilarini ve satir sayilarini klavyeden aldigim kadar matrisime ekleme islemi yapiyor.
        A.append(temp) ## satir ve sutun sayilarini rastgele ekleme isleminden sonra matrisime ekliyorum.


    for i in range(sutunSayisi):
        top = 0
        for j in range (satirSayisi - 1):
            A[j][i] = random.randint(0, 10) ## satır ve sutun sayilarimi rastgele 0 dan 10 a kadar sayilar arasindan seviyorum.
            top += A[j][i] ## olusturdugum top degiskenini random degerler verdigim matris girdileriyle topluyorum.
        A[satirSayisi-1][i] = matrisDegerleri - top 


    print("\nRastgele girdi degerine sahip matris = \n",A)


    # Determinant hesaplama
    print("\nMatrisin Determinantı = " , np.linalg.det(A)) ## numpy kutuphanesinin ozel kodu np.linalg.det(A) ile determinant hesaplatıyorum.



    # Rank (sıralama) hesaplama
    print("\nMatrisin Rankı = " ,np.linalg.matrix_rank(A)) ## yine nnumpy kutuphanesinin ozel kodu np.linalg.matrix_rank(A) ile rank hesaplatıyorum.


    secim = input("\nDevam etmek istiyor musun? (e/h)\n")

    if secim == 'e':
        k = 0

    elif secim == 'h':
        print("cikis yapiliyor...")
        k = 1

    else:
        print("Hatali giris yapildi...")
        k = 1

    



