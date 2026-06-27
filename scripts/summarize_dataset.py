#!/usr/bin/env python3
"""Print summary statistics for the mHealth app review dataset."""
import csv
import hashlib
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


def parse_date(value: str):
    for fmt in ["%m/%d/%Y %H:%M", "%m/%d/%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%m/%d/%Y"]:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass
    return datetime.fromisoformat(value)


def main(path: str):
    file_path = Path(path)
    rows = []
    with file_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    dates = [parse_date(row["review_date"]) for row in rows if row.get("review_date")]
    source_counts = Counter(row["source"] for row in rows)
    sentiment_counts = Counter(row["sentiment_value"] for row in rows)
    rating_counts = Counter(row["rating"] for row in rows)
    app_counts = Counter(row["app_name"] for row in rows)
    app_platform_counts = defaultdict(Counter)
    for row in rows:
        app_platform_counts[row["app_name"]][row["source"]] += 1

    sha256 = hashlib.sha256(file_path.read_bytes()).hexdigest()

    print(f"File: {file_path}")
    print(f"SHA256: {sha256}")
    print(f"Rows: {len(rows):,}")
    print(f"Date range: {min(dates).date()} to {max(dates).date()}")
    print("\nPlatform counts:")
    for key, value in source_counts.most_common():
        print(f"  {key}: {value:,}")
    print("\nSentiment counts:")
    for key, value in sentiment_counts.most_common():
        print(f"  {key}: {value:,}")
    print("\nRating counts:")
    for key in sorted(rating_counts, key=lambda x: int(x)):
        print(f"  {key}: {rating_counts[key]:,}")
    print("\nApp counts:")
    for key, value in app_counts.most_common():
        print(f"  {key}: {value:,}")
    print("\nApp/platform counts:")
    for app, counts in sorted(app_platform_counts.items()):
        print(f"  {app}: {dict(counts)}")


if __name__ == "__main__":
    dataset_path = sys.argv[1] if len(sys.argv) > 1 else "data/HealthApp_Reviews_Clean.csv"
    main(dataset_path)
