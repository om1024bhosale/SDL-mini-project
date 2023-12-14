import tkinter as tk
import pyshorteners
import pyperclip

def shorten_url():
    long_url = entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    result_label.config(text="Shortened URL: " + short_url)

def copy_url():
    short_url = result_label.cget("text").replace("Shortened URL: ", "")
    pyperclip.copy(short_url)

window = tk.Tk()
window.title("URL Shortener")

window.geometry("500x300")

label = tk.Label(window, text="Enter a URL:")
label.pack()
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Shorten", command=shorten_url)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

copy_button = tk.Button(window, text="Copy URL", command=copy_url)
copy_button.pack()

window.mainloop()
