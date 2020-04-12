import pytube


def download_video(link):
    try:
        yt = pytube.YouTube(link)
        dw = yt.streams.first()
        dw.download('C:/yetube')
        print('file downloaded')
    except:
        print('unable to download', link)



