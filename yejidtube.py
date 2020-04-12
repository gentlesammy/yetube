from tkinter import *
import youtuber
import requests
import urllib

yejidtube = Tk()
yejidtube.geometry('700x500')
yejidtube.title('YETUBE Downloader - Free Youtube Downloader By Sayem Tech(+2348060913903)')
yejidtube.configure(bg='black')
ye_title = Label(yejidtube, text="YETUBE 1.0", font=("bolder", 50), fg="red", bg="black")
ye_title.place(x=150, y=20)
link_label = Label(yejidtube, text="PASTE YOUR YOUTUBE LINK HERE: ", font=("bolder", 10), fg="white", bg="black")
link_label.place(x=210, y=150)
my_link = StringVar()
links_box = Entry(yejidtube, width=68, borderwidth=10, textvariable=my_link)
links_box.place(x=125, y=190)


def downloadvideo():
    try:
        response = requests.get(str(my_link.get()))

        info = youtuber.link_info_download(str(my_link.get()))
        print(info)
        result_box = Label(yejidtube, text="check your folder c:/yetube for the file  " + info['title'], fg="blue",
                           bg="black")
        result_box.place(x=210, y=330)
        print(youtuber.download_video(str(my_link.get())))
    except:
        error_result_box = Label(yejidtube, text="Invalid Link or Network Problem, "
                                                 "Please check Both", fg="white", bg="red", font=('bolder', 10))
        error_result_box.place(x=200, y=330)


submit_button = Button(yejidtube, text="DOWNLOAD VIDEO", width=34, bg="white", fg="black", font=('bolder', 15),
                       command=downloadvideo)
submit_button.place(x=150, y=260)

reply_box = Label(yejidtube,
                  text="NOTE: \n * Enter the correct youtube link for downloading  .\n * Click download video ONCE and"
                       "wait for it to download \n *Your downloaded video will be stored in c:/yetube",
                  fg="skyblue", bg="black")
reply_box.place(x=210, y=400)

yejidtube.mainloop()


