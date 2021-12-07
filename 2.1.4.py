#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window

root = tk.Tk()
root.wm_geometry("200x200")


frame_login = tk.Frame(root)
frame_login.grid()
lbl_username = tk.Label(frame_login, text='Username:', font='Courier')
lbl_username.pack(padx=50)
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
lbl_password = tk.Label(frame_login, text='Password:', font='Courier')
lbl_password.pack(pady=5, padx=50)
ent_username = tk.Entry(frame_login, bd=3, show='*')
ent_username.pack(pady =5)
btn_login= tk.Button(frame_login, text='Login')
btn_login.pack(pady=5)

oldtitle = root.title()
root.title('Authorization')


root.mainloop()