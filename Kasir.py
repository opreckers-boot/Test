total1=0
total2=0
totalsemua=0
jenis1=""
jenis2=""

print("=== Program Kasir Sederhana Opreckers ===")
nama = input("Masukkan nama Konsumen: ")
print ("Nama Konsumen :", nama)
print("")
print ("Menu Makanan")
    


def pilihan(i):
        switcher={
                1:'----Nasi Goreng 10000----',
                2:'----Soto 11000----',
                3:'----Mie Ayam 10000----',
                4:'----Bakso 6000----',
                5:'----Kerupuk 1000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")


print("1. Nasi Goreng")
print("2. Soto")
print("3. Mie Ayam")
print("4. Bakso")
print("5. Kerupuk")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
porsi1= int(input("Berapa Porsi: "))

if nomor==1:
    total1=total1+porsi1*10000
    print ("Hasilnya = ", total1)
    jenis1=("Nasi Goreng")
if nomor==2:
    total1=total1+porsi1*11000
    print ("Hasilnya = ", total1)
    jenis1=("Soto")
if nomor==3:
    total1=total1+porsi1*10000
    print ("Hasilnya = ", total1)
    jenis1=("Mie Ayam")
if nomor==4:
	total1=total1+porsi1*6000
	print ("Hasilnya = ", total1)
	jenis1=("Bakso")
if nomor==5:
	total1=total1+porsi1*1000
	print ("Hasilnya = ", total1)
	jenis1=("Kerupuk")
def pilihan(i):
        switcher={
                1:'----Es Teh 3000----',
                2:'----Es Jeruk 4000----',
                3:'----Kopi 3000----',
                4:'----Susu Jahe 4000----',
                5:'----Joshua 5000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")
print("\nMenu Minuman")
print("1. Es teh")
print("2. Es jeruk")
print("3. kopi")
print("4. Susu Jahe")
print("5. Joshua")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
porsi2= int(input("Berapa Gelas: "))
if nomor==1:
    total2=total2+(porsi2*3000)
    print ("Hasilnya = ", total2)
    jenis2=("Es Teh")
if nomor==2:
    total2=total2+(porsi2*4000)
    print ("Hasilnya = ", total2)
    jenis2=("Es Jeruk")
if nomor==3:
    total2=total2+(porsi2*3000)
    print ("Hasilnya = ", total2)
    jenis2=("Kopi")
if nomor==4:
	total2=total2+(porsi2*4000)
	print ("Hasilnya = ", total2)
	jenis2=("Susu Jahe")
if nomor==5:
	total2=total2+(porsi2*5000)
	print ("Hasilnya = ", total2)
uang=int(input("\nUang Tunai: Rp."))
totalsemua=total1+total2    
print("\n=========================")
print("======= S T R U K =======")
print("=========================")
print ("=== Nama      :",nama)
print ("=== Beli      :",porsi1,jenis1)
print ("===            ",porsi2,jenis2)
print ("=== Tagihan   :Rp.",totalsemua)
print ("=== Uang      :Rp.",uang)
akhir=int(uang-totalsemua)
print ("=== Kembalian :Rp.",akhir)
print("=========================")
print("=========================")