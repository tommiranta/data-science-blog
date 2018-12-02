import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# utilize the sklearn.datasets package to load the Boston Housing dataset
boston = load_boston()

# scale the data to same value range first since PCA
# is sensitive to the scaling of data
sc = StandardScaler()
X = sc.fit_transform(boston.data)

# create PCA with n_components=2 to allow visualization in 2 dimensions
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# divide data into 5 clusters (refer to .ipynb for motivation)
kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10)
y_kmeans = kmeans.fit_predict(X_pca)

# create pandas dataframe of the housing data for Power BI
columns = np.append(boston.feature_names, ['MEDV', 'PC1', 'PC2', 'CLUSTER'])
data = np.concatenate((boston.data,
                       boston.target.reshape(-1, 1),
                       X_pca,
                       y_kmeans.reshape(-1, 1)),
                      axis=1)
df_housing = pd.DataFrame(data=data, columns=columns)
# we need to convert all columns as string because of different
# decimal separator in Python (.) and Finnish locale (,) that Power BI uses.
# comment out below line if Power BI uses dot as a decimal separator.
df_housing = df_housing.astype('str')

# create pandas dataframe of the pca data for Power BI
columns = np.append(boston.feature_names, ['VARRATIO'])
data = np.concatenate((pca.components_,
                       pca.explained_variance_ratio_.reshape(-1, 1)),
                      axis=1)
df_pca = pd.DataFrame(data=data, columns=columns, index=['PC1', 'PC2'])
df_pca = df_pca.astype('str')

# debug prints
# uncomment below lines and run script to test that everything works.
# print(df_housing.sample(5))
# print(df_pca)
