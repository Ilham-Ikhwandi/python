print('Calculator Kekinian')
print('=' *25)


print('Operasi Matematika')
print('1. Penjumlahan \t [+]')
print('2. Pengurangan \t[-]')
print('3. Perkalian \t [*]')
print('4. Pembagian \t[/]')

print('='*25)

oprasi= input('Pilih Oprasi 1/2/3/4 : ')

print('='*25)

if oprasi == '1':
    print('User Memilih Penjumlahan')
elif oprasi == '2':
    print('User Memilibh Pengurangan')
elif oprasi == '3':
    print('User Memilih Perkalian')
elif oprasi == '4':
    print('User Memilih Pembagian')
else :
    print('Filed')
    exit(0)
    
print('='*25)

a = int(input('Masukan Angka Pertama : '))
b = int(input('Masukan ANgaka Ke Dua : '))


    
print('='*25)

if oprasi == '1':
    hasil = a+b
    print(f'Hasil operasi dari {a} + {b} = {hasil}')
elif oprasi == '2':
    hasil = a-b
    print(f'Hasil operasi dari {a} - {b} = {hasil}')
elif oprasi == '3':
    hasil = a*b
    print(f'Hasil operasi dari {a} * {b} = {hasil}')
elif oprasi == '4':
    hasil = a/b
    print(f'Hasil operasi dari {a} / {b} = {hasil}')
else :
    print('Filed')

