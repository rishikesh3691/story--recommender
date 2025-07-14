
import pandas as pd

class StoryRecommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def recommend(self, genre=None, min_rating=None):
        result = self.data
        if genre:
            result = result[result['genre'].str.lower() == genre.lower()]
        if min_rating:
            result = result[result['rating'] >= float(min_rating)]
        return result['title'].tolist()
