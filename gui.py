import tkinter as tk
from yt_dl import yt_dl


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

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

row_cnt = 0

entry = tk.Entry(frame)
entry.grid(row=row_cnt, column=0, sticky="ew")

entry.bind("<Return>", add_to_list)

# Submit button
entry_btn = tk.Button(frame, text="Submit", command=add_to_list)
entry_btn.grid(row=row_cnt, column=1)

row_cnt += 1

# spacer
frame.grid_rowconfigure(row_cnt, minsize=20)  # row 1 is now 20px tall
row_cnt += 1

# Format selector
frame_format = tk.Frame(frame)
frame_format.grid(row=row_cnt, column=0, sticky="nsew")
format3_btn = tk.Button(frame_format, text="mp3", command=lambda: print('pressed mp3'))
format4_btn = tk.Button(frame_format, text="mp4", command=lambda: print('pressed mp4'))
format3_btn.grid(row=0, column=0)
format4_btn.grid(row=0, column=1)

row_cnt += 1

# Location Selector
print(row_cnt)
frame_location = tk.Frame(frame)
frame_location.grid(row=row_cnt, column=0, columnspan=2, sticky="nsew")
frame_location.columnconfigure(1, weight=1)

location_btn = tk.Button(frame_location, text="Save Location", command=lambda: print('pressed browse'))
location_btn.grid(row=0, column=0, sticky='w')
location_entry = tk.Entry(frame_location)
location_entry.grid(row=0, column=1, sticky="ew")

row_cnt += 1

# processed files list
text_list = tk.Listbox(frame)
text_list.grid(row=row_cnt, column=0, columnspan=2, sticky="nsew")

row_cnt += 1

root.mainloop()

# URL 
# Format (mp3/mp4)
# Location (default downloads)

# List of downloaded items