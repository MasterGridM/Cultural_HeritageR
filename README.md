
# **Project Folder: Cultural_HeritageR**

This folder contains various datasets, scripts, reports, and applications related to analyzing and preserving historical artifacts and texts.

## **Datasets**
- **My3DModels/** – Contains a dataset of 3D models.
- **Gutenberg_Books/** – Stores over 2,000 books downloaded from Project Gutenberg.
- **My3DModelsEDA/** – A superset of approximately 300 3D models for exploratory data analysis.
- **texts/** – Contains `.gz` files downloaded from Project Gutenberg, later converted and saved in the *Gutenberg_Books* folder.

## **Applications & Scripts**
- **app.py** – A Flask application to visualize 3D models along with their mapped historical timelines.
- **DescAndTime/** – Script to generate descriptions and estimated historical timelines for artifacts.
- **gutenberg_d.py** – Script used to download books from Project Gutenberg.
- **merge.py** – Script to merge two CSV files and create a consolidated dataset.
- **modeldataretr.py** – Script to retrieve metadata for 3D models.

## **Notebooks**
- **My3DMod.ippynb** – Jupyter Notebook for exploratory data analysis (EDA) on the 3D models dataset.
- **mybook.ipynb** – Notebook for analyzing historical texts, extracting keywords, and generating insights.

## **Metadata & Reports**
- **Final 3D Model Metadata Report.pdf** – Extracted metadata to aid in preservation and reconstruction activities.
- **gutenberg_metadata.csv** – Metadata of the downloaded Gutenberg books.
- **Keywords.json** – Extracted keywords from each document.
- **Metadata summary report/** – An intermediate report generated during analysis.
- **My3DModels_metadata_summary.csv** – Summary of metadata extracted from 3D models.
- **merged_file_data.csv** – The final merged dataset after processing.

## **Other Files**
- **templates/** – Contains `index.html` for web-based visualization.
- **DataSetReadme/** – Provides dataset links for *My3DModels* and *Gutenberg_Books*.

This project integrates 3D model analysis, historical text processing, and metadata extraction to support digital preservation and reconstruction efforts.
