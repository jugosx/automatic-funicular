### Latihan Konversi Satuan Temperature

### Konversi Fahrenheit ke Kelvin


print("\nPROGRAM KONVERSI Kelvin to Fahrenheit\n")

kelvin = float(input("Masukan Suhu dalam Kelvin: "))
print("Suhu Adalah", kelvin, " Kelvin")

# ## Reamur
# reamur = (4 / 5) * celcius
# print("Suhu dalam Reamur ", reamur, " Reamur")

## Celcius
# celcius = 5 / 9 * (fahrenheit - 32)
celcius = kelvin - 273
print("Suhu dalam Celcius", celcius, " Celcius")

## Kelvin
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Kelvin", fahrenheit, " Kelvin")