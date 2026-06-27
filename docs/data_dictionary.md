# Data dictionary

## `data/HealthApp_Reviews_Clean.csv`

| Column | Type | Description | Example |
|---|---|---|---|
| `source` | string | Review platform. Values include `Google Play` and `App Store`. | `Google Play` |
| `review_description` | string | Cleaned app-store review text. This is the main text field used for sentiment classification and thematic analysis. | `enjoying the workouts and the guidance from the trainers` |
| `review_date` | datetime string | Date and time associated with the review in the exported dataset. | `4/16/2025 13:49` |
| `rating` | integer | User star rating from 1 to 5. | `5` |
| `app_name` | string | Application name as stored in the cleaned dataset. | `Centr: Personal Fitness App` |
| `sentiment_value` | string | Sentiment label derived from rating. Values: `Positive`, `Negative`, `Neutral`. | `Positive` |

## Sentiment mapping

| Rating | Sentiment label |
|---:|---|
| 1 | Negative |
| 2 | Negative |
| 3 | Neutral |
| 4 | Positive |
| 5 | Positive |

## Dataset statistics

The cleaned corpus contains 19,601 reviews.

| Platform | Reviews | Date range |
|---|---:|---|
| Google Play | 15,023 | 2016-04-07 to 2025-04-19 |
| App Store | 4,578 | 2015-06-16 to 2025-04-18 |

| Sentiment | Reviews |
|---|---:|
| Positive | 13,525 |
| Negative | 4,885 |
| Neutral | 1,191 |

## Notes

- The final binary classification task in the manuscript excludes neutral reviews.
- Ratings are used to derive sentiment labels and should not be used as input predictors when reproducing text-based sentiment models.
- The review text is user-generated and may contain spelling variation, informal language, and app-specific wording.
