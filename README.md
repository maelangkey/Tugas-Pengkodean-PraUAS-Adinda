**DATA TABEL**
Tabel Produksi:
No	Barang	Jumlah Produksi
1	Barang A	100
2	Barang B	150
3	Barang C	200
4	Barang D	180
5	Barang E	220
6	Barang F	120
7	Barang G	90
8	Barang H	210
9	Barang I	160
10	Barang J	190

Tabel Penjualan:
No	Barang	Jumlah Penjualan
1	Barang A	80
2	Barang B	120
3	Barang C	150
4	Barang D	100
5	Barang E	180
6	Barang F	70
7	Barang G	60
8	Barang H	200
9	Barang I	130
10	Barang J	170

Tabel Persediaan:
No	Barang	Jumlah Persediaan
1	Barang A	20
2	Barang B	30
3	Barang C	50
4	Barang D	80
5	Barang E	40
6	Barang F	50
7	Barang G	30
8	Barang H	10
9	Barang I	30
10	Barang J	20


**LANGKAH-LANGKAH :**
1. Deskripsi Data:
Pertama, tinjau struktur data untuk memahami atributnya.
Anda dapat menggunakan head() untuk melihat beberapa baris pertama dari DataFrame dan info() untuk melihat informasi tentang tipe data dan jumlah nilai non-null.

2. Statistik Deskriptif:
Hitung statistik deskriptif seperti rata-rata, median, kuartil, dan deviasi standar untuk kedua variabel.
Gunakan fungsi describe() pada DataFrame untuk mendapatkan ringkasan statistik deskriptif.

3. Visualisasi Data:
Gunakan histogram untuk melihat distribusi data penjualan dan persediaan.
Anda juga dapat membuat diagram batang atau pie chart untuk melihat komposisi persediaan berdasarkan barang.

4. Korelasi:
Hitung korelasi antara data penjualan dan persediaan.
Korelasi dapat memberikan informasi tentang seberapa erat hubungan antara kedua variabel.
Anda dapat menggunakan fungsi corr() pada DataFrame untuk menghitung korelasi.

5. Analisis Regresi (Opsional):
Jika Anda ingin memahami bagaimana penjualan dipengaruhi oleh persediaan, Anda dapat melakukan analisis regresi.
Regresi linier sederhana atau regresi berganda dapat memberikan gambaran tentang hubungan antara penjualan dan persediaan.
Gunakan library seperti scikit-learn untuk melakukan analisis regresi.

6. Analisis Skewness:
Hitung skewness dari distribusi data penjualan dan persediaan.
Skewness dapat memberikan informasi tentang asimetri distribusi data.
Anda dapat menggunakan fungsi skew() dari scipy.stats untuk menghitung skewness.

7. Heatmap (Opsional):
Jika Anda ingin memvisualisasikan korelasi antara penjualan dan persediaan dengan lebih jelas, Anda bisa menggunakan heatmap.
Heatmap adalah cara yang bagus untuk memvisualisasikan korelasi antara dua variabel numerik.
Anda dapat menggunakan library seaborn untuk membuat heatmap.

