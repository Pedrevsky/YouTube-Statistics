import pandas as pd
import psycopg2 as ps
from create_tables import *
from update_tables import *


channels_with_playlist_id = pd.read_csv("data/channels_with_playlist_id.csv")
channels_stats = pd.read_csv("data/channels_stats.csv")
video_info = pd.read_csv("data/video_info.csv")
video_stats = pd.read_csv("data/video_stats.csv")

with open("db_auth.txt", "r") as f:
    db_auth = f.read().split(",")


conn = ps.connect(f"dbname={db_auth[0]} user={db_auth[1]} password={db_auth[2]} port={db_auth[3]}")
curr = conn.cursor()


#Initialize tables 
create_channels_with_playlist_id_table(curr)
create_channels_stats_table(curr)
create_video_info_table(curr)
create_video_stats_table(curr)
print("\n\nCreating OK\n\n")




append_channels_with_playlist_id_table(curr, channels_with_playlist_id)
append_channels_stats_table(curr, channels_stats)
