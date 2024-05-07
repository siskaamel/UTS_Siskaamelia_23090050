while True:
    tahun=int(input('Masukkan Tahun : '))
    if tahun % 4 == 0:
        print(tahun, 'Merupakan TAHUN KABISAT')
    else:
        print(tahun, 'Bukan TAHUN KABISAT')