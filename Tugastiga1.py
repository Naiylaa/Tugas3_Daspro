# Data dictionary 
data_mahasiswa = {
    'Nurhasna': '07352311161',
    'Serly': '07352311162',
    'Nabila': '07352311163',
    'Naiyla S. Karim': '07352311164',
    'Manda': '07352311165',
    'Fika': '07352311166',
    'Acha': '07352311167',
    'Aridoh': '07352311168',
    'Nabil': '07352311169',
    'Ela': '07352311170'
}

# Fungsi untuk melakukan login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print(f"Selamat datang, {username}!")
    else:
        print("password salah silahkan Coba lagi.")

# Memanggil fungsi login
login()
