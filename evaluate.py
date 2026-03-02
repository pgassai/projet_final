import pandas as pd
from sklearn.manifold import trustworthiness

city_lifestyle = pd.read_csv('data/city_lifestyle_dataset.csv')

pca_emb = pd.read_csv('outputs/pca_emb_2d.csv')
tsne_emb = pd.read_csv('outputs/tsne_emb_2d.csv')
umap_emb = pd.read_csv('outputs/umap_emb_2d.csv')


score_pca = trustworthiness(city_lifestyle.select_dtypes(include='number'), pca_emb.select_dtypes(include='number'), n_neighbors=10)
score_tsne = trustworthiness(city_lifestyle.select_dtypes(include='number'), tsne_emb.select_dtypes(include='number'), n_neighbors=10)
score_umap = trustworthiness(city_lifestyle.select_dtypes(include='number'), umap_emb.select_dtypes(include='number'), n_neighbors=10)

print("Trustworthiness PCA:", round(score_pca,3))
print("Trustworthiness t-SNE:", round(score_tsne,3))
print("Trustworthiness UMAP:", round(score_umap,3))
