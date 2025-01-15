import cleanData
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

salary_data = cleanData.DataFrame("Salary_Data.csv")
salary_data.removeNullValues()
salary_data.removeDuplicateCategories()
salary_data.convertCategoricalToNumeric()

corr = salary_data.df.corr()
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(corr, cmap='coolwarm')
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=90)
ax.set_yticklabels(corr.columns)
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax.text(j, i, "{:.2f}".format(corr.iloc[i, j]), ha="center", va="center", color="w")
plt.colorbar(im)
plt.savefig("correlation.png")


salary_data.df.plot.scatter(x='Years of Experience', y='Salary')
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.savefig("salary_exp.png")

