import math

totalTimur = 0.0
totalUtara = 0.0

while True:
    arah = input("Masukkan arah (Utara/Timur) atau ketik 'selesai' untuk keluar: ")
    if arah.lower() == "selesai":
        break

    if arah.lower() not in ["timur", "utara"]:
        print("Arah tidak valid. Silakan masukkan 'Timur' atau 'Utara'.")
        continue

    try:
        jarak = float(input("Masukkan jarak (dalam meter): "))
    except ValueError:
        print("Input tidak valid. Silakan masukkan jarak dan arah yang benar.")
        continue

    if arah.lower() == "timur":
        totalTimur += jarak
    elif arah.lower() == "utara":
        totalUtara += jarak

    print(f"Tercatat perpindahan ke {arah}: {jarak} meter")
    print(f"Total perpindahan ke Utara: {totalUtara} meter, Total perpindahan ke Timur: {totalTimur} meter")

resultan = math.sqrt(totalTimur**2 + totalUtara**2)
print(f"Resultan perpindahan: {resultan:.2f} meter")
