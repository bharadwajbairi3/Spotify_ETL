# AWS Glue Visual ETL: Spotify_ETL Pipeline

## 📄 Overview
This Glue ETL pipeline processes music-related data from Spotify-like sources. The raw data is ingested from S3 buckets and goes through a series of joins and transformations before being saved as clean, analytics-ready Parquet files to a destination S3 bucket.

---

## 🗂️ Data Sources
- **Artist** (S3 bucket)
- **Albums** (S3 bucket)
- **Track** (S3 bucket)

---

## 🔄 Transformations

### 1. 🔗 Join Artist & Album
- Join performed on `artist_id`
- Combines artist metadata (like `name`, `followers`, `popularity`) with album information (like `album_name`, `label`, `release_date`)

### 2. 🔗 Join with Track
- Second join between the previous result and Track dataset using `album_id`
- This brings in song-level details like `track_name`, `duration_sec`, and `track_popularity`

### 3. 🧹 Drop Unnecessary Fields
- Dropped raw fields like:
  - redundant keys
  - system-generated IDs
  - null-heavy columns
- Ensures output schema is clean and useful for analysis

---

## 🧪 Sample Output Schema

| Column Name         | Data Type |
|---------------------|-----------|
| artist_id           | string    |
| artist_name         | string    |
| followers           | string    |
| artist_popularity   | string    |
| album_id            | string    |
| album_name          | string    |
| label               | string    |
| release_date        | string    |
| album_popularity    | string    |
| track_id            | string    |
| track_name          | string    |
| duration_sec        | string    |
| track_popularity    | string    |
| genre               | string    |

> Note: All columns were stored as string in S3, but casted appropriately in Athena later (e.g., `INT`, `FLOAT`, `TIMESTAMP`).

---

## 🧾 Output
- **Target**: Cleaned data written to a separate S3 object
- **Format**: Parquet
- **Path**: `s3://bb-spotify-project-1/datawarehouse/`
- **Compression**: Snappy

---

## 🧠 Why This Matters
This pipeline demonstrates a typical music metadata ETL process where multiple datasets (artist, albums, tracks) are joined and normalized. It allows easy querying in Athena and visualization in QuickSight.

---

## 🛠️ Tools Used
- AWS Glue Studio (Visual ETL)
- Amazon S3 (Staging and Output)
- AWS Athena (Querying)
- AWS QuickSight (Visualization)
