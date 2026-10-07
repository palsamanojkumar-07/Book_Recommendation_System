# 📚 Book Recommendation System

## 🔗 Project Links

🌐 **Live Streamlit Application:** https://bookrecommendationsystem07.streamlit.app/

💻 **GitHub Repository:** https://github.com/palsamanojkumar-07/Book_Recommendation_System

📓 **Jupyter Notebook:** `Book Recommendation System.ipynb`


## Project Overview

The **Book Recommendation System** is a machine learning project
designed to provide personalized book recommendations based on
historical user-book rating interactions.

The project uses **User-Based Collaborative Filtering** as the final
recommendation approach. The system identifies users with similar rating
patterns and recommends books that similar users have rated, while
excluding books already rated by the target user.

The recommendation system is deployed as an interactive **Streamlit**
application.

------------------------------------------------------------------------

## 🎯 Business Objective

Develop a personalized book recommendation system that uses historical
user-book interactions and engineered book features to recommend
relevant books to users.

------------------------------------------------------------------------

## 📊 Dataset

The project uses three datasets:

### 1. Books Dataset

Contains book-related information such as:

-   ISBN
-   Book Title
-   Book Author
-   Publisher
-   Publication information
-   Image URLs

### 2. Users Dataset

Contains:

-   User ID
-   Location
-   Age

### 3. Ratings Dataset

Contains:

-   User ID
-   ISBN
-   Book Rating

Ratings include both:

-   **Explicit ratings** --- ratings from 1 to 10
-   **Implicit interactions** --- rating value 0

------------------------------------------------------------------------

## 🔍 Exploratory Data Analysis

The project includes analysis of:

-   Book rating distribution
-   Explicit vs. implicit ratings
-   Most-rated books
-   Most active users
-   User age distribution
-   Top authors by number of books
-   Dataset missing values
-   Duplicate records
-   Rating statistics
-   Interaction sparsity

### Key EDA Observations

-   The dataset contains a large number of user-book interactions.
-   Implicit interactions are more numerous than explicit ratings.
-   A relatively small number of books receive a large number of
    ratings.
-   User activity varies considerably across users.
-   Some user age values require cleaning before analysis.
-   The interaction matrix is highly sparse, which is common in
    recommendation systems.

------------------------------------------------------------------------

## 🛠️ Data Preprocessing

The preprocessing workflow includes:

1.  Loading the Books, Users, and Ratings datasets.
2.  Checking dataset dimensions and data types.
3.  Identifying missing values.
4.  Checking duplicate records.
5.  Separating explicit ratings from implicit interactions.
6.  Cleaning unrealistic age values.
7.  Handling missing age values.
8.  Creating book-level rating features.
9.  Preparing user-book interaction data.
10. Creating training and testing datasets.

------------------------------------------------------------------------

## ⚙️ Feature Engineering

The project creates the following book-level features:

-   `Average_Rating`
-   `Rating_Count`

A combined text feature is also created from:

-   Book Title
-   Book Author
-   Publisher

This feature is used by the content-based recommendation approach
evaluated during the project.

------------------------------------------------------------------------

## 🤖 Recommendation Models

Six recommendation approaches were developed and evaluated:

### 1. Popularity-Based Recommendation

Recommends books based on their rating popularity.

### 2. Content-Based Recommendation

Uses TF-IDF features and cosine similarity to identify books with
similar textual information.

### 3. User-Based Collaborative Filtering

Identifies users with similar rating patterns and uses their ratings to
generate personalized recommendations.

### 4. Item-Based Collaborative Filtering

Identifies books with similar user-rating patterns and recommends
similar items.

### 5. SVD Matrix Factorization

Uses matrix factorization to learn latent user and book representations.

### 6. Hybrid Recommendation

Combines content-based and collaborative filtering information.

------------------------------------------------------------------------

## 📈 Model Evaluation

The recommendation models were evaluated using:

-   Precision@10
-   Recall@10
-   F1@10
-   Hit Rate@10

The evaluation results were compared across the recommendation
approaches.

Based on the evaluation results obtained in this experiment,
**User-Based Collaborative Filtering** was selected as the final model.

> Note: The evaluation populations differ between some models because
> each approach operates on the users/items for which the required
> recommendation information was available.

