import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Data
produksi = np.array([100, 150, 200, 180, 220, 120, 90, 210, 160, 190]).reshape(-1, 1)  # Produksi
penjualan = np.array([80, 120, 150, 100, 180, 70, 60, 200, 130, 170])  # Penjualan

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(produksi, penjualan, test_size=0.2, random_state=42)

# Membuat model regresi linier
model = LinearRegression()
model.fit(X_train, y_train)

# Memprediksi penjualan berdasarkan produksi
prediksi_penjualan = model.predict(X_test)

# Plot data dan garis regresi
plt.scatter(produksi, penjualan, color='blue', label='Data')
plt.plot(produksi, model.predict(produksi), color='red', label='Regresi Linier')
plt.xlabel('Produksi')
plt.ylabel('Penjualan')
plt.title('Analisis Regresi Linier Produksi vs Penjualan')
plt.legend()
plt.show()

# Evaluasi model
mse = mean_squared_error(y_test, prediksi_penjualan)
print(f"Mean Squared Error: {mse}")
