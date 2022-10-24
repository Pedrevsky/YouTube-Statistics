import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://www.hiphop.pl/kanaly-hip-hop"

os.chdir("C:/Users/Kiepson/Studia/3 rok/IAD/Python/youtube_project")

with open("data/strona.txt", encoding="utf8") as f:
    soup = bs(f.read())


links = [link["href"] for link in soup.body.find_all("a", href=True)[27:243]]
channels_names = [name.string for name in soup.body.find_all("div", {"class":"ant-card-grid Channels_gridStyle__R1mPg ant-card-grid-hoverable"})]

df = pd.DataFrame({"channels_names":channels_names, "links":links})
with open("data/names_of_wanted_channels.txt") as f:
    wanted_channels = f.read().split(",")

df = df[df["channels_names"].isin(wanted_channels)]


channels_ids = []

for link in df["links"]:
    page = requests.get(link)
    soup = bs(page.content, "html.parser")
    script_with_id = soup.find_all("script")[-1]
    json_object = json.loads(script_with_id.contents[0])
    channels_ids.append(json_object["props"]["pageProps"]["channel"]["youtube_id"])
    # print(json_object["props"]["pageProps"]["channel"]["youtube_id"])

df["channels_ids"] = channels_ids


df.to_csv("data/channels.csv", index=False)