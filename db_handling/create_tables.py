def create_channels_with_playlist_id_table(curr):
    create_table_command = ("""CREATE TABLE IF NOT EXISTS channels_with_playlist_id (
        channel_id VARCHAR(255),
        channel_name VARCHAR(255),
        playlist_id VARCHAR(255),
        PRIMARY KEY (channel_id)
    )""")

    curr.execute(create_table_command)


def create_channels_stats_table(curr):
    create_table_command = ("""CREATE TABLE IF NOT EXISTS channels_stats (
        channel_id VARCHAR(255),
        total_videos INTEGER,
        views BIGINT,
        subscribers BIGINT,
        time DATE NOT NULL DEFAULT CURRENT_DATE,
        PRIMARY KEY (channel_id, time)  
    )""")

    curr.execute(create_table_command)

def create_video_info_table(curr):
    create_table_command = ("""CREATE TABLE IF NOT EXISTS video_info (
        video_id VARCHAR(255),
        channel_id VARCHAR(255),
        title VARCHAR(255),
        length_of_description INTEGER,
        tags VARCHAR(2047),
        published_at DATE,
        duration VARCHAR(20),
        definition TEXT CHECK (definition IN ('hd', 'sd')),
        caption BOOLEAN,
        PRIMARY KEY (video_id),
        FOREIGN KEY (channel_id) REFERENCES channels_with_playlist_id (channel_id) ON UPDATE CASCADE ON DELETE CASCADE
    )""")

    curr.execute(create_table_command)


def create_video_stats_table(curr):
    create_table_command = ("""CREATE TABLE IF NOT EXISTS video_stats (
        video_id VARCHAR(255),
        channel_id VARCHAR(255),
        views_count DECIMAL,
        likes_count DECIMAL,
        comments_count DECIMAL,
        time DATE NOT NULL DEFAULT CURRENT_DATE,
        PRIMARY KEY (video_id, time),
        FOREIGN KEY (channel_id) REFERENCES channels_with_playlist_id (channel_id) ON UPDATE CASCADE ON DELETE CASCADE
    )""")

    curr.execute(create_table_command)

