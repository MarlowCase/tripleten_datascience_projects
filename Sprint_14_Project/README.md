# Introduction
The Film Junky Union, a new edgy community for classic movie enthusiasts, is developing a system to automatically categorize movie reviews, helping classic movie enthusiasts quickly identify and engage with diverse perspective on their beloved films.

# Project Objective
To build a high-performing classification model that accurately detects negative reviews **with an F1 score of at least 0.85,** enhancing the community's content moderation and streamlining the review filtering process. 

# Data

*The data was provided by Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011). **Learning Word Vectors for Sentiment Analysis.** The 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011).*

*Description of the data*

- `tconst`: A unique identifier for each title; links each entry to a specific movie, show, or episode.
- `title_type`: The type or category indicating the kind of media. (_movie, short, tvSeries, tvEpisode, etc_)
- `primary_title`: The main or common title of the media as it is generally known or advertised.
- `original_title`: The original title of the media.
- `start_year`: The year the media was first released or aired.
- `end_year`: For TV series, the year the media ended, or year of final airing.
- `runtime_minutes`: The duration of the media in minutes. Total runtime for movies, or average episode runtime for TV series.
- `is_adult`: Flag field indicating if the media is intended for adult audiences (e.g., rated 18+). 1 means yes.
- `genres`: The genre associated with the media entry.
- `average_rating`: The average user rating for the title on a scale from 1-10.
- `votes`: The total number of votes, or user reviews, submitted by users for this title.
- `rating`: The rating given to the media by the user during review.
- `sp`: Sentiment polarity; essentially a string-flag indicator for positive or negative review
- `ds_part`: Specifies the data split, such as "train" or "test". Used for splitting the data.
- `idx`: An identifier for the data point in the dataset.

*Features:*
- `review`: The text of a user review for the media.
 
*Target:*
- `pos`: Represents the sentiment polarity as an integer for positive reviews. 1 means positive review.

# Main Libraries Used
Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, LightGBM, PyTorch, NLTK, SpaCy, Transformers

# Table of Contents
1. Introduction
    - Imports & Initializations 
2. Data Exploration & Preprocessing
3. Exploratory Data Analysis
    - Number of Movies & Reviews per Year
    - Distribution of Number of Reviews per Movie
    - Top 10 Genres
    - Rating Distribution Comparison: Train vs. Test 
    - Number of Reviews Distribution Comparison: Train vs. Test
    - Distribution of Target Classes
4. Model Preparation
    - Normalization
    - Dataset Segmentation
5. Model Development
    - Model 0 - Constant
    - Model 1 - NLTK, TF-IDF, and LogR
    - Model 2 - NLTK, TF-IDF, and LGBM
    - Model 3 - spaCy, TF-IDF, and LogR
    - Model 4 - spaCy, TF-IDF, and LGBM
    - Model 5 - BERT LogR
    - Model 6 - BERT LGBM
    - Final Results
6. Custom Reviews
7. Conclusion
8. Appendix A: Saving Models