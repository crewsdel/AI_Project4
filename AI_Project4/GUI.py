import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Setup main window
window = tk.Tk()
window.title("Recyclable Material Classification")
window.minsize(width=900, height=600)
frameMain = tk.Frame(master=window, relief="sunken", borderwidth=8, padx=5, pady=5)
frameMain.grid(column=2, row=1, padx=5, pady=5)
# Setup main window

# For tabs on the top of the window: Upload | Help
menuOptions = tk.Menu(window)
window.config(menu= menuOptions)
uploadMenu = tk.Menu(menuOptions)
menuOptions.add_cascade(label="Upload", menu=uploadMenu)
uploadMenu.add_command(label="Upload Image", command=lambda: window.event_generate("<<OpenUploadWindow>>"))
helpMenu = tk.Menu(menuOptions)
menuOptions.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="How to use", command=lambda: window.event_generate("<<OpenHelpWindow>>"))
helpMenu.add_command(label="Makers", command=lambda: window.event_generate("<<OpenMakerWindow>>"))
# For tabs on the top of the window: Upload | Help


greeting = tk.Label(master=frameMain, text="Import custom image: ")
button = tk.Button(
    text="Upload Image",
    bg="blue",
    fg="white",
    width=20,
    height=5,
    master=frameMain
)
output = tk.Listbox(master=frameMain, height=40, width=150)
canvas = tk.Canvas(master=frameMain, height=150, width=150)

def openFileExplorer(event):
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("All files", "*.jpg *.png"), ("JPG files", "*.jpg"),
                                                     ("PNG files", "*.png")))
    if filename:
        img = Image.open(filename)
        img = img.resize((150, 150))  # Resize image to 150x150
        img = ImageTk.PhotoImage(img)
        canvas.image = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.config(width=150, height=150)  # Set canvas size to 150x150
        output.insert(tk.END, "File opened: " + filename)

def openHelpWindow(event):
    newWindow = tk.Toplevel(window)
    newWindow.title("How to use")
    newWindow.geometry("500x200")
    #add text here explaining things
    newWindow.resizable(False, False)
    helpInfo = tk.Label(master=newWindow, text="To use this program you need to select an image from your \n"
                                               "computer, using the upload button or tab.\n\n"
                                               "The upload button to the right side of the screen allows you to upload images\n"
                                               "of type .JPG or .PNG files.\n\n"
                                               "This program is an image recognition tool that recognizes the picture\n"
                                               "given and returns a percentage of correctness for a certain type of\n "
                                               "recyclable material, including types: paper, plastic, metal, or glass.")

    helpInfo.pack()

def openMakerWindow(event):
    newWindow = tk.Toplevel(window)
    newWindow.title("Who made this program")
    newWindow.geometry("500x200")
    newWindow.resizable(False, False)
    names = tk.Label(master=newWindow, text="Aubrey Burke: Data Acquisition and Preprocessing\n\n\n"
                                            "Delanie Crews: Machine Learning Model and Development\n\n\n"
                                            "Sebastian Tyo: Application Development and User Interface\n\n\n"
                                            "Brandon Rocha: Documentation, Project Management, and Testing")
    names.pack()


# Bind the actions to functions, when pressed do action, bind action to function so it runs
button.bind("<Button-1>", openFileExplorer)
window.bind("<<OpenUploadWindow>>", openFileExplorer)
window.bind("<<OpenHelpWindow>>", openHelpWindow)
window.bind("<<OpenMakerWindow>>", openMakerWindow)
# Bind the actions to functions, when pressed do action, bind action to function so it runs



#place everything ( think 2x2 box )
output.grid(column=0, row=1, padx=5, pady=5)
canvas.grid(column=1, row=1, padx=5, pady=5)
greeting.grid(column=0, row=0, padx=5, pady=5)
button.grid(column=1, row=0, padx=5, pady=5)

window.mainloop()
