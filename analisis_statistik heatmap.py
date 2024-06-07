import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data produksi
produksi_data = {
    'Barang': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Jumlah_Produksi': [100, 150, 200, 180, 220, 120, 90, 210, 160, 190]
}

# Data penjualan
penjualan_data = {
    'Barang': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Jumlah_Penjualan': [80, 120, 150, 100, 180, 70, 60, 200, 130, 170]
}

# Membuat DataFrame dari data produksi dan penjualan
df_produksi = pd.DataFrame(produksi_data)
df_penjualan = pd.DataFrame(penjualan_data)

# Menggabungkan kedua DataFrames berdasarkan kolom 'Barang'
df_merged = pd.merge(df_produksi, df_penjualan, on='Barang')

# Menghitung korelasi antara produksi dan penjualan
correlation = df_merged['Jumlah_Produksi'].corr(df_merged['Jumlah_Penjualan'])

# Membuang kolom 'Barang' sebelum menghitung korelasi
df_for_corr = df_merged.drop(columns=['Barang'])

# Membuat heatmap
sns.heatmap(df_for_corr.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap Hubungan antara Produksi dan Penjualan\nKorelasi: {:.2f}'.format(correlation))
plt.show()
