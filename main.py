import matplotlib.pyplot as plt
import pandas
from pandas import DataFrame
import tensorflow
data = pandas.read_csv("cost_revenue_clean.csv")
print(data.describe())
x = DataFrame(data, columns=['production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.3)
plt.title("Film cost vs Global revenue")
plt.xlabel('Production Budget $')
plt.ylabel('Worldwide Gross $')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()

for i in range(0, 100):
    print(i)
