import tkinter as tk
LARGE_FONT = ("Verdana", 12)


class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="bottom", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def q():
    print("damn")


def q1(param):
    print(param)


1


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # button1 = tk.Button(self, text="visit page 1", command=q)

        # this is how to properly pass a func as command when it has parameters
        button1 = tk.Button(self, text="Visit Page 1", command=lambda: q1("tjs"))
        button1.pack(pady=10, padx=10)


if __name__ == "__main__":
    app = Windows()
    app.mainloop()
