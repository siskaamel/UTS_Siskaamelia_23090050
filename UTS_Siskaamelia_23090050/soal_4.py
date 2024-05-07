berat_badan=int(input('Masukkan Berat Badan : '))
tinggi_badan=float(input('Masukkan Tinggi Badan : '))

BMI = berat_badan / tinggi_badan ** 2
print(f'Nilai BMI Anda : {BMI}')
if BMI <=18.5:
    print(BMI,'Berat badan kurang')
elif BMI  <=24.9:
    print(BMI, 'Berat badan normal')
elif BMI <=29.9:
    print(BMI, 'Kelebihan berat badan')
else:
    print(BMI,'Obesitas')