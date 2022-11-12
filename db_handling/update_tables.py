def insert_into_channels_with_playlist_id_table(curr, channel_id, channel_name, playlist_id):
    insert_command = ("""INSERT INTO channels_with_playlist_id (channel_id, channel_name, playlist_id)
    VALUES(%s, %s, %s);""")
    row_to_insert = (channel_id, channel_name, playlist_id)
    curr.execute(insert_command, row_to_insert)


def insert_into_channels_stats_table(curr, channel_id, total_videos, views, subscribers, time):
    insert_command = ("""INSERT INTO channels_stats (channel_id, total_videos, views, subscribers, time)
    VALUES(%s, %s, %s, %s, %s);""")
    row_to_insert = (channel_id, total_videos, views, subscribers, time)
    curr.execute(insert_command, row_to_insert)


def insert_into_video_info_table(curr, video_id, channel_id, title, length_of_description, tags, published_at, duration, definition, caption):
    insert_command = ("""INSERT INTO video_info (video_id, channel_id, title, length_of_description, tags, published_at, duration, definition, caption)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);""")
    row_to_insert = (video_id, channel_id, title, length_of_description, tags, published_at, duration, definition, caption)
    curr.execute(insert_command, row_to_insert)


def insert_into_video_stats_table(curr, video_id, channel_id, views_count, likes_count, comments_count, time):
    insert_command = ("""INSERT INTO video_stats (video_id, channel_id, views_count, likes_count, comments_count, time)
    VALUES(%s, %s, %s, %s, %s, %s);""")
    row_to_insert = (video_id, channel_id, views_count, likes_count, comments_count, time)
    curr.execute(insert_command, row_to_insert)


def update_video_info_row(curr):
    pass

def update_video_info_table(curr):
    pass

def append_channels_with_playlist_id_table(curr, df):
    curr.execute("SELECT * FROM channels_with_playlist_id")
    if len(curr.fetchall()) == 0:
        for i, row in df.iterrows():
            insert_into_channels_with_playlist_id_table(curr, row["channel_id"], row["channel_name"], row["playlist_id"])


def append_channels_stats_table(curr, df):
    for i, row in df.iterrows():
        insert_into_channels_stats_table(curr, row["channel_id"], row["total videos"], row["views"], row["subscribers"], row["time"])



def append_video_info_table(curr, df):
    curr.execute("SELECT * FROM video_info")
    if len(curr.fetchall()) == 0:
        for i, row in df.iterrows():
            insert_into_video_info_table(curr, row["video_id"], row["channel_id"], row["title"], row["length_of_description"], row["tags"], row["published_at"], row["duration"], row["definition"], row["caption"])
    else:
        pass #update table


def append_video_stats_table(curr, df):
    for i, row in df.iterrows():
        insert_into_video_stats_table(curr, row["video id"], row["channel id"], row["views count"], row["likes_count"], row["comments_count"], row["time"])
