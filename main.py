from tkinter import *


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        undo_stack = []
        num = StringVar()
        num.set(0)
        self.label = Entry(text=num, justify=RIGHT)
        self.label.pack()

        Button(text=1).place(x=0, y=50)
        Button(text=2).place(x=75, y=50)
        Button(text=3).place(x=150, y=50)
        Button(text=4).place(x=230, y=50)
        Button(text=5).place(x=310, y=50)
        Button(text=6).place(x=0, y=75)
        Button(text=7).place(x=75, y=75)
        Button(text=8).place(x=150, y=75)
        Button(text=9).place(x=230, y=75)
        Button(text=0).place(x=310, y=75)
        Button(text="/").place(x=0, y=100)
        Button(text="*").place(x=75, y=100)
        Button(text="-").place(x=150, y=100)
        Button(text="+").place(x=230, y=100)
        Button(text="=").place(x=310, y=100)

    def on_button_click(self, value):
        pass

def main():
    root = Tk()
    root.title("")
    root.geometry("300x300")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()
