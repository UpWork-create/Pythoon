import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster._bicluster import SpectralCoclustering

data = pd.read_csv('whisky.txt')
pd.set_option('display.max_rows', 100)
data['Region'] = pd.read_csv('regions.txt')  # Adding extra col

flavours = data.iloc[:, 2:13]

corr_flavours = pd.DataFrame.corr(flavours)
corr_whisky = pd.DataFrame.corr(flavours.transpose())

model = SpectralCoclustering(n_clusters=6, random_state=0)
cluster = model.fit(corr_whisky)

data['Group'] = pd.Series(model.row_labels_, index=data.index)

data = data.iloc[np.argsort(model.row_labels_)]

data.reset_index(drop=True, inplace=True)

corrs = pd.DataFrame.corr(data.iloc[:, 2:13].transpose())
corrs = np.array(corrs)

plt.figure(figsize=(14, 7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title('Original')
plt.axis('tight')

plt.subplot(122)
plt.pcolor(corrs)
plt.title('Sorted')
plt.axis('tight')

plt.savefig('whisky_correlation.pdf')
