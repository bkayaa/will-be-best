from cgi import print_arguments

kontrol = 1

while kontrol == 1:
    print("Toplama işlemi için 1'e basın.\n", "Çıkarma işlemi için 2'ye basın.\n", "Çarpma işlemi için 3'e basın.\n", "Bölme işlemi için 4'e basın.\n", "Çıkış yapmak için 5'e basın.")
    işlem = input("Seçim:")
    while işlem == "1":
        sayi1 = float(input("İlk sayıyı giriniz:"))
        sayi2 = float(input("İkinci sayıyı giriniz:"))
        print("Sayıların toplamı:", sayi1 + sayi2, "\nToplama işlemine devam için 2'ye basın." , "Menüye dönmek için 1'e basın.")
        secim = input("Seçiminiz:")
        if secim == "1":
            işlem = "0"
            break
        else:
            continue
    while işlem == "2":
        sayi1 = float(input("İlk sayıyı giriniz:"))
        sayi2 = float(input("İkinci sayıyı giriniz:"))
        print("Sayıların çıkarması:", sayi1 - sayi2, "\nÇıkarma işlemine devam etmek için 2'ye basın.", "Menüye dönmek için 1'e basın.")
        secim = input("Seçiminiz:")
        if secim == "1":
            işlem = "0"
            break
        else:
            continue
    while işlem == "3":
        sayi1 = float(input("İlk sayıyı giriniz:"))
        sayi2 = float(input("İkinci sayıyı giriniz:"))
        print("Sayıların çarpımı:", sayi1 * sayi2, "\nÇarpma işlemine devam etmek için 2'ye basın.", "Menüye dönmek için 1'e basın.")  
        secim = input("Seçiminiz:")
        if secim == "1":
            işlem = "0"
            break
        else:
            continue
    while işlem == "4":
        sayi1 = float(input("İlk sayıyı giriniz:"))
        sayi2 = float(input("İkinci sayıyı giriniz:"))
        print("Sayıların bölümü:", sayi1 / sayi2, "\nBölme işlemine devam etmek için 2'ye basın." "Menüye dönmek için 1'e basın.")
        secim = input("Seçiminiz:")
        if secim == "1":
            işlem = "0"
            break
        else:
            continue
    if işlem >= "5":
            kontrol = 0
            print("Çıkış yapılıyor.")
