import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import tkinter.messagebox as messagebox

class FileOrganizer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Organizer")
        self.window.geometry("250x160")

        self.directory = ""

        self.directory_label = tk.Label(self.window)
        self.directory_label.pack()

        self.browse_button = tk.Button(self.window, text="Browse", command=self.on_browse_clicked)
        self.browse_button.pack()

        self.organize_button = tk.Button(self.window, text="Organize", command=self.on_organize_clicked)
        self.organize_button.pack()

    def organize_files(self, directory):
        files = os.listdir(directory)

        file_groups = {}
        for file in files:
            _, extension = os.path.splitext(file)
            if extension not in file_groups:
                file_groups[extension] = []
            file_groups[extension].append(file)

        for extension, files in file_groups.items():
            if extension in [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".avif", ".webp", ".svg", ".JPEG", ".JPG", ".PNG", ".BMP", ".GIF", ".TIFF", ".AVIF", ".WEBP", ".SVG"]:
                subfolder = "Images"
            elif extension in [".mp3", ".wav", ".wma", ".aac", ".ogg", ".flac", ".m4a", ".aiff", ".alac"]:
                subfolder = "Audio"
            elif extension in [".ai", ".psd", ".svg", ".eps", ".indd", ".ai", ".PSD", ".SVG", ".EPS", ".INDD", ".AI"]:
                subfolder = "Adobe Files"
            elif extension in [".exe", ".msi", ".dmg", ".pkg"]:
                subfolder = "Executables"
            elif extension in [".txt", ".doc", ".docx", ".pdf", ".rtf", ".odt", ".xls", ".xlsx", ".csv"]:
                subfolder = "Documents"
            elif extension in [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"]:
                subfolder = "Compressed"
            elif extension in [".avi", ".mp4", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".vob", ".ogv", ".ogg", ".drc",
                               ".gifv", ".mng", ".avi", ".mts", ".m2ts", ".ts", ".mov", ".qt", ".wmv", ".yuv", ".rm",
                               ".rmvb", ".asf", ".amv", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".m2v", ".m4v", ".svi",
                               ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv", ".f4v", ".f4p", ".f4a", ".f4b"]:
                subfolder = "Videos"
            elif extension in [".PY", ".py", ".pyw"]:
                subfolder = "Python Files"
            else:
                subfolder = "Other"

            subfolder_path = os.path.join(directory, subfolder)
            if not os.path.exists(subfolder_path):
                os.mkdir(subfolder_path)

            for file in files:
                shutil.move(os.path.join(directory, file), subfolder_path)

        def on_browse_clicked(self):
            self.directory = filedialog.askdirectory()
            self.directory_label.config(text=self.directory)

        def on_organize_clicked(self):
            if self.directory:
                self.organize_files(self.directory)
                messagebox.showinfo("File Organizer", "Done!")

        def mainloop(self):
            self.window.mainloop()

