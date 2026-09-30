def GameResultan():
    x = 0.0  
    y = 0.0  
    enemyHealth = 100

    print("\nKamu adalah seorang pahlawan yang memiliki skill yang memiliki damage berdasarkan resultan dari sebuah Vektor tapi hanya bisa digunakan 1 kali.")
    print("Objektifmu harus mengalahkan boss dengan cara menggerakkan karakter anda ditengah peperangan dengan banyak rintangan ini.\n")
    
    while True:
        arah = input("Masukkan arah (utara/selatan/timur/barat) atau 'serang': ").lower()
        
        # Jika pengguna memasukkan 'serang', keluar dari loop
        if arah == 'serang':
            break
            
        # Validasi input arah, jika tidak valid, minta input ulang
        if arah not in ['utara', 'selatan', 'timur', 'barat']:
            print("Arah tidak dikenali!\n")
            continue

        # Minta input jarak dan validasi input
        try:
            jarak = float(input(f"Berapa meter ke {arah}? "))
        except ValueError:
            print("Harap masukkan angka!\n")
            continue

        # Update posisi berdasarkan arah dan jarak, jika selatan atau barat, jarak dikurangi
        if arah == 'utara':
            y += jarak
        elif arah == 'selatan':
            y -= jarak
        elif arah == 'timur':
            x += jarak
        elif arah == 'barat':
            x -= jarak
            
        print(f"Posisi saat ini: ({x} m, {y} m)\n")

    # Hitung resultan dari perpindahan ( resultan = √(x² + y²) )
    resultan = (x**2 + y**2) ** 0.5
    enemyHealth -= resultan
    if enemyHealth < 0:
        enemyHealth = 0

    print("\n=== HASIL PENYERANGAN ===")
    print(f"Posisi Akhir Sumbu X : {x}m")
    print(f"Posisi Akhir Sumbu Y : {y}m")
    print(f"Damage Resultan      : {resultan:.2f} (m)")
    print(f"HP Boss              : {enemyHealth:.2f} \n")

    if enemyHealth <= 0:
        print("Selamat! Kamu berhasil mengalahkan boss!")
    else:
        print("Boss masih hidup! Ayo coba lagi!")
    
GameResultan()

