import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import shutil
import getpass

def delete_citizenfx_folder():
    username = getpass.getuser()
    folder_path = fr"C:\Users\{username}\AppData\Roaming\CitizenFX"  
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Error")
    else:
        try:
            shutil.rmtree(folder_path)
            messagebox.showinfo("Success", "CitizenFX Removed")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

def delete_digitalentitlements_folder():
    username = getpass.getuser()  
    folder_path = fr"C:\Users\{username}\AppData\Local\DigitalEntitlements"  
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Error")
    else:
        try:
            shutil.rmtree(folder_path)
            messagebox.showinfo("Success", "Unlinked Rockstar Account")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")


root = tk.Tk()
root.title("Cfel Cleaner")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


window_width = 350
window_height = 165


x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)


root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

root.configure(bg='#1E1E1E')


icon_path = "Icon.ico"
if os.path.exists(icon_path):
    root.iconbitmap(default=icon_path)


style = ttk.Style()


style.configure('TButton', font=('Hack', 8, 'bold'), foreground='black', background='#4c325c', width=20, padding=10, borderwidth=3, relief="groove", bordercolor="#4c325c")
style.map('TButton', foreground=[('active', 'black')], background=[('active', '#FEFCFF')])


frame = tk.Frame(root, bg='#1E1E1E')
frame.pack(expand=True, fill='both', padx=20, pady=20)

delete_citizenfx_button = ttk.Button(frame, text="Remove CitizenFX", command=delete_citizenfx_folder)
delete_citizenfx_button.pack(pady=5)

delete_digitalentitlements_button = ttk.Button(frame, text="Unlink Rockstar", command=delete_digitalentitlements_folder)
delete_digitalentitlements_button.pack(pady=5)


note_label = tk.Label(root, text="Discord: .xrein.", fg="#4c325c", bg='#1E1E1E', font=('Segoe UI', 8, 'italic'))
note_label.pack(side=tk.BOTTOM, pady=5)


root.mainloop()
