from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
LARGE_FONT = ("Verdana", 12)
file_path = ''


class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Three window app")

        container = tk.Frame(self)
        container.pack(side="bottom", fill="both", expand=True)
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
        label = tk.Label(self, text="Start page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))

        button2.pack(pady=10, padx=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Number One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack(pady=10, padx=10)


class PageTwo(tk.Frame):

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



if __name__ == "__main__":
    app = Windows()
    app.mainloop()
    print(file_path)
