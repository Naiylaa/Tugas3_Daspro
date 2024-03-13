# Data dictionary pertama
jadwalDasproIf2 = {
    'Senin': 'jam 08:00', 
    'Selasa': 'jam 08:00',
    'Rabu': 'jam 10:50',
    'Kamis': '15:50 ',
    'Jumat': '08:00'
}

# Data dictionary kedua
jadwalDasproIf3 = {
    'Senin': 'jam 08:00',
    'Selasa': 'jam 08:00',
    'Rabu': '15:00',
    'Kamis': '10:50',
    'Jumat': '08:00'
}

# Menggabungkan dua data dictionary
jadwalDasproIf3.update(jadwalDasproIf2)

# Menampilkan hasil gabungan
print("Jadwal Gabungan:")
print(jadwalDasproIf3)
