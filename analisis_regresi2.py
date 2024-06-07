import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Data
dates = pd.date_range(start='2022-01-01', end='2022-06-10', freq='D')  # Extend the date range
produksi_data = {
    'Tanggal': dates,
    'Barang': ['A'] * len(dates),  # Assume constant production for simplicity
    'Jumlah_Produksi': np.random.randint(100, 250, size=len(dates))  # Random production values
}

penjualan_data = {
    'Tanggal': dates,
    'Barang': ['A'] * len(dates),  # Assume constant sales for simplicity
    'Jumlah_Penjualan': np.random.randint(50, 200, size=len(dates))  # Random sales values
}

# Creating DataFrames
df_produksi = pd.DataFrame(produksi_data)
df_penjualan = pd.DataFrame(penjualan_data)

# Dropping NaN values for regression analysis
df_produksi.dropna(inplace=True)
df_penjualan.dropna(inplace=True)

# Check if we have enough data for regression
if len(df_produksi) < 2:
    print("Insufficient data for regression analysis.")
else:
    # Reshaping data for regression
    X = df_produksi['Tanggal'].values.astype(int).reshape(-1, 1)
    y = df_penjualan['Jumlah_Penjualan'].values

    # Fitting regression model
    model = LinearRegression()
    model.fit(X, y)

    # Generating next 5 months for prediction
    next_dates = pd.date_range(start='2022-06-11', periods=5, freq='MS')
    next_dates_int = next_dates.values.astype(int).reshape(-1, 1)
    predictions = model.predict(next_dates_int)

    # Plotting the results
    plt.scatter(df_produksi['Tanggal'], df_penjualan['Jumlah_Penjualan'], label='Actual Penjualan')
    plt.plot(df_produksi['Tanggal'], model.predict(X), color='red', label='Regression Line')
    plt.scatter(next_dates, predictions, color='green', label='Predicted Penjualan (Next 5 Months)')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Penjualan')
    plt.title('Regression Analysis for Next 5 Months')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
