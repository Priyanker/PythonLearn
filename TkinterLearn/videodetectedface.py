import tkinter as tk
from tkinter import ttk
import facedetvideo as fdv
LARGE_FONT = ("Verdana", 20)


class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Three window app")

        # tk.Tk.wm_resizable(self, width=False, height=False)
        # tk.Tk.wm_resizable(self, 0,0)

        tk.Tk.wm_geometry(self, newGeometry='500x500')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, PageOne):
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
    fdv.video()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Capture Window",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=50, padx=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Video Capture", font=LARGE_FONT)
        label.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="VideoCapture",
                             command=ui, width=60)

        button2.pack(pady=10, padx=10)


if __name__ == "__main__":
    app = Windows()
    app.mainloop()
