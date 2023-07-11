from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode='w', filetype=[('text files', '.txt')])
    if new_file is None:
        return
    text = entry.get(1.0, tk.END)  # Changed END to tk.END
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode='r', filetype=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.delete(1.0, tk.END)  # Added tk.END to clear previous content
        entry.insert(tk.INSERT, content)  # Changed INSERT to tk.INSERT

def clearFile():
    entry.delete(1.0, tk.END)  # Changed END to tk.END

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="black")
top = tk.Frame(canvas)  # Changed Frame to tk.Frame
top.pack(padx=10, pady=5, anchor='nw')

b1 = tk.Button(canvas, text="Open", bg="white", command=openFile)  # Changed Button to tk.Button
b1.pack(in_=top, side=tk.LEFT)  # Changed LEFT to tk.LEFT

b2 = tk.Button(canvas, text="Save", bg="white", command=saveFile)  # Changed Button to tk.Button
b2.pack(in_=top, side=tk.LEFT)  # Changed LEFT to tk.LEFT

b3 = tk.Button(canvas, text="Clear", bg="white", command=clearFile)  # Changed Button to tk.Button
b3.pack(in_=top, side=tk.LEFT)  # Changed LEFT to tk.LEFT

b4 = tk.Button(canvas, text="Exit", bg="white", command=canvas.quit)  # Changed exit to canvas.quit
b4.pack(in_=top, side=tk.LEFT)  # Changed LEFT to tk.LEFT

entry = tk.Text(canvas, wrap=tk.WORD, bg="#F9DDA4", font=("poppins", 15))  # Changed Text to tk.Text
entry.pack(padx=10, pady=5, expand=True, fill=tk.BOTH)  # Changed TRUE to tk.TRUE and BOTH to tk.BOTH

canvas.mainloop()
