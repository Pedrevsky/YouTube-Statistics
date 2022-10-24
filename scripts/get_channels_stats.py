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

channels_stats_df = pd.DataFrame(columns=["subscribers","views", "totalVideos"])

for el in channels_ids:
    channels_stats_df = pd.concat([channels_stats_df, YT_API.get_channel_stats(youtube, [el])[["subscribers","views", "totalVideos"]]])

channels_stats_df["channels_ids"] = channels_ids
channels_stats_df["time"] = pd.to_datetime('today').normalize()
channels_stats_df[["subscribers", "views", "totalVideos"]] = channels_stats_df[["subscribers", "views", "totalVideos"]].apply(pd.to_numeric, errors="coerce")

with open("data/channels_stats.csv", 'a') as f:
    channels_stats_df.to_csv(f, mode='a', header=f.tell()==0)
