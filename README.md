# AnimeVerse: 20K+ Real Anime Records from AniList API
A comprehensive anime dataset containing 20,000+ real anime records collected directly from the AniList GraphQL API.

<img width="736" height="414" alt="Itachi Uchiha Wallpaper 4k HD Wallpaper" src="https://github.com/user-attachments/assets/78c1c095-9bce-44f9-badb-837c6865aacb" />

The dataset includes ratings, popularity metrics, favorites, genres, studios, release information, formats, and production metadata, making it suitable for machine learning, recommendation systems, analytics, and data visualization projects.

Kaggle Link : [https://www.kaggle.com/datasets/velvetcrystal/from-naruto-to-one-piece-20k-real-anime-dataset]

## Overview

This dataset contains authentic anime metadata sourced directly from AniList. All records were collected programmatically using Python and the AniList GraphQL API.

No synthetic records, generated values, or manually fabricated entries have been included.

## Features

* 20,000+ Real Anime Records
* Direct API Collection
* Community Ratings and Popularity Metrics
* Genres and Production Studios
* Release and Airing Information
* Suitable for Machine Learning Applications
* Recommendation System Development
* Trend Analysis and Visualization

## Dataset Columns

| Column          | Description                        |
| --------------- | ---------------------------------- |
| anime_id        | Unique AniList identifier          |
| title_romaji    | Anime title in Romaji              |
| title_english   | Official English title             |
| title_native    | Original Japanese title            |
| season          | Release season                     |
| season_year     | Release year                       |
| type            | Media type                         |
| format          | TV, Movie, OVA, ONA, Special, etc. |
| status          | Airing or production status        |
| episodes        | Total episode count                |
| duration        | Episode duration in minutes        |
| average_score   | AniList community score            |
| popularity      | AniList popularity metric          |
| favorites       | Number of user favorites           |
| genres          | Associated genres                  |
| country         | Country of origin                  |
| source_material | Original source material           |
| studio          | Primary animation studio           |
| start_year      | Airing start year                  |
| start_month     | Airing start month                 |
| start_day       | Airing start day                   |

## Data Source

Source: AniList GraphQL API

Official Documentation:
https://anilist.gitbook.io/anilist-apiv2-docs/

## Data Collection Methodology

The dataset was collected using:

* Python
* Requests
* GraphQL Queries
* AniList Public API

All records were retrieved directly from AniList without manual modification.

## Data Authenticity

This dataset contains only real-world anime data.

* Real anime titles
* Real ratings
* Real popularity metrics
* Real favorite counts
* Real studio information
* Real release dates
* No synthetic records
* No AI-generated values

Missing values are preserved when information is unavailable from the source.

## Potential Use Cases

* Anime Recommendation Systems
* Popularity Prediction
* Genre Trend Analysis
* Studio Performance Analysis
* Machine Learning Projects
* Exploratory Data Analysis
* Data Visualization
* Community Engagement Research

## Example Questions

* Which studios produce the highest-rated anime?
* Which genres are the most popular?
* How has anime popularity evolved over time?
* What factors influence anime ratings?
* Which seasons produce the most successful anime?

## Disclaimer

Ratings, popularity scores, and favorite counts may change over time as users continue interacting with AniList. This dataset represents a snapshot of AniList data at the time of collection.

## License

Please review AniList's Terms of Service and API usage guidelines before redistribution or commercial use of the data.

## Acknowledgements

Special thanks to the AniList team for providing public access to anime metadata through their GraphQL API.
