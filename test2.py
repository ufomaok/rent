import matplotlib.pyplot as plt
import numpy as np

# Create some example data for multiple histograms
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)

# Create separate subplots for each histogram
plt.figure(figsize=(10, 4))  # Adjust the figure size as needed

# Subplot 1
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.hist(data1, bins=20, alpha=0.5, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram 1')

