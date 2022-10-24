import pandas as pd
from googleapiclient.discovery import build
import YT_API

df = pd.read_csv("data/channels.csv")

channels_ids = [el for el in list(df.channels_ids) if el not in ["CS60JdvsEX-A0PfEk2qNkWg", "UUC1fw-S3WgUeorPomVPk3s4w"]]
api_service_name = "youtube"
api_version = "v3"

with open ("key.txt") as f:
    api_key = f.read()

# Get credentials and create an API client
youtube = build(api_service_name, api_version, developerKey=api_key)
channels_with_playlist_id_df = pd.DataFrame(columns=["channelName", "playlistId"])

for el in channels_ids:
    channels_with_playlist_id_df = pd.concat([channels_with_playlist_id_df, YT_API.get_channel_overview(youtube, [el])[["channelName", "playlistId"]]])

channels_with_playlist_id_df["channel_id"] = channels_ids

channels_with_playlist_id_df.to_csv("data/channels_with_playlist_id.csv")
