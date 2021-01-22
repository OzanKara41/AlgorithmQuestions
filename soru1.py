def reverse_list(my_list):

    sum = 0 #Toplam değerini başta sıfır olarak seciyoruz sonradan üzerine ekleme yapılacak.
    decimal = 10 #Basamaklarını kullanarak sayıyı elde edeceğimizden 10 olan bir değişken tanımlıyoruz.
    # verilen listeyi önce ters çevireceğiz. yani lst = [1,2,3,4,5] in rev_lst  = [5,4,3,2,1] olmasını istiyoruz.

    # 1. elemanla sondakini, 2. elemanla sondan bir öncekini yer değiştirip durmamız gerekiyor. Bu sebeple len(my_list)/2) kullanıldı.
    # Aksi halde tekrardan 4. elemanla 2. elemanı, 5. elemanla 1. elemanı yer değiştirecek ve liste eski haline dönmüş olacak.
    #Bunu gerçekleştirmek için temp isminde bir değişken tanımlayıp listenin "i." indexindeki elemanı tutuyoruz. Listenin sondaki elemanını alıp
    #baştaki elemanın üstüne yazıyoruz. Ardından temp değişkeninde tuttuğumuz baştaki elemanı ise lisemizin son elemanının üstüne yazıyoruz.
    #Bu sayede elemanlar arasında yer değiştirme işlemi gerçekleşmiş oluyor.
    for i in range(0, int(len(my_list)/2)):
        temp = my_list[i]
        my_list[i] = my_list[len(my_list)-i-1]
        my_list[len(my_list)-i-1] = temp
    #Listemizin elemanlarını ters çevirdikten sonra ise her bir elemanın basamağına göre bir değer almasını istiyoruz.
    #Listedeki eleman sayımıza göre döndüreceğimiz decimal sayıyı aşağıdaki for döngüsü ile ayarlıyoruz. Örneğin verilen dizi 5 elemanlı ise
    #10000 olarak decimal değişkenini kullanacağız.
    for i in range(0, len(my_list)-2):
        decimal *= 10
    # elimizdeki decimal değerini listemizin "i." indeksindeki sayı ile çarpıyoruz. Örneğin ilk eleman 5 ise yeni sum değeri 50000 olacak.
    #2. eleman değeri örneğin 4 ise sum=50000 + 4000 olacak bunun sebebi decimali for döngüsünün her iterasyonunda 10'a bölmemizdir. Bu şekilde Sum değişkeni,
    #bize verilen dizideki elemanların basamak değerlerine göre işlem yapılarak bulunuyor. Type casting işlemi yapılamadığından dolayı bu şekilde bir işlem yapılması gerekiyor.
    for i in range(0, len(my_list)):
        sum += decimal * my_list[i]
        decimal = decimal // 10
    # fonksiyonumuzun içerisine gönderilen dizideki elemanın ters çevrilip integer bir değer olarak çıkmasını return sum ile alıyoruz. Sum değeri girilen dizi
    # lst = [5,4,3,2,1] ise sum olarak döndürülen değer integer veri tipinde 12345(onikibin üçyüzkırkbeş) oluyor.
    return sum


my_list = [7, 5, 9, 4, 6] #1. listemiz
my_list2 = [8,4]          #2. listemiz

deger1 = reverse_list(my_list) # 1. listeden döndürülen integer değer
deger2 = reverse_list(my_list2)# 2. listeden döndürülen integer değer

toplam = deger2+deger1 # sayıların toplamının hesaplanması
print(toplam) # sayıların toplamının ekrana bastırılması