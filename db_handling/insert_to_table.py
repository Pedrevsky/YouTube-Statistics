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