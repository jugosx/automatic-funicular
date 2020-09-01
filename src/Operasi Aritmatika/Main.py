#Operasi Aritmatika

a = 10
b = 3

#Operasi Penjumlahan
hasil = a + b
print(a, "+", b, "=", hasil)

#Operasi Pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

#Operasi Perkalian
hasil = a * b
print(a, "*", b, "=", hasil)

#Operasi Pembagian
hasil = a / b
print(a, "/", b, "=", hasil)

#Operasi Eksponen (Perpangkatan)
hasil = a ** b
print(a, "**", b, "=", hasil)

#Operasi Modulus (Sisa Hasil Pembagian)
hasil = a % b
print(a, "%", b, "=", hasil)

#Operasi Floor Division // (Hasil bagi dibulatkan kebawah)

hasil = a // b
print(a, "//", b, "=", hasil)

'''
    1. ()
    2. Exponen ** (Perpangkatan)
    3. Perkalian dan teman-temanya * / ** % //
    4. Pertambahan, Pengurangan - +
'''

#Prioritas Operasi, Operational Precedence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, "=", hasil)


hasil = (x + y) * z
print('(',x,"+",y,") *",z, "=", hasil)