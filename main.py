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


frame = ctk.CTkFrame(app, bg_color="transparent")
frame.pack(pady=10)

entry = ctk.CTkEntry(frame, width=500, placeholder_text="enter video URL")
entry.grid(row=0, column=0, padx=10, pady=10)

combo = ctk.CTkComboBox(frame, values=["MP3", "MP4"], width=70)
combo.grid(row=0, column=1, padx=10, pady=10)
combo.set("MP3")

button = ctk.CTkButton(frame, text="Download")
button.grid(row=1, column=0, columnspan=2, pady=20)








app.mainloop()