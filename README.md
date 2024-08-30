#Kenya YouTube Channels Analysis
n\Overview

This project involves analyzing YouTube channels in Kenya to understand trends in video content, subscriber growth, and engagement metrics. By leveraging the YouTube Data API, Python, and various data analysis tools, this project aims to provide valuable insights into the performance of Kenyan YouTube channels.

Tools and Technologies

    Python: The primary programming language used for data analysis and API interactions.
    YouTube Data API: Used to retrieve data about YouTube channels, videos, and metrics.
    Requests: A Python library for making HTTP requests to the YouTube API.
    Pandas: For data manipulation and analysis.
    Matplotlib: For creating static, animated, and interactive visualizations in Python.
    Seaborn: For statistical data visualization.
    Streamlit: For creating interactive dashboards.

Project Structure

The project is organized as follows:
Youtube-channel-Analysis/: Root directory of the project

    data/: Directory to store raw and processed data
        kenya_channels.csv: CSV file with data on Kenyan YouTube channels
    notebooks/: Jupyter notebooks for exploration and analysis
        Youtube-channel-Analysis.ipynb: Notebook for data analysis and visualization
    dashboard.py: Streamlit application for creating an interactive dashboard
    .env: Environment file containing API keys and other environment variables
    requirements.txt: File listing Python dependencies required for the project
    README.md: Project documentation file
    LICENSE: License file for the project


Setup and Installation

    Clone the Repository

git clone https://github.com/bellonbits/YouTubeChannel-Analysis.git
cd YouTubeChannel-Analysis

Install Dependencies

pip install -r requirements.txt

Obtain API Key

    Go to the Google Developers Console.
    Create a new project and enable the YouTube Data API.
    Generate an API key and replace the placeholder in data_collection.py.


Run Dashboard

        streamlit run dashboard.py

Features

    Data Collection: Fetches data from the YouTube API, including channel statistics, video metrics, and more.
    Data Analysis: Analyzes subscriber trends, video content performance, and engagement metrics.
    Visualization: Provides various charts and graphs to visualize data insights.
    Dashboard: An interactive web-based interface to explore the data and visualizations.

Example Usage

After setting up the project, you can use the Streamlit dashboard to interactively explore different aspects of Kenyan YouTube channels. Use the filters to view data trends over time, compare subscriber counts, and analyze video performance.

Contributing

Contributions are welcome! Please submit a pull request with your changes or open an issue for discussion.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    YouTube Data API
    Pandas Documentation
    Matplotlib Documentation
    Seaborn Documentation
