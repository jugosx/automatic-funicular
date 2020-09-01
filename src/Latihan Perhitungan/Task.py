### Latihan Konversi Satuan Temperature

### Konversi Fahrenheit ke Kelvin


print("\nPROGRAM KONVERSI Fahrenheit to Kelvin\n")

fahrenheit = float(input("Masukan Suhu dalam Fahrenheit: "))
print("Suhu Adalah", fahrenheit, " Fahrenheit")

# ## Reamur
# reamur = (4 / 5) * celcius
# print("Suhu dalam Reamur ", reamur, " Reamur")

## Celcius
# celcius = 5 / 9 * (fahrenheit - 32)
celcius = (fahrenheit - 32)*5/9
print("Suhu dalam Celcius", celcius, " Celcius")

## Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin", kelvin, " Kelvin")