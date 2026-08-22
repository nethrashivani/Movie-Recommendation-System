# Movie Recommendation System

A content-based movie recommendation system built with Python and Streamlit that recommends the **5 most similar movies** based on a movie selected by the user.

## Overview

This project uses **cosine similarity** to identify movies that are most similar to the user's selected movie.

The application compares the feature representation of the selected movie with the representations of other movies in the dataset. The movies with the highest cosine similarity scores are returned as recommendations.

For example, if a user selects a particular movie, the system calculates how similar that movie is to every other movie and displays the **top 5 most similar movies**.

## How It Works

The recommendation process follows these steps:

1. The movie dataset is processed to create a numerical representation of each movie.
2. Each movie is represented as a feature vector based on its available movie information.
3. When the user selects a movie, its vector is compared with the vectors of other movies.
4. **Cosine similarity** is used to measure the similarity between the movies.
5. The movies are ranked based on their similarity scores.
6. The system displays the **5 highest-scoring movies** as recommendations.

### Why Cosine Similarity?

Cosine similarity measures the angle between two vectors rather than their absolute size.

A score closer to **1** indicates that two movie vectors are highly similar, while a score closer to **0** indicates lower similarity.

This makes cosine similarity useful for comparing movie feature representations.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Jupyter Notebook

## Project Structure

```text
Movie-Recommendation-System/
│
├── MovieRecommender.ipynb   # Data processing and recommendation logic
├── app.py                   # Streamlit web application
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/nethrashivani/Movie-Recommendation-System.git
```

Navigate into the project:

```bash
cd Movie-Recommendation-System
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Project Highlights

* Built a content-based movie recommendation system.
* Implemented movie similarity using cosine similarity.
* Generates the top 5 movie recommendations for a selected movie.
* Developed an interactive interface using Streamlit.
* Used Python-based data processing and machine learning libraries.

## Future Improvements

* Add movie posters and additional movie information.
* Improve recommendations using multiple movie attributes.
* Add genre-based filtering.
* Allow users to rate movies and personalize recommendations.
* Explore collaborative filtering and hybrid recommendation techniques.
