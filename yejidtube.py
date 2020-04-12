from tkinter import *
import youtuber

yejidtube = Tk()
yejidtube.geometry('700x500')
yejidtube.title('YETUBE Downloader - Free Youtube Downloader By Sayem Tech(+2348060913903)')
yejidtube.configure(bg='black')
ye_title = Label(yejidtube, text="YETUBE", font=("bolder", 50), fg="red", bg="black")
ye_title.place(x=180, y=20)
link_label = Label(yejidtube, text="PASTE YOUR YOUTUBE LINK HERE: ", font=("bolder", 10), fg="white", bg="black")
link_label.place(x=210, y=150)
my_link = StringVar()
links_box = Entry(yejidtube, width=68, borderwidth=10, textvariable=my_link)
links_box.place(x=125, y=190)


def downloadvideo():
    youtuber.download_video(str(my_link.get()))


submit_button = Button(yejidtube, text="DOWNLOAD VIDEO", width=34, bg="white", fg="black", font=('bolder', 10), command=downloadvideo)
submit_button.place(x=200, y=260)

reply_box = Label(yejidtube, text="NOTE: \n *Enter the correct youtube link for downloading \n * Click download video and wait for it to download \n *Your downloaded video will be stored in c:/yetube", fg="red", bg="black")
reply_box.place(x=210, y=400)

yejidtube.mainloop()

