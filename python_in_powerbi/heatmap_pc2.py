import matplotlib.pyplot as plt
import seaborn as sns

dataset.index = ['PC1', 'PC2']
plt.figure(figsize=(2, 8))
data = dataset.loc['PC2', :].to_frame().sort_values(by='PC2', ascending=False)
sns.heatmap(data,
            cmap='plasma',
            square=True,
            annot=True,
            cbar=False,
            xticklabels='')
plt.show()
