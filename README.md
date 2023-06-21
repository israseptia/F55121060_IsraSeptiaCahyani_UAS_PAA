# F55121060_IsraSeptiaCahyani_UAS_PAA

UAS "PERANCANGAN ANALISIS ALGORITMA"
NAMA : ISRA SEPTIA CAHYANI
NIM  : F55121060
KELAS: B

A. Analysis Algorithm
   BUBBLE SORT
   1. Worst case
      Pada worst case, kita harus mempertimbangkan jumlah maksimum iterasi yang diperlukan untuk mengurutkan elemen dalam array. Pada bubble sort, worst case terjadi ketika
      elemen-elemen dalam array sudah dalam urutan terbalik (terbesar ke terkecil). Dalam kasus ini, setiap pasangan elemen akan menukar posisinya pada setiap iterasi.
      Jumlah iterasi yang diperlukan dalam worst case adalah sebanyak (n-1) iterasi, di mana n adalah jumlah elemen dalam array. Dalam kasus ini, dengan 74 iterasi,
      dapat disimpulkan bahwa ini adalah worst case.
   3. Best case
      Pada best case, kita mempertimbangkan jumlah minimum iterasi yang diperlukan untuk mengurutkan elemen dalam array. Pada bubble sort, best case terjadi ketika
      elemen-elemen dalam array sudah dalam urutan yang benar (terkecil ke terbesar). Dalam kasus ini, tidak ada pertukaran yang perlu dilakukan pada setiap iterasi,
      dan algoritma akan berhenti setelah satu iterasi penuh tanpa adanya pertukaran. Jumlah iterasi yang diperlukan dalam best case adalah 1 iterasi. Dalam kasus ini,
      pada iterasi ke-72, dapat disimpulkan bahwa ini adalah best case.
   5. Average case
      Pada average case, kita mempertimbangkan jumlah rata-rata iterasi yang diperlukan untuk mengurutkan elemen dalam array dengan sejumlah kemungkinan kombinasi urutan.
      Average case pada bubble sort adalah sulit untuk dihitung secara tepat, tetapi dapat diperkirakan sebagai O(n^2), di mana n adalah jumlah elemen dalam array.
      Dalam kasus ini, dengan 74 iterasi, dapat disimpulkan bahwa ini adalah average case yang terjadi.
    Pengurutan ini membutuhkan waktu komputasi sekitar 0.0013651847839355469 detik. Waktu komputasi dapat bervariasi tergantung pada kecepatan mesin dan implementasi algoritma.

   INSERTION SORT
   1. Worst case
      Kasus terburuk terjadi ketika larik bilangan awal terurut secara terbalik. Dalam kasus ini, setiap elemen harus digeser ke posisi yang benar saat iterasi dilakukan.
      Pada setiap iterasi, algoritma insertion akan membandingkan elemen yang sedang diperiksa dengan semua elemen sebelumnya dalam larik yang telah terurut.
      Dalam kasus ini, setiap elemen akan memerlukan pemindahan maksimum ke posisi yang benar, sehingga jumlah pergeseran adalah maksimum. Oleh karena itu,
      waktu komputasi dalam kasus terburuk adalah O(n^2), di mana n adalah jumlah elemen dalam larik.
   3. Best case
      Kasus terbaik terjadi ketika larik bilangan awal sudah terurut dengan benar. Dalam kasus ini, tidak ada pergeseran yang perlu dilakukan karena semua elemen sudah
      berada pada posisi yang tepat. Algoritma insertion hanya perlu memeriksa setiap elemen sekali untuk memastikan bahwa mereka berada pada posisi yang benar.
      Dalam kasus terbaik ini, waktu komputasi adalah O(n), di mana n adalah jumlah elemen dalam larik.
   5. Average case
      Kasus rata-rata mencakup semua kemungkinan larik yang diurutkan secara acak. Dalam kasus ini, setiap elemen pada iterasi pertama memerlukan maksimum satu pergeseran,
      pada iterasi kedua setiap elemen memerlukan maksimum dua pergeseran, dan seterusnya. Secara rata-rata, setiap elemen memerlukan sekitar setengah dari jumlah iterasi
      sebagai pergeseran. Oleh karena itu, waktu komputasi dalam kasus rata-rata adalah O(n^2), di mana n adalah jumlah elemen dalam larik.
    Pada kasus yang diberikan, waktu komputasi pengurutan insertion adalah 0.0014302730560302734 detik.
      
B. Analysis Algorithm untuk mengevaluasi:
    a. Worst case
    b. Best case
    c. Average case
