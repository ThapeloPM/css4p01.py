# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:30:57 2024

@author: Thapelo
"""

import pandas as pd

df =df = pd.read_csv("movie_dataset.csv")

print (df.info())

"""
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None
"""
# The Revenue (Millions) and Metascore have some missing values or NaN.

print (df.describe())

"""
              Rank         Year  ...  Revenue (Millions)   Metascore
count  1000.000000  1000.000000  ...          872.000000  936.000000
mean    500.500000  2012.783000  ...           82.956376   58.985043
std     288.819436     3.205962  ...          103.253540   17.194757
min       1.000000  2006.000000  ...            0.000000   11.000000
25%     250.750000  2010.000000  ...           13.270000   47.000000
50%     500.500000  2014.000000  ...           47.985000   59.500000
75%     750.250000  2016.000000  ...          113.715000   72.000000
max    1000.000000  2016.000000  ...          936.630000  100.000000

[8 rows x 7 columns]
"""
# Since the missing values/Nan are less done 20% per column of the data. I am gonna fill them with mean values.

df["Metascore"] = df["Metascore"].fillna(0).astype(int)

print (df.info())
"""
#   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           1000 non-null   int32  
dtypes: float64(2), int32(1), int64(4), object(5)
memory usage: 90.0+ KB
None
"""

print(df.columns)
"""
Index(['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year',
       'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)',
       'Metascore'],
      dtype='object')
"""

# Since the missing values/Nan are less done 20% per column of the data. I am gonna fill them with mean values.

mean_Revenue = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"] = df["Revenue (Millions)"].fillna(mean_Revenue)

# Check if all the missing/NaN values are replaced with the mean

print (df.info())
"""
#   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  1000 non-null   float64
 11  Metascore           1000 non-null   int32  
dtypes: float64(2), int32(1), int64(4), object(5)
memory usage: 90.0+ KB
None
"""

# Data looks clean

print(df.head())
"""
  Rank                    Title  ... Revenue (Millions) Metascore
0     1  Guardians of the Galaxy  ...             333.13        76
1     2               Prometheus  ...             126.46        65
2     3                    Split  ...             138.12        62
3     4                     Sing  ...             270.32        59
4     5            Suicide Squad  ...             325.02        40

[5 rows x 12 columns]
"""

# What is the highest rated movie in the dataset?

highest_rated_movie = df.loc[df["Rating"].idxmax()]["Title"]

print(f"The highest-rated movie is: {highest_rated_movie}")

# What is the average revenue of all movies in the dataset? 

average_revenue = df["Revenue (Millions)"].mean()

print(f"The average revenue of all movies is: {average_revenue}")

# What is the average revenue of movies from 2015 to 2017 in the dataset?

filtered_df = df[(df["Year"] >= 2015) & (df["Year"] <= 2017)]

average_revenue_2015_to_2017 = filtered_df["Revenue (Millions)"].mean()

print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_to_2017}")

# How many movies were released in the year 2016?

movies_2016 = df[df["Year"] == 2016]

# Get the count of movies released in 2016
number_of_movies_2016 = len(movies_2016)

print(f"The number of movies released in 2016 is: {number_of_movies_2016}")

# How many movies were directed by Christopher Nolan?
nolan_movies = df[df["Director"] == "Christopher Nolan"]

# Get the count of movies directed by Christopher Nolan
number_of_nolan_movies = len(nolan_movies)

print(f"The number of movies directed by Christopher Nolan is: {number_of_nolan_movies}")

# How many movies in the dataset have a rating of at least 8.0?

high_rated_movies = df[df["Rating"] >= 8.0]

# Get the count of movies with a rating of at least 8.0
number_of_high_rated_movies = len(high_rated_movies)

print(f"The number of movies with a rating of at least 8.0 is: {number_of_high_rated_movies}")

# What is the median rating of movies directed by Christopher Nolan?

nolan_movies = df[df["Director"] == "Christopher Nolan"]

# Calculate the median rating of Nolan's movies
median_rating_nolan = nolan_movies["Rating"].median()

print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan}")

# Find the year with the highest average rating?

average_rating_by_year = df.groupby("Year")["Rating"].mean()

# Find the year with the highest average rating

year_highest_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(f"The year with the highest average rating is {year_highest_rating} with an average rating of {highest_average_rating:.2f}")

# What is the percentage increase in number of movies made between 2006 and 2016?

movies_2006 = df[df["Year"] == 2006]
movies_2016 = df[df["Year"] == 2016]

# Calculate the number of movies in each year
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print(f"The percentage increase in the number of movies between 2006 and 2016 is {percentage_increase:.2f}%")

# Find the most common actor in all the movies?

from collections import Counter

# Assuming df is your DataFrame
# Replace 'Actors' with the actual column name in your dataset

# Combine all actor names into a single list
all_actors = df["Actors"].str.split(',').explode().str.strip().tolist()

# Use Counter to count occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor, count = actor_counts.most_common(1)[0]

print(f"The most common actor in all movies is: {most_common_actor} with {count} appearances.")

# How many unique genres are there in the dataset?

all_genres = df["Genre"].str.split(',').explode().str.strip()

# Get the number of unique genres
unique_genres_count = all_genres.nunique()

print(f"There are {unique_genres_count} unique genres in the dataset.")

# Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.

# And what advice can you give directors to produce better movies?

numerical_features = ["Year", "Runtime (Minutes)", "Rating", "Votes", "Revenue (Millions)", "Metascore"]
correlation_matrix = df[numerical_features].corr()

print("Correlation Matrix:")
print(correlation_matrix)
"""
Correlation Matrix:
                        Year  Runtime (Minutes)  ...  Revenue (Millions)  Metascore
