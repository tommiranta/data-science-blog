import matplotlib.pyplot as plt
import seaborn as sns

dataset.index = ['PC1', 'PC2']
plt.figure(figsize=(8, 2))
plt.xticks(rotation=45)
data = dataset.loc['PC1', :].to_frame().sort_values(by='PC1').transpose()
sns.heatmap(data,
            cmap='plasma',
            square=True,
            annot=True,
            cbar=False,
            yticklabels='')
plt.show()
