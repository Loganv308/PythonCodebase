# Fuck PyTube on god

# This script is used to scrape all the information of the videos, put the data into JSON files,
# then return a list of the Youtube URL's to be downloaded by the main file (downloader.py).

import scrapetube
import json
import os
from utils import utils
from pathlib import Path


# * Integrate limiter as arg so it doesn't import all the channels videos if there's a shit ton.
# * Integrate special character renaming. In windows, some characters can't go in the name of a json file.
#       Example: [Errno 22] Invalid argument: 'output\\penguinz0\\#24 - Moist Meter | Saw X.json'
# * The issue is this character: ||||||
def getChannelVideosInfo(channel_name):
    video_Urls = []

    x = utils.Utils()
    y = 0

    videos = scrapetube.get_channel(
        channel_url=f"https://www.youtube.com/@{channel_name}"
    )

    if not videos:
        print(f"No videos found for channel: {channel_name}")
    # Exit or handle the error as needed
    else:
        for video in videos:
            channel_url = video["navigationEndpoint"]["commandMetadata"][
                "webCommandMetadata"
            ]["url"]

            formatted_Vid_URL = f"https://www.youtube.com{channel_url}"

            video_Urls.append(formatted_Vid_URL)

            video_title = video["title"]["runs"][0]["text"]

            try:
                my_file = Path(f"output\\{channel_name}")

                if not my_file.exists():
                    os.mkdir(f"output\\{channel_name}")
                    with open(
                        f"output\\{channel_name}\\#{y} - {video_title}.json", "a+"
                    ) as f:
                        json.dump(video, f, indent=2)
                        f.write("\n")
                        x.countUp(y)
                else:
                    os.mkdir(f"output\\{channel_name}")
            except Exception as e:
                print("CHANNELTESTER_ERROR:", e)
                continue
    return video_Urls
