# Movie Recommendation System 🎥

A **web-based movie recommendation system** that uses **content-based filtering** and **sentiment analysis** to recommend movies and analyze user reviews.

## 🚀 Features
- **Personalized Recommendations**: Recommends movies based on user preferences using content-based filtering.
- **Sentiment Analysis**: Analyzes user reviews scraped from IMDb to determine positive or negative sentiments.
- **Interactive Interface**: A dynamic and responsive web application built with Flask and AJAX.
- **Detailed Movie Information**: Fetches movie details (title, genre, runtime, rating, poster, etc.) via the TMDb API.

## 🛠️ Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (with AJAX)
- **Database**: SQLite
- **Libraries**: BeautifulSoup, NLTK, Scikit-learn, Requests
- **API**: TMDb API

## 📋 How to Run the Project?
# 1. Clone or download this repository to your local machine:
git clone https://github.com/yourusername/Movie-Recommendation-System.git

# 2. Navigate to the project directory:
cd Movie-Recommendation-System

# 3. Install all required libraries:
pip install -r requirements.txt

# 4. Get your TMDb API key:
# - Create an account at TMDb (https://www.themoviedb.org/).
# - Go to your account settings, navigate to the API section, and generate your API key.

# 5. Replace YOUR_API_KEY in the following lines of static/recommend.js:
#    Line 15
#    Line 29

# 6. Run the application:
python main.py

# 7. Open a browser and go to:
http://127.0.0.1:5000/

## 📊 Recommendation Algorithm
# Content-Based Filtering:
# This algorithm recommends movies based on their similarity to a given movie. 
# The similarity is calculated using cosine similarity on movie metadata such as genres, keywords, and descriptions.

# Cosine Similarity Formula:
# Cosine Similarity = (A · B) / (||A|| × ||B||)
# Where A and B are vectors representing the movie features.

# Implementation Example:
# 1. Preprocess movie metadata to create feature vectors.
# 2. Compute cosine similarity between feature vectors.
# 3. Sort movies by similarity scores and recommend the top results.

# Sentiment Analysis:
# User reviews scraped from IMDb are analyzed to determine positive or negative sentiments.
# The analysis uses natural language processing techniques, such as:
# 1. Tokenization
# 2. Stop-word removal
# 3. Polarity scoring with libraries like NLTK or TextBlob.

# Final Recommendations:
# The final recommendations are presented as a combination of:
# 1. Content similarity-based recommendations.
# 2. Sentiment-driven filtering to exclude movies with predominantly negative reviews.

## 📚 Dataset Sources
# The datasets used in this project include:
# - IMDB 5000 Movie Dataset: https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset
# - The Movies Dataset: https://www.kaggle.com/rounakbanik/the-movies-dataset
# - List of American Films (2018–2020)

## 📌 Future Enhancements
# Future plans to improve the system include:
# 1. Adding collaborative filtering to enhance the recommendation engine.
# 2. Improving multi-language support for global audiences.
# 3. Integrating additional APIs (e.g., OMDB) for more comprehensive movie data.
# 4. Deploying the application to platforms like Heroku or AWS for public access.

## 📝 License
# This project is licensed under the MIT License.
# See the LICENSE file



