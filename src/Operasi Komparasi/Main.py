### Operasi Komparasi
### Setiap Hasil dari Operasi Komparasi adalah Boolean

'''
>, <, >=, <=, ==, !=, is, is not
'''

a = 4
b = 2

#Lebih Besar Dari
print('==== Lebih Besar Dari (>)')
hasil = a > 3
print(a,'>', 3,'=', hasil)
hasil = b > 3
print(a,'>', 3,'=', hasil)

#Kurang Dari Dari
print('==== Kurang Dari (<)')
hasil = a < 3
print(a,'<', 3,'=', hasil)
hasil = b < 3
print(a,'<', 3,'=', hasil)

#Lebih Besar Dari Sama Dengan
print('==== Lebih Besar Dari Sama Dengan (>=)')
hasil = a >= 3
print(a,'>=', 3,'=', hasil)
hasil = b >= 2
print(a,'>=', 3,'=', hasil)

#Kurang Dari Dari Sama Dengan
print('==== Kurang Dari Sama Dengan (<=)')
hasil = a <= 4
print(a,'<=', 3,'=', hasil)
hasil = b < 3
print(a,'<=', 3,'=', hasil)

#Sama Dengan
print('==== Sama Dengan (==)')
hasil = a == 4
print(a,'==', 3,'=', hasil)
hasil = b == 3
print(a,'==', 3,'=', hasil)

#Tidak Sama Dengan
print('==== Tidak Sama Dengan (==)')
hasil = a != 4
print(a,'!=', 3,'=', hasil)
hasil = b != 3
print(a,'!=', 3,'=', hasil)


print('==== Object Identity (is)')
# 'is' sebagai komparasi object identity

x = 5 # ini adalah assignment membuat object
y = 5

print('nilai x =', x ,'id = ', hex(id(x)))
print('nilai y =', y ,'id = ', hex(id(y)))

print('x is y =', hasil)

print('==== Object Identity (is not)')
# 'is not' sebagai komparasi object identity

x = 5 # ini adalah assignment membuat object
y = 6

print('nilai x =', x ,'id = ', hex(id(x)))
print('nilai y =', y ,'id = ', hex(id(y)))

print('x is not y =', hasil)
