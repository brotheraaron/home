import tkinter
import customtkinter
from pytube import YouTube
from pytube.innertube import _default_clients
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

def quit_app():
    exit()

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress,use_oauth=False,allow_oauth_cache=True)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="black")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except Exception as e:
        finishLabel.configure(text="Download Error", text_color="red")
        print(e)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size  * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    progressBar.set(float(percentage_of_compeletion / 100))

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.geometry("520x280")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(padx=10, pady=10)

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

exit_app = customtkinter.CTkButton(app, text="Exit", command=quit_app).pack(side="right",padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload).pack(side="right",padx=10, pady=10)

app.mainloop()
