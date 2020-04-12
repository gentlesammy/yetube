import pytube


def download_video(link):
    try:
        yt = pytube.YouTube(link)
        dw = yt.streams.first()
        dw.download('C:/yetube')
        return 'file downloaded'
    except:
        return 'unable to download', link


# video details fetching link


def link_info_download(link):
    yt = pytube.YouTube(link)
    video_details = {
        'title':   yt.title,
        'cover':   yt.thumbnail_url
    }
    return video_details

