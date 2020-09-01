#Casting
#Merubah dari satu tipe ke tipe lain 
#tipe data = int, float, str, bool

#INTEGER
print("====INTEGER====")
data_int = 9
print("Data : ", data_int, "Bertipe : ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("Data : ", data_float, "Bertipe : ", type(data_float))
print("Data : ", data_str, "Bertipe : ", type(data_str))
print("Data : ", data_bool, "Bertipe : ", type(data_bool)) #akan False juka nilai int =0

print("====FLOAT====")
#FLOAT
data_float = 9.5
print("Data : ", data_float, "Bertipe : ", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)

print("Data : ", data_int, "Bertipe : ", type(data_int))
print("Data : ", data_str, "Bertipe : ", type(data_str))
print("Data : ", data_bool, "Bertipe : ", type(data_bool))#akan False juka nilai int =0

print("====BOOLEAN=====")
#BOOLEAN
data_bool = True
print("Data : ", data_bool, "Bertipe : ", type(data_bool))

data_int = int(data_bool) # akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool)

print("Data : ", data_int, "Bertipe : ", type(data_int))
print("Data : ", data_str, "Bertipe : ", type(data_str))
print("Data : ", data_float, "Bertipe : ", type(data_float))#akan False juka nilai int =0


print("====STRING====")
#STRING
data_str = "Text String"
print("Data : ", data_str, "Bertipe : ", type(data_str))

data_int = int(data_str) # string harus angka
data_bool = bool(data_str)#False jika stringnya kosong
data_float = float(data_str) #string harus angka

print("Data : ", data_int, "Bertipe : ", type(data_int))
print("Data : ", data_bool, "Bertipe : ", type(data_bool))
print("Data : ", data_float, "Bertipe : ", type(data_float))#akan False juka nilai int =0