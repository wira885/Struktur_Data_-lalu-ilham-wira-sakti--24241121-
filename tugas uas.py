# Daftar NIM dan Nama Mahasiswa
mahasiswa = {
    "24241125": "Elen Jaelani",
    "24241121": "Ilham Wira Sakti",
    "24241141": "Muhammad Azizi Maulana Alpharezi"
}

# Menampilkan daftar mahasiswa
print("Daftar Mahasiswa Kelompok 1:")
for nim, nama in mahasiswa.items():
    print(f"NIM: {nim} | Nama: {nama}")
def meet1():
    print("===== Meet 1: Tabel Kebenaran =====")
    print("A\tB\tA AND B\tA OR B\tNOT A")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{A}\t{B}\t{A and B}\t{A or B}\t{not A}")
def meet2():
    print("===== Meet 2: Operasi Logika =====")
    a = input("Masukkan A (1 = True, 0 = False): ")
    b = input("Masukkan B (1 = True, 0 = False): ")

    if a in ['1', '0'] and b in ['1', '0']:
        a = bool(int(a))
        b = bool(int(b))
        print(f"A AND B = {a and b}")
        print(f"A OR B = {a or b}")
        print(f"NOT A = {not a}")
    else:
        print("Input salah. Hanya masukkan 1 atau 0.")

def meet3():
    print("===== Meet 3: Ambil Digit Angka =====")
    angka = input("Masukkan angka: ")
    if angka.isdigit():
        for digit in angka:
            print(digit)
    else:
        print("Input harus berupa angka!")

def main():
    while True:
        print("\n=== Menu ===")
        print("1. Meet1 - Tabel Kebenaran")
        print("2. Meet2 - Operasi Logika")
        print("3. Meet3 - Ambil Digit Angka")
        print("0. Keluar")
        
        pilihan = input("Pilih program (0-3): ")

        if pilihan == "1":
            meet1()
        elif pilihan == "2":
            meet2()
        elif pilihan == "3":
            meet3()
        elif pilihan == "0":
            print("Terima kasih. Keluar...")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

main()