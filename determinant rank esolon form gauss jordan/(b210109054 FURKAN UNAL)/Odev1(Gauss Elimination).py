"""
ÖDEV1 = 
3x3 lük bir matrisin girdilerini
kullanıcıdan alınız. Elde ettiğiniz matrisi
Gauss eleminasyon yönetmiyle 
eşolon forma dönüştürüp elde edilen 
matrisi ekrana yazdırınız.
"""
from numpy import array, matrix,zeros
import numpy as np
import random
from numpy import array,zeros,fabs,linalg

a11 = float(input("a11 icin deger gir\n"))
a12 = float(input("a12 icin deger gir\n"))
a13 = float(input("a13 icin deger gir\n"))

a21 = float(input("a21 icin deger gir\n"))
a22 = float(input("a22 icin deger gir\n"))
a23 = float(input("a23 icin deger gir\n"))

a31 = float(input("a31 icin deger gir\n"))
a32 = float(input("a32 icin deger gir\n"))
a33 = float(input("a33 icin deger gir\n"))

birinciSatir = float(input("Birinci satirin degerini girin\n"))
ikinciSatir = float(input("ikinci satirin degerini girin\n"))
UcuncuSatir = float(input("ucuncu satirin degerini girin\n"))

matrisEsitleri = np.array([[birinciSatir],[ikinciSatir],[UcuncuSatir]])

matrix = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])

print("\nGirdiginiz Matris = \n", matrix)

print("\nGirdiginiz matrislerin sonuclari = \n",matrisEsitleri)

n = len(matrisEsitleri)

x = zeros(n)

for k in range(n-1):
    for i in range(k+1,n):
        fctr = matrix[i,k] / matrix[k,k]
        for j in range(k,n):
            matrix[i,j] = matrix[i,j] - fctr*matrix[k,j]
        matrisEsitleri[i] = matrisEsitleri[i] - fctr*matrisEsitleri[k]


x[n-1] = matrisEsitleri[n-1] / matrix[n-1,n-1]
for i in range(n-2,-1,-1):
    Sum = matrisEsitleri[i]
    for j in range(i+1,n):
        Sum = Sum - matrix[i,j]*x[j]
    
    x[i] = Sum/matrix[i,i]


print("\nDonusumlu hal(Esolon Form):\n")
print(matrix)

















