#Aplikasi game secret number

secret_number = 333
guess_number = int(input("Masukkan tebak angka:"))

while guess_number != secret_number:
    print("Tebakan salah, silakan coba lagi")
    guess_number = int(input("Masukkan tebak angka:"))

print("Selamat... Tebakan Anda benar!!")
print("Kode inik saya buat di codespace")