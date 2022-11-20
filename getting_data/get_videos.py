from os import environ
import pandas as pd
from googleapiclient.discovery import build
import YT_API

api_service_name = "youtube"
api_version = "v3"

api_key = environ.get("youtube_api_key")

# Get credentials and create an API client
youtube = build(api_service_name, api_version, developerKey=api_key)

channels_df = pd.read_csv("data/channels_with_playlist_id.csv")

video_ids = []

for value in channels_df["playlist_id"]:
    video_ids += YT_API.get_video_ids(youtube, value)


video_df = YT_API.get_video_details(youtube, video_ids)
video_df["description"] = video_df["description"].apply(len)

video_stats_df = YT_API.get_video_stats(youtube, video_ids)


video_df = video_df.rename(columns = {"channelId": "channel_id", "publishedAt": "published_at", "description":"length_of_description"})

video_stats_df = video_stats_df.rename(columns = {"channelId": "channel_id", "viewCount": "views_count", "likeCount": "likes_count", "commentCount": "comments_count"})
video_stats_df = video_stats_df[["video_id", "channel_id", "views_count", "likes_count", "comments_count", "time"]]

video_df.to_csv("data/video_info.csv")
video_stats_df.to_csv("data/video_stats.csv")
