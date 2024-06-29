from pytube import YouTube
import os

def download(name, link):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="")
    new_file = name + ".mp3"
    os.rename(out_file, new_file)


n = str(input("Enter file name: "))
l = str(input("Enter Link: "))
download(n,l)