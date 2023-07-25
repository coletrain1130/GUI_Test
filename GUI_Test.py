import tkinter as tk
import webbrowser
import subprocess

# Define a function to be called when the button is clicked
def button_click():
    url = "https://www.youtube.com/watch?v=LDU_Txk06tM"
    webbrowser.open(url)

def button_click2():
    app_path = "C:\\Program Files (x86)\\Steam\\steam.exe"
    subprocess.Popen(app_path)

def button_click3():
    app_path = "C:\\Users\\jacobcole\\AppData\\Local\\Programs\\Microsoft VS Code Insiders\\Code - Insiders.exe"
    subprocess.Popen(app_path)

def button_click4():
    app_path = "C:\\Users\\jacobcole\\AppData\\Local\\Discord\\app-1.0.9013\\Discord.exe"
    subprocess.Popen(app_path)

def close_program():
    window.destroy()


# Create a window
window = tk.Tk()
window.title("Buttons O' Wonder!")
window.geometry("300x200")

# Change the background color of the window
window.configure(bg="black")

# Create a label
label = tk.Label(window, text="Buttons O' Plenty!", bg="black", fg="white")
label.grid(row=0, column=1, columnspan=1, pady=10)

# Create a button
button = tk.Button(window, text="YouTube", command=button_click, bg="red", fg="white")
button.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(window, text="Steam", command=button_click2, bg="#0E2450", fg="white")
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tk.Button(window, text="VS Code Insiders", command=button_click3, bg="#5CBCA6", fg="white")
button3.grid(row=1, column=2, columnspan=1, padx=10, pady=10)

button4 = tk.Button(window, text="Discord", command=button_click4, bg="#747Bf0", fg="white")
button4.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

close_button = tk.Button(window, text="Close", command=close_program, bg="gray", fg="white")
close_button.grid(row=2, column=2, columnspan=1, padx=10, pady=10)

# Run the window
window.mainloop()