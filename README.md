# Spotify_ETL : AWS Serverless Data Pipeline Project

This project demonstrates a complete end-to-end ETL pipeline for processing music metadata using AWS services. It integrates multiple datasets — artists, albums, and tracks — and transforms them into an analytics-ready format for querying and visualization.

---

## 🗺️ Project Architecture

S3 (raw data)
├── artist.csv
├── albums.csv
└── tracks.csv
↓
AWS Glue Visual ETL (joins, cleanup)
↓
S3 (cleaned output in Parquet)
↓
AWS Glue Crawler (create catalog)
↓
Athena (SQL queries)
↓
QuickSight (visual dashboards)

---

## 🧰 Tools & Services Used

- **Amazon S3**: Raw and processed data storage  
- **AWS Glue Studio**: Visual ETL job with joins and transformations  
- **AWS Glue Crawler**: Crawled transformed data into the Glue Data Catalog  
- **AWS Athena**: Ran SQL queries on transformed data  
- **Amazon QuickSight**: Built visual dashboards and charts

---

## 🧪 ETL Pipeline Description

The ETL pipeline is built using AWS Glue Studio (Visual ETL) and performs the following steps:

- Joins artist and album datasets using `artist_id`
- Joins the result with track dataset using `album_id`
- Drops unnecessary or redundant fields
- Outputs the cleaned data to S3 in Parquet format

📄 Full description: (https://github.com/bharadwajbairi3/Spotify_ETL/blob/main/Glue/glue%3Aetl_pipeline_description.md)

🖼️ Pipeline Diagram:  
![Spotify_ETL Visual Flow](./images/glue_pipeline_screenshot.png)

---

## 🔍 Athena SQL Queries

Here are some of the queries used for data analysis:

- Top 10 most popular tracks
- Average duration by genre
- Most prolific artists
- Number of songs released per year
- Longest and shortest tracks

📄 Full queries: [sql/athena_queries.sql](./sql/athena_queries.sql)

---

## 📈 QuickSight Dashboards

Amazon QuickSight was used to visualize:

- Genre distribution
- Popularity trends
- Year-wise release counts
- Track duration analysis

🖼️ Dashboard previews: [quicksight/](./quicksight/dashboard_screenshots/)

---

## 🧠 Key Learnings

- Built a fully **serverless** ETL pipeline using AWS Glue Visual ETL  
- Performed **schema inference**, **joins**, and **data type casting**  
- Integrated AWS services for end-to-end analytics — from raw data to visualization  
- Practiced building scalable data workflows and dashboards

---

## 📁 Project Structure
aws-etl-pipeline-project/
├── glue/
│ └── etl_pipeline_description.md
├── sql/
│ └── athena_queries.sql
├── quicksight/
│ └── dashboard_screenshots/
├── images/
│ └── glue_pipeline_screenshot.png
├── data/
│ ├── sample_input.csv
│ └── sample_output.csv
└── README.md

---

## 🧑‍💻 Author

**Bharadwaj Bairi**  
AWS Data Engineer | Glue | S3 | Athena | QuickSight  
📧 bharadwajbairi3@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/bharadwajbairi)

---

## 📌 How to Run This Project

> Note: You need an AWS account with Glue, Athena, S3, and QuickSight access.

1. Upload sample CSV files to an S3 bucket.
2. Open AWS Glue Studio and import or rebuild the visual ETL job.
3. Create a crawler to catalog the output data.
4. Run Athena queries using the cataloged table.
5. Connect QuickSight to Athena and build visualizations.
