# mHealth App Review Sentiment Dataset

This repository contains the cleaned mHealth app-review dataset used for sentiment classification and thematic analysis in the manuscript:

**A Unified Framework for Sentiment Classification and Thematic Analysis of mHealth App Reviews**

The dataset contains public user reviews collected from health-related applications across Google Play and the Apple App Store. It is intended for academic research on mHealth feedback analysis, sentiment classification, topic modeling, and interpretable NLP.

## Repository contents

```text
.
├── data/
│   ├── HealthApp_Reviews_Clean.csv
│   └── external_validation/
│       └── README.md
├── docs/
│   └── data_dictionary.md
├── outputs/
│   └── dataset_summary.json
├── scripts/
│   └── summarize_dataset.py
├── CITATION.cff
├── DATA_TERMS.md
├── LICENSE
└── README.md
```

## Dataset file

Main dataset file:

```text
data/HealthApp_Reviews_Clean.csv
```

## Dataset summary

| Item | Value |
|---|---:|
| Total cleaned reviews | 19,601 |
| Columns | 6 |
| Review date range | 2015-06-16 to 2025-04-19 |
| Google Play reviews | 15,023 |
| App Store reviews | 4,578 |
| Positive reviews | 13,525 |
| Negative reviews | 4,885 |
| Neutral reviews | 1,191 |

## Columns

| Column | Description |
|---|---|
| `source` | Review platform: Google Play or App Store. |
| `review_description` | Cleaned user review text. |
| `review_date` | Date and time associated with the review. |
| `rating` | User star rating from 1 to 5. |
| `app_name` | Name of the mHealth application. |
| `sentiment_value` | Rating-derived sentiment label: Positive, Negative, or Neutral. |

More details are provided in [`docs/data_dictionary.md`](docs/data_dictionary.md).

## Sentiment labeling

The sentiment labels are derived from star ratings:

- 1–2 stars: `Negative`
- 3 stars: `Neutral`
- 4–5 stars: `Positive`

The manuscript reformulates the final classification task as binary positive-versus-negative sentiment classification after excluding the neutral class.


## Reproducing summary statistics

Run:

```bash
python scripts/summarize_dataset.py data/HealthApp_Reviews_Clean.csv
```

This prints row counts, platform counts, sentiment distribution, rating distribution, date range, and checksum.
