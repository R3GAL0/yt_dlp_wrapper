import tkinter as tk

# tk._test()


root = tk.Tk()
root.title("Youtube to mp3/mp4")

# def on_click():
#     print("Testing")
#     lbl.config(text="Button Clicked?")

# lbl = tk.Label(root, text="Label 1")
# lbl.grid(row=0, column=2)

# # print(lbl.config().keys())

# btn = tk.Button(root, text="Submit", command=on_click)
# btn.grid()

def add_to_list(event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)

frame = tk.Frame(root)
frame.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

entry.bind("<Return>", add_to_list)

entry_btn = tk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0)

root.mainloop()

# URL 
# Format (mp3/mp4)
# Location (default downloads)

# List of downloaded items