

from yt_dlp import YoutubeDL
import platform

URLS = ['https://www.youtube.com/shorts/87_NPqV9ZEk']
form = 'mp4'
location = ''

def yt_dl(URLS, form, location):
    '''
    Input:
        URLS = [] of youtube url strings
        form = 'mp3' or 'mp4'
        location = '' or other save location. Default to Downloads
    '''
    # detect host system and set default to Downloads folder
    if not location and platform.system() == 'Windows':
        location = r"%userprofile%\downloads"
    elif not location and platform.system() == 'Linux': 
        location = r"~/Downloads/"
    elif not location and platform.system() == 'Darwin': 
        location = r"~/Downloads/"
        

    if form == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{location}%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }],
        }
    elif form == 'mp4':
        ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{location}%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)

# yt_dl(URLS, 'mp3', '')