**VISUALISASI DATA**
![bar chart](https://github.com/maelangkey/Tugas-Pengkodean-PraUAS-Adinda/assets/166582618/222ebb50-0884-4a78-9ade-b32550e25ea3)
![scatter plot](https://github.com/maelangkey/Tugas-Pengkodean-PraUAS-Adinda/assets/166582618/85349daf-deda-49da-8e12-76e92e90de6c)
![pie chart](https://github.com/maelangkey/Tugas-Pengkodean-PraUAS-Adinda/assets/166582618/6c0b2a57-b50d-4023-ac23-0634a16502bc)
![histogram](https://github.com/maelangkey/Tugas-Pengkodean-PraUAS-Adinda/assets/166582618/0b936a91-0887-454b-87df-87beb3b14d5b)

**ANALISIS REGRESI 1**
1. Visualisasi Data:
Dalam plot yang dihasilkan, kita dapat melihat titik-titik data (ditampilkan dalam warna biru) yang mewakili hubungan antara produksi dan penjualan. Garis merah adalah garis regresi linier yang menunjukkan hubungan prediksi antara kedua variabel. Kita bisa melihat bahwa garis regresi cenderung mengikuti arah umum titik-titik data, meskipun ada variasi di sekitar garis.

2. Interpretasi Model:
Model regresi linier digunakan untuk memprediksi penjualan berdasarkan produksi. Model ini mengasumsikan bahwa penjualan dapat dijelaskan secara linear oleh produksi.
Garis regresi linier yang dihasilkan oleh model adalah representasi matematis dari hubungan antara produksi dan penjualan. Misalnya, jika produksi suatu barang naik sebesar satu unit, model memprediksi bahwa penjualan akan meningkat sebesar koefisien regresi yang diperoleh dari model.

3. Evaluasi Model:
Evaluasi model dilakukan menggunakan Mean Squared Error (MSE), yang merupakan metrik untuk mengukur seberapa baik model regresi linier memprediksi nilai penjualan berdasarkan produksi.
Semakin rendah nilai MSE, semakin baik model dalam memprediksi penjualan. Nilai MSE yang rendah menunjukkan bahwa prediksi model cenderung mendekati nilai sebenarnya dari data uji.
Dalam kasus ini, nilai MSE yang dihasilkan dapat digunakan untuk mengevaluasi kinerja model. Semakin rendah nilainya, semakin baik modelnya.

![analisis regresi 1](https://github.com/maelangkey/Tugas-Pengkodean-PraUAS-Adinda/assets/166582618/6f69f270-1435-4fd6-a6d3-b71453d09bc7)

**ANALISIS REGRESI 2**
1. Visualisasi Data dan Model Regresi:
Pada plot yang dihasilkan, titik-titik biru menunjukkan data aktual penjualan sepanjang rentang waktu yang diamati.
Garis merah adalah garis regresi linier yang menunjukkan tren umum hubungan antara tanggal (waktu) dan jumlah penjualan berdasarkan data yang diamati.
Titik-titik hijau menunjukkan prediksi jumlah penjualan untuk 5 bulan ke depan berdasarkan model regresi.

2. Interpretasi Model:
Model regresi linier digunakan untuk memprediksi jumlah penjualan berdasarkan tanggal (waktu).
Garis regresi linier adalah representasi matematis dari hubungan antara tanggal dan jumlah penjualan. Dalam konteks ini, garis regresi menunjukkan tren umum penjualan seiring berjalannya waktu.

3. Prediksi untuk 5 Bulan ke Depan:
Titik-titik hijau pada plot adalah hasil prediksi jumlah penjualan untuk 5 bulan ke depan berdasarkan model regresi.
Prediksi ini dapat digunakan untuk membuat perkiraan tentang kinerja penjualan di masa mendatang, dengan asumsi bahwa tren yang diamati dalam data historis akan terus berlanjut.

4. Kesimpulan:
Dengan menggunakan model regresi linier, kita dapat membuat perkiraan tentang jumlah penjualan barang untuk beberapa bulan ke depan berdasarkan data historis.
Namun, penting untuk diingat bahwa prediksi ini didasarkan pada asumsi bahwa tren yang diamati dalam data historis akan berlanjut ke masa depan. Perubahan dalam faktor-faktor eksternal atau kondisi pasar dapat mempengaruhi akurasi prediksi ini. Oleh karena itu, disarankan untuk memperbarui model secara berkala dengan data baru untuk meningkatkan akurasi prediksi.

![analisis regresi 2](https://github.com/maelangkey/Tugas-Pengkodean-PraUAS-Adinda/assets/166582618/ba8fe748-9559-4795-b612-7ea84bab2d52)

**ANALISIS STATISTIK HEATMAP**
1. Heatmap Korelasi:
Heatmap menampilkan matriks korelasi antara variabel produksi dan penjualan.
Setiap sel pada heatmap menunjukkan korelasi antara dua variabel. Nilai korelasi berkisar dari -1 hingga 1, di mana:
Nilai positif menunjukkan korelasi positif, artinya kedua variabel bergerak ke arah yang sama.
Nilai negatif menunjukkan korelasi negatif, artinya kedua variabel bergerak ke arah yang berlawanan.
Nilai mendekati 0 menunjukkan korelasi yang lemah atau tidak ada korelasi.
Anotasi pada heatmap menunjukkan nilai korelasi untuk setiap pasangan variabel.

2. Interpretasi Korelasi:
Korelasi antara produksi dan penjualan diperoleh dari heatmap. Nilai korelasi mengindikasikan seberapa kuat hubungan antara kedua variabel.
Jika korelasi mendekati 1, itu menunjukkan hubungan positif yang kuat antara produksi dan penjualan. Artinya, semakin tinggi produksi, semakin tinggi juga penjualan, dan sebaliknya.
Jika korelasi mendekati -1, itu menunjukkan hubungan negatif yang kuat. Namun, dalam konteks produksi dan penjualan, kita biasanya mengharapkan korelasi positif.

3. Kesimpulan:
Dari heatmap, kita dapat melihat seberapa erat hubungan antara produksi dan penjualan.
Jika korelasi positif dan kuat, ini menunjukkan bahwa peningkatan produksi cenderung menghasilkan peningkatan penjualan, yang merupakan hasil yang diharapkan dalam bisnis.
Namun, jika korelasi lemah atau tidak ada korelasi, ini menunjukkan bahwa ada faktor lain yang memengaruhi penjualan selain produksi, dan perlu untuk menyelidiki faktor-faktor tersebut lebih lanjut untuk meningkatkan kinerja penjualan.

![analisis statistik heatmap](https://github.com/maelangkey/Tugas-Pengkodean-PraUAS-Adinda/assets/166582618/856866cc-30ad-4cb8-8a1e-9bac051c3fc9)

**ANALISIS STATISTIK SKEWNESS**
1. Skewness Residu:
Skewness adalah ukuran statistik yang mengukur asimetri distribusi data.
Nilai skewness dari residu menunjukkan seberapa simetris distribusi residu regresi.
Jika nilai skewness mendekati 0, itu menunjukkan bahwa distribusi residu hampir simetris.
Jika nilai skewness positif, itu menunjukkan adanya ekor panjang di sebelah kanan distribusi, sedangkan jika negatif, itu menunjukkan adanya ekor panjang di sebelah kiri distribusi.

2.Interpretasi Skewness:
Dalam kasus ini, nilai skewness residu menunjukkan seberapa simetris distribusi residu regresi.
Jika skewness mendekati 0, distribusi residu hampir simetris, yang menandakan bahwa model regresi berhasil menangkap pola dalam data dan residu tersebar secara merata di sekitar garis regresi.
Jika skewness positif atau negatif, ini menunjukkan adanya ketidakseimbangan dalam distribusi residu. Skewness yang signifikan dapat menunjukkan bahwa model mungkin tidak sesuai dengan data dengan baik, dan mungkin ada pola yang tidak terdeteksi oleh model.

3. Plot Residu:
Plot residu menunjukkan hubungan antara jumlah produksi dan residu dari model regresi.
Garis merah pada plot adalah garis referensi pada nilai nol, menunjukkan titik di mana residu adalah nol.
Jika residu tersebar secara merata di sekitar garis referensi, ini menunjukkan bahwa model regresi memprediksi penjualan dengan baik.
Namun, jika ada pola atau struktur yang terlihat dalam plot residu, ini dapat menunjukkan adanya pola dalam data yang tidak ditangkap oleh model regresi.

![analisis statistik skewness](https://github.com/maelangkey/Tugas-Pengkodean-PraUAS-Adinda/assets/166582618/6fa46ed4-77ad-45e0-a669-b3f21760612f)
