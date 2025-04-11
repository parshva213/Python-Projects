import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text='C', width=21, command=self.clear_entry).grid(row=5, column=0, columnspan=4)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

calculator = Calculator(root)
root.mainloop()




'''#import file
import tkinter as abc
from tkinter import font as xyz

#simple calculator (sc) +,-,*,/,% operator
def sc(a,op,b):
    if op=='+':
        result=a+b
    elif op=='-':
        result=a-b
    elif op=='*':
        result=a*b
    elif op=='/':
        result=a/b
    elif op=='%':
        result=a%b
    else:
        op_lable.config(text='ENTER PERFECT OPERATOR')
    z=result
    result=f'{a}  {op}  {b}  =  {z}'
    return result

#input function to take submit value
def input():
    try:
        a=int(a_input.get())
        op=op_input.get()
        b=int(b_input.get())
        o_p=sc(a,op,b)
        r_lable.config(text=o_p)
    except ValueError:
        result_lable.config(text='ENTER VALID DETAIL')
        
#clear_entry function and labels
def clear_entry():
    a_input.delete(0,abc.END)
    op_input.delete(0,abc.END)
    b_input.delete(0,abc.END)
    r_lable.config(text=' ')
    op_lable.config(text='ENTER OPERATOR \n +,-,*,/,%.')


#sc window
window=abc.Tk()
window.title('SIMPLE CALCULATOR')
window.geometry('5000x5000')

#sc font
RCB = xyz.Font(font='bold',size=15)

#value1 input and label
a_lable=abc.Label(window,text='ENTER NUMBER',font=RCB)
a_lable.pack(pady=10)
a_input=abc.Entry(window ,font=RCB,width=10,justify='center')
a_input.pack(pady=10)

#operator input and label
op_lable=abc.Label(window,text='ENTER OPERATOR \n +,-,*,/,%.',font=RCB)
op_lable.pack(pady=10)
op_input=abc.Entry(window ,font=RCB,width=10,justify='center')
op_input.pack(pady=10)

#value2 input and label
b_lable=abc.Label(window,text='ENTER NUMBER',font=RCB)
b_lable.pack(pady=10)
b_input=abc.Entry(window ,font=RCB,width=10,justify='center')
b_input.pack(pady=10)

#submit button
submit_button=abc.Button(window,text='SUBMIT',command=input,font=RCB,padx=10,pady=5)
submit_button.pack()

#result value label
r_lable=abc.Label(window,text=' ',font=RCB)
r_lable.pack(pady=10)

#clear buttun as refresh
clear_button=abc.Button(window,text='REFRESH',command=clear_entry,font=RCB,padx=10,pady=5)
clear_button.pack()

#window reapate again
window.mainloop()
'''
