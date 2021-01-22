def add_element(element, my_list, element_before): # element = yazmak istediğimiz değer, my_list=verdiğimiz liste, element_before=kontrol edilen sayı ve bu değerden sonra element değeri yazdırılacak.
    temp = [0] * (len(my_list) + 1) # sıfırlardan oluşan bir temp listesi oluşturup eleman sayısını verilen listenin eleman sayısından 1 fazla olacak şekilde seçtim.
    index = 0 #while döngüsü kullanacağımdan indexi başta 0  olarak tanımladım.

    #ilk while döngüsü 0 dan başlayıp son indekse kadar gidecek. Bu işlem yapılırken eğer üzerinde durulan indeksin değeri 3 değil ise(başka değer de girilebilir 3 olmak zorunda değil
    # element_before değeri bizim eşleşen değerimizi temsil etmektedir.) temp değişkenine listemizin indeksindeki değeri yazıyoruz.
    while index <= len(my_list)-1:
        if my_list[index] != element_before: # eğer 3 değerine gelmemiş isek
            temp[index] = my_list[index]#3 değerine gelene kadarki sayıları temp'de tutuyoruz.(her iterasyonda 1 değer eklenecek şekilde)
            index += 1 # bir sonraki indekse bakmak için index değişkenini 1 arttırıyoruz.
        elif my_list[index] == element_before: # eğer bulunduğumuz indeksin değeri 3 ise
            temp[index] = my_list[index] # 3 değerini de yine temp listemize atıyoruz. bu kısma gelene kadar temp içersinde [1,2,3,0,0,0] olmuş oluyor.
            temp[index + 1] = element # elimizdeki temp listesinde 3. indekse 8 değerini yazıyoruz. [1,2,3,8,0,0]
            index += 2 # bir sonraki while döngüsünde temp listesinde kaldığımız indeksden devam edebilmek için 2 olan index değerimizi 2 ekleyerek 4 yapıyoruz.
            break # index değerini 4 yaptık ve bu döngüden çıktık. Temp listesindeki kalan 2 sıfırı da değiştirip yerine 4 ve 5 yazmak için alttaki döngüyü kullanacağız.

    i = 0 # başlangıç değerini 0 olarak belirliyoruz.
    while i <= len(my_list)-index: # bu döngünün kaç kere döneceğini elimizdeki temp listesinde kaç sıfır olduğu belirliyor. Bu sebeple döngü 0 ve 1 için dönecek
        temp[i + index] = my_list[i + index-1] #kendi listemizdeki 4 ve 5 değerini alıp temp listesindeki 4. ve 5. indekse yazıyoruz. Bunun çıktısı ise [1,2,3,8,4,5] oluyor.
        i += 1

    return temp # elde etmek istediğimiz liste temp listesi olduğundan bu fonksiyon için bu listeyi döndürüyoruz.

my_list = [1,2,3,4,5] #liste tanımlanıyor
sonuc = add_element(8,my_list,3) #tanımlanan listeye 3 değerinden sonra 8 eklenmesi işlemi tanımlanan fonksiyon ile yapılıyor.

print(sonuc)# elde edilen temp listesini yazdırıyor.

#not: liste içerisinde birden fazla element değeri(3) olması durumu yapılmamıştır.