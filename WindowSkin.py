import tkinter as tk

class WindowSkin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x200")
        self.root.configure(bg='white')
        self.root.title("Custom Window Skin")

        # Create a label to display the background image
        self.background_label = tk.Label(self.root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Set the background image
        self.background_image = tk.PhotoImage(file="images/background.png")
        self.background_label.configure(image=self.background_image)

# Create the main window
root = tk.Tk()

# Create an instance of the WindowSkin class
window_skin = WindowSkin(root)

# Run the main loop
root.mainloop()
