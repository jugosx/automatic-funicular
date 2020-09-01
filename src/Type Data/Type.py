# Type Data: Angka Satuan (Integer)
data_integer = 1100 #yang gak ada komanya
print("Data : ", data_integer, "Bertipe : ", type(data_integer))

#Type Data: float (Angka dengan koma)
data_float = 1.5
print("Data : ", data_float, "Bertipe : ", type(data_float))

#Type Data: String (Kumpulan karakter)
data_string = "Karakt3r Bur4k"
print("Data : ", data_string, "Bertipe : ", type(data_string))

#Type Data: boolean (binary (True/False))
data_bool = True
print("Data : ", data_bool, "Bertipe : ", type(data_bool))


#Type Data Khusus

#Bilangan Kompleks
data_complex = complex(5,6)
print("Data : ", data_complex, "Bertipe : ", type(data_complex))

#Type data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(10.6)
print("Data : ", data_c_double, "Bertipe : ", type(data_c_double))