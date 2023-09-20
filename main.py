from tkinter import *


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass

def main():
    root = Tk()
    root.title("TEST")
    root.geometry("300x300")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()