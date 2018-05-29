from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import copy
from PIL import Image, ImageTk
LARGE_FONT = ("Verdana", 12)
file_path = ''


class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Three window app")
        #tk.Tk.wm_geometry(self, newGeometry='900x100')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, PageOne, PageTwo):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def q():
    print("damn")


def q1(param):
    print(param)


def ui():
    global file_path
    file_path = filedialog.askopenfilename()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))

        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Number One", font=LARGE_FONT)
        label.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    img = None
    count1 = 0
    count2 = 0

    def showImg(self):
        try:
            load = Image.open(file_path)

            render = ImageTk.PhotoImage(load)
            self.img = tk.Label(self, image=render)
            self.img.image = render
            self.img.pack()
            self.count1 = self.count1 + 1
        except AttributeError as e:
            print("Please Upload the image")

    def clearImg(self):
        self.img.pack_forget()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Number Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # we use ttk for little bit more stylish buttons. Otherwise tk.Button for general buttons
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Back to Page One",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack(pady=10, padx=10)

        button3 = ttk.Button(self, text="Upload",
                             command=ui)

        button3.pack(pady=10, padx=10)
        try:

            button4 = ttk.Button(self, text="Show Image",
                                 command=self.showImg)

            button4.pack(pady=10, padx=10)

            button5 = ttk.Button(self, text="Clear",
                                 command=self.clearImg)

            button5.pack(pady=10, padx=10)

        except AttributeError as e:
            print("Please Upload the image")


if __name__ == "__main__":
    app = Windows()
    app.mainloop()
    # print(file_path)
