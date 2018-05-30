from PIL import Image, ImageTk
import tkinter

image_list = ['1.jpg', '2.gif', '3.jpg']
image_list = ["images/"+f for f in image_list]
text_list = ['apple', 'bird', 'cat']
current = 0


def move(delta):

    global current, image_list
    if not (0 <= current + delta < len(image_list)):
        # tkinter.MessageBox.showinfo('End', 'No more image.')
        print("NO MORE IMAGES")
        return
    current += delta
    image = Image.open(image_list[current])
    photo = ImageTk.PhotoImage(image)
    # label['text'] = text_list[current]   # to display text below the picture
    label['image'] = photo
    label.photo = photo


root = tkinter.Tk()

label = tkinter.Label(root, compound=tkinter.TOP)
label.pack()

frame = tkinter.Frame(root)
frame.pack()


tkinter.Button(frame, text='Previous picture',
               command=lambda: move(-1)).pack(side=tkinter.LEFT)
tkinter.Button(frame, text='Next picture',
               command=lambda: move(+1)).pack(side=tkinter.LEFT)
tkinter.Button(frame, text='Quit', command=root.quit).pack(side=tkinter.LEFT)


move(0)

root.mainloop()
