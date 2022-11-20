from os import environ
import pandas as pd
from googleapiclient.discovery import build
import YT_API

df = pd.read_csv("data/channels.csv")

channels_ids = [el for el in list(df.channels_ids) if el not in ["CS60JdvsEX-A0PfEk2qNkWg", "UUC1fw-S3WgUeorPomVPk3s4w"]]
api_service_name = "youtube"
api_version = "v3"

api_key = environ.get("youtube_api_key")

# Get credentials and create an API client
youtube = build(api_service_name, api_version, developerKey=api_key)

channels_with_playlist_id_df = pd.DataFrame(columns=["channelName", "playlistId"])
channels_stats_df = pd.DataFrame(columns=["subscribers","views", "totalVideos"])

for el in channels_ids:
    channels_with_playlist_id_df = pd.concat([channels_with_playlist_id_df, YT_API.get_channel_overview(youtube, [el])[["channelName", "playlistId"]]])
    channels_stats_df = pd.concat([channels_stats_df, YT_API.get_channel_stats(youtube, [el])[["subscribers","views", "totalVideos"]]])

channels_with_playlist_id_df["channel_id"] = channels_ids

channels_stats_df["channel_id"] = channels_ids
channels_stats_df["time"] = pd.to_datetime('today')
channels_stats_df[["subscribers", "views", "totalVideos"]] = channels_stats_df[["subscribers", "views", "totalVideos"]].apply(pd.to_numeric, errors="coerce")

channels_with_playlist_id_df = channels_with_playlist_id_df.rename(columns={"channelName": "channel_name", "playlistId": "playlist_id"})
channels_with_playlist_id_df = channels_with_playlist_id_df[["channel_id", "channel_name", "playlist_id"]]

channels_stats_df = channels_stats_df.rename(columns={"totalVideos":"total_videos"})
channels_stats_df = channels_stats_df[["channel_id", "total_videos", "views", "subscribers", "time"]]

channels_with_playlist_id_df.to_csv("data/channels_with_playlist_id.csv")
channels_stats_df.to_csv("data/channels_stats.csv")

