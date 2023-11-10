import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Left Menu with 2 Items and 2 Frames")
        self.geometry("400x400")

        # Create the left menu
        self.left_menu = tk.Frame(self, bg="gray")
        self.left_menu.pack(side=tk.LEFT, fill=tk.Y)

        # Create the two menu items
        self.menu_item1 = tk.Button(self.left_menu, text="Item 1")
        self.menu_item1.pack()
        self.menu_item2 = tk.Button(self.left_menu, text="Item 2")
        self.menu_item2.pack()

        # Create the two frames
        self.frame1 = tk.Frame(self)
        self.frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.frame2 = tk.Frame(self)
        self.frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create the two buttons in the first frame
        self.button1 = tk.Button(self.frame1, text="Button 1")
        self.button1.pack()
        self.button2 = tk.Button(self.frame1, text="Button 2")
        self.button2.pack()

        # Create the label in the second frame
        self.label = tk.Label(self.frame2, text="Label")
        self.label.pack()

        # Bind the menu items to the frames
        self.menu_item1.bind("<Button-1>", self.show_frame1)
        self.menu_item2.bind("<Button-1>", self.show_frame2)

    def show_frame1(self, event):
        self.frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.frame2.pack_forget()

    def show_frame2(self, event):
        self.frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.frame1.pack_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()