import pytube


def download_video(link):
    try:
        yt = pytube.YouTube(link)
        dw = yt.streams.first()
        dw.download('C:/yetube')
        return 'file downloaded'
    except:
        return 'unable to download', link


