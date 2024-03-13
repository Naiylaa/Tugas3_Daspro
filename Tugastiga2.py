# Data list pertama sebagai kunci (key)
keys = ['nama', 'Npm', 'usia', 'alamat']

# Data list kedua sebagai nilai (value)
values = ['Naiyla S. Karim', '07352311164', 18, 'Jl. Kel. Jati. No. 07']

# Fungsi untuk mengubah dua data list menjadi data dictionary
def lists_to_dict(keys, values):
    data_dict = dict(zip(keys, values))
    return data_dict

# Memanggil fungsi dan menampilkan data dictionary hasil konversi
data_dictionary = lists_to_dict(keys, values)
print("Data Dictionary:")
print(data_dictionary)
