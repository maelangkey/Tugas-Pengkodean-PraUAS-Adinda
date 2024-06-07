import pandas as pd
import numpy as np
from scipy.stats import skew
from sklearn.linear_model import LinearRegression
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

# Fitting regresi linier
X = df_produksi['Jumlah_Produksi'].values.reshape(-1, 1)
y = df_penjualan['Jumlah_Penjualan'].values
model = LinearRegression().fit(X, y)

# Prediksi nilai penjualan berdasarkan model regresi
y_pred = model.predict(X)

# Menghitung residu
residuals = y - y_pred

# Menghitung skewness dari residu
skewness_residuals = skew(residuals)
print("Skewness dari residu:", skewness_residuals)

# Plot residu
plt.scatter(df_produksi['Jumlah_Produksi'], residuals)
plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel('Jumlah Produksi')
plt.ylabel('Residu')
plt.title('Plot Residu dan Skewness: {:.2f}'.format(skewness_residuals))
plt.grid(True)
plt.show()
