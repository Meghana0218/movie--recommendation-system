import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD

from web.models import Myrating

def generate_recommendations(user_id, num_recommendations=5):
    ratings = Myrating.objects.all().values()
    ratings_df = pd.DataFrame(ratings)
    if ratings_df.empty:
        return []
    user_movie_matrix = ratings_df.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
    user_mean_ratings = user_movie_matrix.mean(axis=1)
    normalized_matrix = user_movie_matrix.sub(user_mean_ratings, axis=0)
    svd = TruncatedSVD(n_components=20)
    reduced_matrix = svd.fit_transform(normalized_matrix)
    similarity_matrix = cosine_similarity(reduced_matrix)
    similarity_df = pd.DataFrame(similarity_matrix, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    similar_users = similarity_df[user_id].sort_values(ascending=False).index[1:]
    recommendation_scores = {}
    for similar_user in similar_users:
        similar_user_ratings = user_movie_matrix.loc[similar_user]
        for movie_id, rating in similar_user_ratings.items():
            if user_movie_matrix.loc[user_id, movie_id] == 0:
                if movie_id not in recommendation_scores:
                    recommendation_scores[movie_id] = 0
                recommendation_scores[movie_id] += rating
    recommended_movies = sorted(recommendation_scores.items(), key=lambda x: x[1], reverse=True)
    recommended_movie_ids = [movie_id for movie_id, _ in recommended_movies[:num_recommendations]]
    return recommended_movie_ids
