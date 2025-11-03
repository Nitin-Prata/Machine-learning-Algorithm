import os
import matplotlib.pyplot as plt
from kmeans import KMeans
import pandas as pd

# Use a repository-relative path to the example dataset (safer than absolute path)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_path = os.path.join(BASE_DIR, "DataSets", "student_clustering.csv")

df = pd.read_csv(data_path)
X = df.iloc[:, :].values

km = KMeans(n_clusters=4, max_iter=500)
y_means = km.fit_predict(X)

plt.scatter(X[y_means == 0, 0], X[y_means == 0, 1], color="red")
plt.scatter(X[y_means == 1, 0], X[y_means == 1, 1], color="blue")
plt.scatter(X[y_means == 2, 0], X[y_means == 2, 1], color="green")
plt.scatter(X[y_means == 3, 0], X[y_means == 3, 1], color="yellow")
plt.show()
