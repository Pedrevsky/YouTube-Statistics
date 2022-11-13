from insert_to_table import *


def check_if_video_exists(curr, video_id):
    query = ("SELECT video_id FROM video_info WHERE video_id = %s")

    curr.execute(query, (video_id,))
    return curr.fetchone() is not None

def update_video_info_row(curr, video_id, title, length_of_description, tags):
    query = ("""UPDATE video_info
    SET title = %s,
        length_of_description = %s,
        tags = %s
    WHERE video_id = %s;""")
    vars_to_update = (title, length_of_description, tags, video_id)
    curr.execute(query, vars_to_update)

def append_channels_with_playlist_id_table(curr, df):
    curr.execute("SELECT * FROM channels_with_playlist_id")
    if len(curr.fetchall()) == 0:
        for i, row in df.iterrows():
            insert_into_channels_with_playlist_id_table(curr, row["channel_id"], row["channel_name"], row["playlist_id"])


def append_channels_stats_table(curr, df):
    for i, row in df.iterrows():
        insert_into_channels_stats_table(curr, row["channel_id"], row["total_videos"], row["views"], row["subscribers"], row["time"])



def append_video_info_table(curr, df):
    curr.execute("SELECT * FROM video_info")
    if len(curr.fetchall()) == 0:
        for i, row in df.iterrows():
            insert_into_video_info_table(curr, row["video_id"], row["channel_id"], row["title"], row["length_of_description"], row["tags"], row["published_at"], row["duration"], row["definition"], row["caption"])
    else:
        for i, row in df.iterrows():
            if check_if_video_exists(curr, row["video_id"]):
                update_video_info_row(curr, row["video_id"], row["title"], row["length_of_description"], row["tags"])
            else:
                insert_into_video_info_table(curr, row["video_id"], row["channel_id"], row["title"], row["length_of_description"], row["tags"], row["published_at"], row["duration"], row["definition"], row["caption"])


def append_video_stats_table(curr, df):
    for i, row in df.iterrows():
        insert_into_video_stats_table(curr, row["video_id"], row["channel_id"], row["views_count"], row["likes_count"], row["comments_count"], row["time"])
