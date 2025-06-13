# Fuck PyTube on god

import yt_dlp as ydl
import channelVideoScrape
from utils import utils

OPTIONS = {
    # First will try to to download a 1080p copy of the video, if there isn't one it will go for 1440p. 
    "format": "bestvideo[height=1080]+bestaudio/best[height=1080],bestvideo[height=1440]+bestaudio/best[height=1440]",
    "postprocessors": [
        {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }
    ],
}

if __name__ == "__main__":
    channel = input("Enter Channel Name: ")

    videoLimit = input("Number of videos (Sorted by newest): ")

    # The following line will return a list of all the YouTube URL's, and generate JSON files of the data.
    videoInfo = channelVideoScrape.getChannelVideosInfo(channel_name=str(channel), limit=videoLimit)

    print("VID URL'S", videoInfo)

    # with ydl.YoutubeDL(OPTIONS) as y:
    #     y.download()
