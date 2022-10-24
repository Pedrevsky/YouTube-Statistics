import pandas as pd
from googleapiclient.discovery import build
import YT_API

api_service_name = "youtube"
api_version = "v3"

with open ("key.txt") as f:
    api_key = f.read()

# Get credentials and create an API client
youtube = build(api_service_name, api_version, developerKey=api_key)

channels_df = pd.read_csv("data/channels_with_playlist_id.csv")

video_ids = []

for value in channels_df["playlistId"]:
    video_ids += YT_API.get_video_ids(youtube, value)

video_stats_df = YT_API.get_video_stats(youtube, video_ids)

with open("data/video_stats.csv", 'a') as f:
    video_stats_df.to_csv(f, mode='a', header=f.tell()==0)
