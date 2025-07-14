
# story--recommender

📖 **Story Recommender**

A simple Python-based story recommendation system that filters stories by genre and minimum rating using a CSV dataset.

## 📂 Dataset

Located in `data/storys.csv`  
It contains the following columns:

- `title` : Title of the story  
- `genre` : Genre of the story (e.g. Fantasy, Thriller, Sci-Fi)  
- `rating` : Story rating (float)

## 💡 How it works

The recommender reads the CSV and returns a list of stories matching:

- A given genre  
- A minimum rating  

---

> Example usage is provided in `main.py`, and the recommendation logic is inside `recommender/story__recommender.py`.
