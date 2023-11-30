from PIL import Image, ImageTk
import tkinter as tk
import os

root = tk.Tk()
root.overrideredirect(1)
root.attributes("-topmost", True)

logo = Image.open("images/splash.png")
logo_width, logo_height = logo.size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
pos_x = int((screen_width - logo_width) / 2)
pos_y = int((screen_height - logo_height) / 2)
root.geometry("+{}+{}".format(pos_x, pos_y))

logo_img = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image = logo_img)
logo_label.pack()

def fade_out():
    for i in range(100, 0, -5):
        root.attributes("-alpha", i/100)
        root.update()
        root.after(50)
    root.destroy()

root.after(2000, fade_out)
root.mainloop()


# Run main file
import app
