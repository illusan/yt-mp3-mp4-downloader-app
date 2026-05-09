import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.title("yt mp3/mp4 downloader")
app.geometry("800x600")

text = ctk.CTkLabel(app, text="YouTube to mp3 / mp4 conventer", font=("Arial", 40))
text.pack(pady=(30, 0))
text2 = ctk.CTkLabel(app, text="free mp3 and mp4 format converter, compatibile with YouTube", font=("Arial", 17))
text2.pack(pady=(5, 0))

entry = ctk.CTkEntry(app, width=500, placeholder_text="URL")
entry.pack(pady=(30, 0))


combo = ctk.CTkComboBox(app, values=["MP3", "MP4"], width=70)
combo.pack()
combo.set("MP3")

button = ctk.CTkButton(app, text="Download")
button.pack()

text3 = ctk.CTkLabel(app, text="Enter the video URL", font=("Arial", 12))
text3.pack(pady=(5, 0))

frame = ctk.CTkFrame(app, bg_color="transparent")





app.mainloop()