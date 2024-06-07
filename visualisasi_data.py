import matplotlib.pyplot as plt
import pandas as pd

# Data
dates = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
produksi_data = {
    'Tanggal': dates,
    'Barang': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Jumlah_Produksi': [100, 150, 200, 180, 220, 120, 90, 210, 160, 190]
}

penjualan_data = {
    'Tanggal': dates,
    'Barang': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Jumlah_Penjualan': [80, 120, 150, 100, 180, 70, 60, 200, 130, 170]
}

persediaan_data = {
    'Tanggal': dates,
    'Barang': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Jumlah_Persediaan': [20, 30, 50, 80, 40, 50, 30, 10, 30, 20]
}

# Membuat DataFrame dari data
df_produksi = pd.DataFrame(produksi_data)
df_penjualan = pd.DataFrame(penjualan_data)
df_persediaan = pd.DataFrame(persediaan_data)

# Scatter plot
plt.scatter(df_produksi['Tanggal'], df_penjualan['Jumlah_Penjualan'])
plt.title('Scatter Plot Produksi vs Penjualan')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penjualan')
plt.xticks(rotation=45)
plt.show()

# Histogram
plt.hist(df_produksi['Tanggal'], bins=5, alpha=0.5, label='Produksi')
plt.hist(df_penjualan['Tanggal'], bins=5, alpha=0.5, label='Penjualan')
plt.title('Histogram Produksi vs Penjualan')
plt.xlabel('Tanggal')
plt.ylabel('Frekuensi')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Pie chart
plt.pie(df_persediaan['Jumlah_Persediaan'], labels=df_persediaan['Barang'], autopct='%1.1f%%')
plt.title('Persentase Persediaan Barang')
plt.axis('equal')
plt.show()

# Bar chart
plt.bar(df_produksi['Tanggal'], df_produksi['Jumlah_Produksi'], label='Produksi')
plt.bar(df_penjualan['Tanggal'], df_penjualan['Jumlah_Penjualan'], label='Penjualan')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah')
plt.title('Bar Chart Produksi vs Penjualan')
plt.xticks(rotation=45)
plt.legend()
plt.show()