------------------------------------------------------------------------

## ⭐ Final Model: User-Based Collaborative Filtering

The final recommendation workflow is:

``` text
User ID
   ↓
Find Target User
   ↓
Calculate User Similarities
   ↓
Select Similar Users
   ↓
Collect Ratings from Similar Users
   ↓
Calculate Weighted Recommendation Scores
   ↓
Remove Books Already Rated
   ↓
Select Top-N Books
   ↓
Display Book Details
```

The application uses the top similar users to calculate weighted
recommendation scores and returns books that the target user has not
already rated.

------------------------------------------------------------------------

## 🚀 Streamlit Deployment

The project is deployed using Streamlit.

### Application Features

The application allows the user to:

1.  Enter a User ID.
2.  Select the number of recommendations.
3.  Generate personalized recommendations.
4.  View recommended book titles.
5.  View authors.
6.  View average ratings.
7.  View recommendation scores.

------------------------------------------------------------------------

## 📁 Project Structure

``` text
Book_Recommendation_System/
│
├── app.py
├── user_book_sparse.pkl
├── user_similarity.pkl
├── user_index.pkl
├── book_index.pkl
├── books_model.pkl
└── README.md
```

### File Description

  File                     Description
  ------------------------ ------------------------------------------
  `app.py`                 Streamlit application
  `user_book_sparse.pkl`   Sparse user-book interaction matrix
  `user_similarity.pkl`    User similarity matrix
  `user_index.pkl`         User ID index mapping
  `book_index.pkl`         Book/ISBN index mapping
  `books_model.pkl`        Book information and engineered features
  `README.md`              Project documentation

------------------------------------------------------------------------

## 💻 Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   SciPy
-   Streamlit
-   Pickle

------------------------------------------------------------------------

## ▶️ How to Run the Application

### Step 1: Clone the Repository

``` bash
git clone <https://github.com/palsamanojkumar-07/Book_Recommendation_System.git>
```

### Step 2: Open the Project Folder

``` bash
cd Book_Recommendation_System
```

### Step 3: Install Required Libraries

``` bash
pip install pandas numpy scikit-learn scipy streamlit
```

### Step 4: Run Streamlit

``` bash
streamlit run app.py
```

The application will open in the browser.

------------------------------------------------------------------------

## 🧪 Example Usage

1.  Open the Streamlit application.
2.  Enter a valid User ID.
3.  Select the number of recommendations.
4.  Click **Get Recommendations**.
5.  Review the personalized Top-N book recommendations.

Example User ID:

``` text
195079
```

------------------------------------------------------------------------

## 📌 Recommendation Output

The application displays:

  -----------------------------------------------------------------------
  Column                              Description
  ----------------------------------- -----------------------------------
  ISBN                                Unique book identifier

  Book Title                          Recommended book title

  Author                              Book author

  Average Rating                      Average rating of the book

  Recommendation Score                Weighted score generated by the
                                      recommendation model
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## ⚠️ Limitations

-   Recommendations depend on available user-book interaction history.
-   New users with insufficient rating history may not receive
    personalized recommendations.
-   Highly sparse interaction data can make similarity-based
    recommendations challenging.
-   Recommendation scores are model-generated scores and are not direct
    book ratings.

------------------------------------------------------------------------

## 🔮 Future Enhancements

Possible future improvements include:

-   Adding a cold-start strategy for new users.
-   Combining user-based and item-based collaborative filtering.
-   Improving hybrid recommendation weighting.
-   Adding book cover images to the Streamlit interface.
-   Adding filtering by author or rating.
-   Improving recommendation explanations.
-   Monitoring recommendation performance after deployment.

------------------------------------------------------------------------

## 👨‍💻 Developed By

**PALSA MANOJ KUMAR**

Book Recommendation System\
Data Science / Machine Learning Project

------------------------------------------------------------------------

## 📚 Project Summary

This project demonstrates how recommendation-system techniques can
transform historical user-book interactions into personalized book
recommendations.

The workflow covers:

**Data Preprocessing → EDA → Feature Engineering → Train/Test Split →
Recommendation Models → Model Evaluation → Final User-Based
Collaborative Filtering Model → Streamlit Deployment**
