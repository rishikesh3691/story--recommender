
from recommender.story__recommender import StoryRecommender

def main():
    recommender = StoryRecommender("data/storys.csv")
    print("Recommendations for genre='Fantasy', min_rating=8.5:")
    print(recommender.recommend(genre='Fantasy', min_rating=8.5))

if __name__ == "__main__":
    main()
