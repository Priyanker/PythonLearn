import os
import os.path
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import facesdetect as fsd
from PIL import Image, ImageTk
LARGE_FONT = ("Verdana", 22)
file_paths1 = []
current = 0


class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "DETECTING GALLERY")
        # tk.Tk.wm_resizable(self, width=False, height=False)
        # tk.Tk.wm_resizable(self, 0,0)

        tk.Tk.wm_geometry(self, newGeometry='800x700')
        container = tk.Frame(self, background="#2196F3")
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
    global file_paths1
    file_path = filedialog.askopenfilename()
    file_paths1 = fsd.getLocs(file_path)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome!", font=LARGE_FONT, fg='#2196F3')
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Uploading Window",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=50, padx=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Upload your image here", font=LARGE_FONT)
        label.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=20, padx=10)

        button2 = ttk.Button(self, text="Upload",
                             command=ui, width=60)

        button2.pack(pady=20, padx=10)

        button3 = ttk.Button(self, text="Open Gallery",
                             command=lambda: controller.show_frame(PageTwo))
        button3.pack(pady=20)


class PageTwo(tk.Frame):
    label1 = None

    def __init__(self, parent, controller):
        # global label1
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Number Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # we use ttk for little bit more stylish buttons. Otherwise tk.Button for general buttons
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Back to Uploading Window",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack(pady=10, padx=10)

        ttk.Button(self, text='Previous picture',
                   command=lambda: self.move(-1)).pack(side=tk.LEFT)
        ttk.Button(self, text='Next picture',
                   command=lambda: self.move(+1)).pack(side=tk.LEFT)
        ttk.Button(self, text='Quit', command=parent.quit).pack(side=tk.LEFT)

        self.label1 = tk.Label(self, compound=tk.LEFT, width=900, height=900)
        self.label1.pack(padx=30, pady=60)

        self.move(0)

    def move(self, delta):

        global current, file_paths1
        if not (0 <= current + delta < len(file_paths1)):
            # tkinter.MessageBox.showinfo('End', 'No more image.')
            print("NO MORE IMAGES")
            return
        current += delta
        image = Image.open(file_paths1[current])
        photo = ImageTk.PhotoImage(image)
        # label['text'] = text_list[current]   # to display text below the picture
        self.label1['image'] = photo
        self.label1.photo = photo
        self.label1.pack(padx=30, pady=10)


if __name__ == "__main__":
    app = Windows()
    app.mainloop()
    list_dir = os.listdir('D:\Programming\PythonLearn\TkinterLearn\images\JL')
    list_dir = ["images/JL/"+name for name in list_dir]
    # abs_path = [os.path.abspath(path) for path in list_dir]
    # file_paths1 = [os.path.abspath(path) for path in file_paths1]
    for path in list_dir:
        if path not in file_paths1:
            os.remove(path)
