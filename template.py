import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import tkinter.messagebox as messagebox

def organize_files(directory):
    files = os.listdir(directory)

    file_groups = {}
    for file in files:
        _, extension = os.path.splitext(file)
        if extension not in file_groups:
            file_groups[extension] = []
        file_groups[extension].append(file)

    for extension, files in file_groups.items():
        if extension in [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".avif", ".webp", ".svg", ".JPEG", ".JPG", ".PNG", ".BMP", ".GIF", ".TIFF", ".AVIF", ".WEBP", ".SVG"]:
            subfolder = "_Images"
        elif extension in [".mp3", ".wav", ".wma", ".aac", ".ogg", ".flac", ".m4a", ".aiff", ".alac"]:
            subfolder = "_Audio"
        elif extension in [".ai", ".psd", ".svg", ".eps", ".indd", ".ai", ".PSD", ".SVG", ".EPS", ".INDD", ".AI"]:
            subfolder = "_Adobe Files"
        elif extension in [".exe", ".msi", ".dmg", ".pkg"]:
            subfolder = "_Executables"
        elif extension in [".txt", ".doc", ".docx", ".pdf", ".rtf", ".odt", ".xls", ".xlsx", ".csv"]:
            subfolder = "_Documents"
        elif extension in [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"]:
            subfolder = "_Compressed"
        elif extension in [".avi", ".mp4", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".vob", ".ogv", ".ogg", ".drc", ".gifv", ".mng", ".avi", ".mts", ".m2ts", ".ts", ".mov", ".qt", ".wmv", ".yuv", ".rm", ".rmvb", ".asf", ".amv", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".m2v", ".m4v", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv", ".f4v", ".f4p", ".f4a", ".f4b"]:
            subfolder = "_Videos"
        elif extension in [".PY", ".py", ".pyw"]:
            subfolder = "_Python Files"
        else:
            subfolder = "_Other"

        subfolder_path = os.path.join(directory, subfolder)
        if not os.path.exists(subfolder_path):
            os.mkdir(subfolder_path)

        for file in files:
            if os.path.isfile(os.path.join(directory, file)):
                shutil.move(os.path.join(directory, file), subfolder_path)

def on_browse_clicked():
    browse_button.config(state="disabled")
    organize_button.config(state="disabled")
    show_terms_and_conditions()
    directory = filedialog.askdirectory()
    directory_label.config(text=directory)
    browse_button.configure(image=select_folder_img)

def on_organize_clicked():
    directory = directory_label["text"]
    if directory:
        organize_files(directory)
        messagebox.showinfo("File Organizer", "Done!")
    organize_button.configure(image=organize_img)

from TermsAndConditions import TermsAndConditions

def show_terms_and_conditions():
    if not os.environ.get('APP_TERMS_ACCEPTED', False):
        terms_window = tk.Toplevel()
        terms_window.title("Terms and Conditions  |  Privacy Policy")
        terms_window.geometry("500x300")
        terms_window.minsize(width=500, height=300)
        terms_window.resizable(False, False)

        terms = TermsAndConditions()

        # Create a Text widget to display the terms and conditions
        terms_text = tk.Text(terms_window, wrap="word")
        # Insert the text into the Text widget
        terms_text.insert("1.0", terms.get_text())
        terms_text.config(state="disabled")

        # Create a Scrollbar widget and attach it to the Text widget
        terms_scrollbar = tk.Scrollbar(terms_window, orient="vertical", command=terms_text.yview)
        terms_text.config(yscrollcommand=terms_scrollbar.set)

        # Pack the Text and Scrollbar widgets
        terms_scrollbar.pack(side="right", fill="y")
        terms_text.pack(expand=True, fill="both")

        agree_var = tk.IntVar()
        agree_checkbox = tk.Checkbutton(terms_window, text="I agree to all", variable=agree_var)
        agree_checkbox.pack()
        start_button = tk.Button(terms_window, text="Start Organizing", command=lambda: on_start_clicked(agree_var, terms_window))
        start_button.pack()
        terms_window.geometry(root.geometry())
    else:
        browse_button.config(state="normal")
        organize_button.config(state="normal")

def on_start_clicked(agree_var, terms_window):
    if agree_var.get() == 1:
        os.environ['APP_TERMS_ACCEPTED'] = 'True'
        terms_window.destroy()
        browse_button.config(state="normal")
        organize_button.config(state="normal")
    else:
        messagebox.showerror("Terms and Conditions", "You must agree to the terms and conditions  |  Privacy Policy before you can use the Data Mop software.")

root = tk.Tk()
root.title("Data Mop")
root.configure(bg="white")
root.resizable(width=False, height=False)

top_frame = tk.Frame(root)
top_frame.pack(side="top", padx=30, pady=60)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 350
window_height = 450

x_coord = (screen_width/2) - (window_width/2)
y_coord = (screen_height/2) - (window_height/2)

root.geometry("{}x{}+{}+{}".format(window_width, window_height, int(x_coord), int(y_coord)))

logo_frame = tk.Frame(root, height=5, bg="white")
logo_frame.pack(side='bottom', fill='x')
logo = tk.PhotoImage(file = "images/logo_datamop.png")
logo_label = tk.Label(logo_frame, image=logo, bg="white")
logo_label.pack()

directory_label = tk.Label(root, text="")
directory_label.pack()

select_folder_img = PhotoImage(file="images/s_folder.png").subsample(1,1)
organize_img = PhotoImage(file="images/organize.png").subsample(1,1)

browse_button = tk.Button(root, image=select_folder_img, command=on_browse_clicked, state="disabled", relief="flat", fg="white")
browse_button.pack()

directory_label = tk.Label(directory_label, bg="white", text="No Folder Selected")
directory_label.pack()

organize_button = tk.Button(root, image=organize_img, command=on_organize_clicked, state="disabled", relief="flat", fg="white")
organize_button.pack()

root.after(500, show_terms_and_conditions)
root.mainloop()

directory_label = tk.Label(root, text="", font=("Helvetica", 11, "bold"), bg="white")
directory_label.pack()

browse_button = tk.Button(root, width=225, height=78, command=on_browse_clicked, font=("Helvetica", 11, "bold"), fg="white")
browse_button.configure(image=select_folder_img)
browse_button.pack()

organize_button = tk.Button(root, width=180, height=62, command=on_organize_clicked, font=("Helvetica", 11, "bold"), fg="white")
organize_button.configure(image=organize_img)
organize_button.pack()

root.mainloop()