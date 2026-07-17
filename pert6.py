import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Produk": ["Laptop", "Mouse", "Keyboard"],
    "Penjualan": [120, 350, 200]
}

df = pd.DataFrame(data)

plt.bar(df["Produk"], df["Penjualan"])

plt.title("Penjualan Produk")
plt.xlabel("Produk")
plt.ylabel("Jumlah")

plt.show()