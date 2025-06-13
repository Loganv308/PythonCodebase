# Fuck PyTube on god

# This script is used to scrape all the information of the videos, put the data into JSON files,
# then return a list of the Youtube URL's to be downloaded by the main file (downloader.py).

import scrapetube
import json
import os
from pathlib import Path
import utils.utils as u


# * Integrate limiter as arg so it doesn't import all the channels videos if there's a shit ton. 
# * Integrate special character renaming. In windows, some characters can't go in the name of a json file. 
#       Example: [Errno 22] Invalid argument: 'output\\penguinz0\\#24 - Moist Meter | Saw X.json' 
# * The issue is this character: |||||| 
def getChannelVideosInfo(channel_name, limit):

    video_Urls = []

    x = u.Utils()
    incrementer = x.countUp(0)

    videos = scrapetube.get_channel(channel_url=f"https://www.youtube.com/@{channel_name}", limit={limit})
        
    if not videos:
        print(f"No videos found for channel: {channel_name}")
    # Exit or handle the error as needed
    else:
        for video in videos:
            for video in videos:
                channel_url = video["navigationEndpoint"]["commandMetadata"][
                    "webCommandMetadata"
                ]["url"]

                formatted_Vid_URL = f"https://www.youtube.com{channel_url}"

                video_Urls.append(formatted_Vid_URL)

                video_title = video["title"]["runs"][0]["text"]

                try:
                    my_file = Path(f"output\\{channel_name}")
                    if my_file.exists():
                        with open(
                            f"output\\{channel_name}\\#{incrementer} - {video_title}.json", "a+"
                            
                        ) as f:
                            x.replace_illegal_chars_regex(f, pattern=r'[\\/*?:"<>|]', replacement="")
                            json.dump(video, f, indent=2)
                            f.write("\n")
                        x = x + 1
                    else:
                        os.mkdir(f"output\\{channel_name}")
                except Exception as e:
                    print(e)
                    continue
    return video_Urls