Year                1.000000          -0.164900  ...           -0.117562  -0.066547
Runtime (Minutes)  -0.164900           1.000000  ...            0.247834   0.166101
Rating             -0.211219           0.392214  ...            0.189527   0.472446
Votes              -0.411904           0.407062  ...            0.607941   0.312790
Revenue (Millions) -0.117562           0.247834  ...            1.000000   0.137363
Metascore          -0.066547           0.166101  ...            0.137363   1.000000

[6 rows x 6 columns]
"""

# Insights

"""
1. Negative Correlation between Year and Votes: The negative correlation coefficient of -0.411904 between 'Year' and 'Votes' suggests that, on average, older movies tend to have fewer votes compared to newer ones. This could be due to the increasing accessibility of movies and voting platforms over time.

2. Positive Correlation between Runtime and Votes: The positive correlation coefficient of 0.407062 between 'Runtime (Minutes)' and 'Votes' indicates that movies with longer runtimes tend to attract more votes. This suggests that audiences might appreciate and engage more with movies that offer a longer viewing experience.

3. Positive Correlation between Rating and Metascore: The positive correlation coefficient of 0.472446 between 'Rating' and 'Metascore' suggests a moderate correlation between the movie's rating and its Metascore. This indicates that movies with higher professional critic scores (Metascore) tend to have higher audience ratings.

4. Strong Positive Correlation between Votes and Revenue: The strong positive correlation coefficient of 0.607941 between 'Votes' and 'Revenue (Millions)' indicates that movies with higher vote counts also tend to generate higher revenue. This implies that audience engagement and popularity play a significant role in a movie's financial success.

5. Positive Correlation between Rating and Revenue: The positive correlation coefficient of 0.189527 between 'Rating' and 'Revenue (Millions)' suggests a mild positive correlation between a movie's rating and its revenue. This implies that movies with higher ratings tend to have slightly higher revenue.
"""

# Advice for directors to produce better movies:

"""
1. Focus on Audience Engagement: Given the strong positive correlation between votes and revenue, directors should prioritize creating movies that resonate with audiences. Engaging storylines, well-developed characters, and captivating visuals can contribute to increased audience interaction.

2. Consider Movie Length: The positive correlation between runtime and votes suggests that audiences appreciate longer movies. However, directors should strike a balance, ensuring that the length aligns with the narrative and maintains viewer interest.

3. Collaborate with Critics: The positive correlation between Metascore and audience rating indicates that movies receiving positive professional reviews also tend to be well-received by audiences. Directors should consider collaborating with critics and ensuring a high-quality production.

4. Strive for Quality Ratings: The positive correlation between rating and revenue suggests that movies with higher ratings may attract a larger audience and, consequently, higher revenue. Directors should prioritize creating high-quality content that resonates with both critics and audiences.

5. Stay Current: The negative correlation between year and votes implies that newer movies tend to attract more votes. Directors should stay attuned to current trends, technology, and audience preferences to create movies that capture the zeitgeist and appeal to contemporary viewers.
"""












