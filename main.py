import model
import view
import os


while True:
    print('\n|================|')
    print('|  Pilihan Menu  |')
    print('|================|')
    print('\n1. Tambah Data')
    print('2. Hapus Data')
    print('3. Ubah Data')
    print('4. Cari Data')
    print('5. Lihat Semua Data')
    print('6. Keluar ')

    pilihan = input('\nMasukan Pilihan Menu = ')

    if pilihan == '1':
        view.input_nilai.masukan_data()
    elif pilihan == '2':
        view.input_nilai.cari_hapus()
    elif pilihan == '3':
        view.input_nilai.cari_ubah()
    elif pilihan == '4':
        model.daftar_nilai.cari_data()
    elif pilihan == '5':
        view.view_nilai.tampilkan()
    elif pilihan == '6':
        break
    else:
        print('Masukan Pilihan yang Benar!!')
