"""
ÖDEV2 =
Girdileri (-20,80) aralığından rastgele
seçilen 5x5 lik bir matris oluşturup Gauss-Jordan
yöntemi ile indirgenmiş 
eşolon forma dönüştürüp elde edilen matrisi ekrana yazdırınız

"""
import numpy as np
import random
k = 0
while k == 0:


    Matrisim = [[0 for x in range(5)] for y in range(5) ]

    for i in range(5):
        for j in range(5):
            Matrisim[i][j]  = random.randint(-20,80)
            Matrisim[i][j] = random.randint(-20,80)

    print("\nRastgele 5x5'lik matris = \n{}".format(Matrisim))


    matrisEsitleri = [[0 for x in range(5)] for y in range(5)]

    for i in range(5):
        matrisEsitleri[i] = random.randint(0,10)




    def GaussJordanMethod(a,b):
        a = np.array(a, float)
        b = np.array(b, float)
        n = len(b)

        for k in range(n):
            if np.fabs(a[k,k]) < 1.0e-12:
                for i in range(k+1,n):
                    if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                        for j in range(k,n):
                            a[k,j],a[i,j] = a[i,j],a[k,j]
                        b[k],b[i] = b[i],b[k]
                        break

            
            pivot = a[k,k]
            for j in range(k,n):
                a[k,j] /= pivot
            b[k]  /=pivot

            for i in range(n):
                if i == k or a[i,k] ==0:
                    continue
                factor = a[i,k]
                for j in range(k,n):
                    a[i,j] -= factor * a[k,j]
                b[i] -= factor*b[k]

        return b,a

    a = Matrisim
    b = matrisEsitleri

    X,A = GaussJordanMethod(a,b)


    print("\n\nGauss Jordan Çözüm(x1,x2,x3,x4,x5) = \n\n" , X )

    print("\n\nDönüstürülmüs Hali =\n\n",A)

    secim = input("Devam etmek istiyor musunuz? (e/h)")

    if secim == 'e':
        k = 0

    elif secim == 'h':
        k = 1
    
    else:
        print("Yanlis secim yaptiniz.")
        k = 1





























    








