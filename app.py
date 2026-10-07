# ============================================================
# BOOK RECOMMENDATION SYSTEM
# User-Based Collaborative Filtering
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# LOAD MODEL FILES
# ============================================================

@st.cache_resource
def load_model():

    with open("user_book_sparse.pkl", "rb") as file:
        user_book_sparse = pickle.load(file)

    with open("user_similarity.pkl", "rb") as file:
        user_similarity = pickle.load(file)

    with open("user_index.pkl", "rb") as file:
        user_index = pickle.load(file)

    with open("book_index.pkl", "rb") as file:
        book_index = pickle.load(file)

    books_model = pd.read_pickle("books_model.pkl")

    return (
        user_book_sparse,
        user_similarity,
        user_index,
        book_index,
        books_model
    )


# Load model artifacts
(
    user_book_sparse,
    user_similarity,
    user_index,
    book_index,
    books_model
) = load_model()


# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

def recommend_books(user_id, n=10):

    # Check whether user exists
    if user_id not in user_index:

        return pd.DataFrame(
            columns=[
                "ISBN",
                "Book-Title",
                "Book-Author",
                "Average_Rating",
                "Score"
            ]
        )

    # --------------------------------------------------------
    # Step 1: Get target user's position
    # --------------------------------------------------------

    user_position = user_index.get_loc(user_id)

    # --------------------------------------------------------
    # Step 2: Get similarity scores
    # --------------------------------------------------------

    similarity_scores = (
        user_similarity[user_position]
        .toarray()
        .flatten()
    )

    # --------------------------------------------------------
    # Step 3: Find similar users
    # --------------------------------------------------------

    similar_users = np.argsort(
        similarity_scores
    )[::-1]

    # Remove target user
    similar_users = similar_users[
        similar_users != user_position
    ]

    # Select top 20 similar users
    similar_users = similar_users[:20]

    # --------------------------------------------------------
    # Step 4: Calculate recommendation scores
    # --------------------------------------------------------

    scores = np.zeros(len(book_index))

    for u in similar_users:

        similarity = similarity_scores[u]

        # Ignore zero or negative similarity
        if similarity <= 0:
            continue

        user_ratings = (
            user_book_sparse[u]
            .toarray()
            .flatten()
        )

        scores += similarity * user_ratings

    # --------------------------------------------------------
    # Step 5: Remove books already rated by the user
    # --------------------------------------------------------

    current_ratings = (
        user_book_sparse[user_position]
        .toarray()
        .flatten()
    )

    scores[current_ratings > 0] = -1

    # --------------------------------------------------------
    # Step 6: Select Top-N books
    # --------------------------------------------------------

    top_books = np.argsort(
        scores
    )[::-1][:n]

    # --------------------------------------------------------
    # Step 7: Create recommendation result
    # --------------------------------------------------------

    result = pd.DataFrame({
        "ISBN": book_index[top_books],
        "Score": scores[top_books]
    })

    # --------------------------------------------------------
    # Step 8: Add book information
    # --------------------------------------------------------

    result = result.merge(
        books_model[
            [
                "ISBN",
                "Book-Title",
                "Book-Author",
                "Average_Rating"
            ]
        ],
        on="ISBN",
        how="left"
    )

    # --------------------------------------------------------
    # Step 9: Return required columns
    # --------------------------------------------------------

    return result[
        [
            "ISBN",
            "Book-Title",
            "Book-Author",
            "Average_Rating",
            "Score"
        ]
    ]


# ============================================================
# STREAMLIT USER INTERFACE
# ============================================================

st.title("📚 Book Recommendation System")

st.write(
    "Get personalized book recommendations "
    "using User-Based Collaborative Filtering."
)


# ============================================================
# SIDEBAR - RECOMMENDATION SETTINGS
# ============================================================

st.sidebar.header("⚙️ Recommendation Settings")

user_id = st.sidebar.number_input(
    "Enter User ID",
    min_value=1,
    step=1,
    value=195079
)

number_of_books = st.sidebar.slider(
    "Number of Recommendations",
    min_value=5,
    max_value=20,
    value=10
)


# ============================================================
# RECOMMEND BUTTON
# ============================================================

if st.sidebar.button("📚 Get Recommendations"):

    recommendations = recommend_books(
        user_id,
        number_of_books
    )

    # --------------------------------------------------------
    # Invalid User
    # --------------------------------------------------------

    if recommendations.empty:

        st.error(
            "User ID not found in the trained model. "
            "Please enter a valid User ID."
        )

    # --------------------------------------------------------
    # Display Recommendations
    # --------------------------------------------------------

    else:

        st.success(
            f"Recommendations generated for User ID: {user_id}"
        )

        st.subheader("📖 Recommended Books")

        # Create display copy
        display_result = recommendations.copy()

        # Recommendation number
        display_result.index = range(
            1,
            len(display_result) + 1
        )

        # Rename columns for user-friendly display
        display_result.columns = [
            "ISBN",
            "Book Title",
            "Author",
            "Average Rating",
            "Recommendation Score"
        ]

        # Display recommendation table
        st.dataframe(
            display_result,
            use_container_width=True
        )


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.sidebar.markdown("---")

st.sidebar.write(
    "**Model:** User-Based Collaborative Filtering"
)

st.sidebar.write(
    "**Recommendation Method:** Similar User Ratings"
)

st.sidebar.write(
    "**Recommendation Type:** Personalized Top-N Books"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Developed by PALSA MANOJ KUMAR | "
    "Book Recommendation System"
)