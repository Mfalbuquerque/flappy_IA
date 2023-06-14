import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title('Bora?')
root.geometry('600x600')
root.configure(background='#ffc8dd')

def move_button_1(e):
    button_1_x = button_1.winfo_x()
    button_1_y = button_1.winfo_y()

    if abs(e.x - button_1_x) < 50 and abs(e.y - button_1_y) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo('Bora', 'Eu te faço um carinho!')

def denied():
    button_1.destroy()

margin = tk.Canvas(root, width=500, bg='#ffc8dd', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = tk.Label(root, bg='#ffc8dd', text='Bora transar?', fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()

button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied, relief='ridge', bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()

root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', command=accepted, relief='ridge', bd=3, font=('Montserrat', 14, 'bold'))
button_2.pack()

root.mainloop()
