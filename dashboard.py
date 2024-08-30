import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV
@st.cache
def load_data():
    return pd.read_csv('kenya_channels.csv')

df = load_data()

# Streamlit Dashboard
st.title("YouTube Channel Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")

# Filter by subscriber count
min_subscribers, max_subscribers = st.sidebar.slider(
    "Subscriber Count Range",
    min_value=int(df['subscriberCount'].min()),
    max_value=int(df['subscriberCount'].max()),
    value=(int(df['subscriberCount'].min()), int(df['subscriberCount'].max()))
)
filtered_df = df[(df['subscriberCount'] >= min_subscribers) & (df['subscriberCount'] <= max_subscribers)]

# Filter by view count
min_views, max_views = st.sidebar.slider(
    "View Count Range",
    min_value=int(df['viewCount'].min()),
    max_value=int(df['viewCount'].max()),
    value=(int(df['viewCount'].min()), int(df['viewCount'].max()))
)
filtered_df = filtered_df[(filtered_df['viewCount'] >= min_views) & (filtered_df['viewCount'] <= max_views)]

# Filter by video count
min_videos, max_videos = st.sidebar.slider(
    "Video Count Range",
    min_value=int(df['videoCount'].min()),
    max_value=int(df['videoCount'].max()),
    value=(int(df['videoCount'].min()), int(df['videoCount'].max()))
)
filtered_df = filtered_df[(filtered_df['videoCount'] >= min_videos) & (filtered_df['videoCount'] <= max_videos)]

# Display filtered data
st.write(f"Showing {len(filtered_df)} channels")
st.dataframe(filtered_df)

# Visualization: Subscriber Count vs. View Count
st.subheader("Subscriber Count vs. View Count")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x='subscriberCount', y='viewCount', hue='title', palette='viridis')
plt.title('Subscriber Count vs. View Count')
plt.xlabel('Subscriber Count')
plt.ylabel('View Count')
st.pyplot(plt)

# Visualization: Distribution of Subscriber Counts
st.subheader("Distribution of Subscriber Counts")
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['subscriberCount'], bins=20, edgecolor='black')
plt.title('Distribution of Subscriber Counts')
plt.xlabel('Subscriber Count')
plt.ylabel('Frequency')
st.pyplot(plt)

