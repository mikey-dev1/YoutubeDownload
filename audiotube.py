from pytube import YouTube
# from pytube import YouTube
url = " "
yt = YouTube(url)

yd = yt.streams.get_highest_resolution()

yd.download()