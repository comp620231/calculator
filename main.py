from tkinter import *

expression = ""
class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.input_field = Entry(self, font='Arial 15 bold', width=24, state="readonly")
        self.input_field.pack(fill=BOTH)

        buttons = (('7', '8', '9', '/', '4'),
                   ('4', '5', '6', '*', '4'),
                   ('1', '2', '3', '-', '4'),
                   ('0', '.', '=', '+', '4')
                   )

        expression = ""

        button = Button(text='C', command=lambda: self.bt_clear())
        button.grid(row=1, column=3, sticky="nsew")

        for row in range(4):
            for col in range(4):
                Button( width=2, height=3, text=buttons[row][col],
                       command=lambda row=row, col=col: self.btn_click(buttons[row][col])).grid(row=row + 2, column=col,
                                                                                           sticky="nsew", padx=1,
                                                                                           pady=1)

    def btn_click(self,item):
        global expression
        try:
            self.input_field['state'] = "normal"
            expression += item
            self.input_field.insert(END, item)

            if item == '=':
                result = str(eval(expression[:-1]))
                self.input_field.insert(END, result)
                expression = ""

            self.input_field['state'] = "readonly"
        except ZeroDivisionError:
            self.input_field.delete(0, END)
            self.input_field.insert(0, 'Ошибка (деление на 0)')
        except SyntaxError:
            self.input_field.delete(0, END)
            self.input_field.insert(0, 'Ошибка')

    def bt_clear(self):
        global expression
        self.input_field['state'] = "normal"
        self.input_field.delete(0, END)
        self.input_field['state'] = "readonly"

def main():
    root = Tk()
    root.title("")
    root.geometry("300x300")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()

#Поторапливатесь с проектом у нас дедлайн!!!!!!!!!!!