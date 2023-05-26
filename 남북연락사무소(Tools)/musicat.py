
import youtube_dl

# YouTube video URL
url = input("URL: ")

# Options for downloading and converting to mp3
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])
