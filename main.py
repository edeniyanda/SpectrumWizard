from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from colorthief import ColorThief
import os


root = Tk()


width=797
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.title("SpectrumWizard")
# root.resizable(0,0)
root.iconbitmap("images/color-wheel.ico")


def spectrumize():
    # Use ColorThief to extract colors from the image
    try:
        ct = ColorThief(filename)
        palette = ct.get_palette(color_count=11)
    except:
        messagebox.showerror("Error","Upload an Image to Spectrumize")
        return

    colorls = []
    rgbcolor = []
    # print(palette)
    for i in range(10):
        rgbcolor.append(f"{palette[i][0]}, {palette[i][1]}, {palette[i][2]}")
    print(rgbcolor)
    
    for i in range(10):
        # Convert RGB values to hexadecimal color codes
        colorls.append(f"#{palette[i][0]:02x}{palette[i][1]:02x}{palette[i][2]:02x}")
    lstids1 = [id1,id2,id3,id4,id5]
    lstids2 = [id6,id7,id8,id9,id10]
    lsthexes1 = [hex1,hex2,hex3,hex4,hex5]
    lsthexes2 = [hex6,hex7,hex8,hex9,hex10]
    
        
    # Update the colors in the canvas and labels
    for i in lstids1:
        colour.itemconfig(i, fill=colorls[i])
    for i in lstids2:
        colour2.itemconfig(i, fill=colorls[5+lstids2.index(i)])
    
    def supply_rgb():
        for i in lsthexes1:
            i.config(state='normal')
            i.delete("1.0", END)
            # Insert the new text
            i.insert(END, rgbcolor[lsthexes1.index(i)+1])
            i.config(state='disabled')   
            
        for i in lsthexes2:    
            i.config(state='normal')
            i.delete("1.0", END)
            # Insert the new text
            i.insert(END, rgbcolor[5+lsthexes2.index(i)])
            i.config(state='disabled')   
        
    def supply_hex():   
        for i in lsthexes1: 
            i.config(state='normal')
            i.delete("1.0", END)
            # Insert the new text
            i.insert(END, colorls[lsthexes1.index(i)+1])
            i.config(state='disabled')   
        
        for i in lsthexes2:    
            i.config(state='normal')
            i.delete("1.0", END)
            # Insert the new text
            i.insert(END, colorls[5+lsthexes2.index(i)])
            i.config(state='disabled')   

    print("Yo")
    if selection.get() == "Hex Value":
        return supply_hex()
    elif selection.get() == "RGB value":
        return supply_rgb()

def showimage():
    global img_lbl
    global filename
    # Open a file dialog to select an image file
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                          filetypes=(("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp"),
                                                     ("All files", "*.*")))
    
    # Open and display the selected image using PIL
    if filename:
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        img_lbl.configure(image=img, width=290, height=290)
        img_lbl.image = img  # Update the image reference to avoid garbage collection
        # img_lbl.config(width=img.width(), height=img.height())  # Update width and height of img_lbl



frame1 = Frame(root, width=797, height=100, bg="#11D78F")
frame1.place(x=0,y=0)

frame2 = Frame(root, width=654, height=380, bg="#575454")
frame2.place(x=70, y=60)

frame3 = Frame(frame2, width=310, height=353, bg ="#EEEED5")
frame3.place(x=10, y=10)

frame4 = Frame(frame2, width=310, height=353, bg ="#EEEED5")
frame4.place(x=330, y=10)

logo_image = PhotoImage(file="images/color-wheel.png")
logo_label = Label(frame3, image=logo_image)
logo_label.place(x=20, y=20)

name_label = Label(frame3, text="SpectrumWizard", font=("Helvet 15 bold"))
name_label.place(x=90, y=40)

# Color canvas on the left side
colour = Canvas(frame3, bg="#EEEED5", width=150, height=265, bd=0)
colour.place(x=10, y=90)


id1 = colour.create_rectangle((10,10,50,50),fill="#b8255f")
id2 = colour.create_rectangle((10,50,50,100),fill="#b8255f")
id3 = colour.create_rectangle((10,100,50,150),fill="#b8255f")
id4 = colour.create_rectangle((10,150,50,200),fill="#b8255f")
id5 = colour.create_rectangle((10,200,50,250),fill="#b8255f")


def copy_text(event):
    # Get the selected text
    selected_text = event.widget.get("sel.first", "sel.last")
    # Copy the text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(selected_text)

# Create a Text widget instead of Label
hex1 = Text(colour, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex1.insert(END, "#b8255f")
hex1.config(state='disabled')
hex1.place(x=60, y=20)

hex2 = Text(colour, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex2.insert(END, "#b8255f")
hex2.config(state='disabled')
hex2.place(x=60, y=65)

hex3 = Text(colour, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex3.insert(END, "#b8255f")
hex3.config(state='disabled')
hex3.place(x=60, y=110)

hex4 = Text(colour, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex4.insert(END, "#b8255f")
hex4.config(state='disabled')
hex4.place(x=60, y=160)

hex5 = Text(colour, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex5.insert(END, "#b8255f")
hex5.config(state='disabled')
hex5.place(x=60, y=210)

# Bind the Ctrl+C event to copy the selected text
hex1.bind("<Control-c>", copy_text)
hex2.bind("<Control-c>", copy_text)
hex3.bind("<Control-c>", copy_text)
hex4.bind("<Control-c>", copy_text)
hex5.bind("<Control-c>", copy_text)

# Color canvas on the right side
colour2 = Canvas(frame3, bg="#EEEED5", width=150, height=265, bd=0)
colour2.place(x=170, y=90)

id6 = colour2.create_rectangle((10,10,50,50),fill="#b8255f")
id7 = colour2.create_rectangle((10,50,50,100),fill="#b8255f")
id8 = colour2.create_rectangle((10,100,50,150),fill="#b8255f")
id9 = colour2.create_rectangle((10,150,50,200),fill="#b8255f")
id10 = colour2.create_rectangle((10,200,50,250),fill="#b8255f")


hex6= Label(colour2, text="#b8255f",fg="#000", font=("arial 12 bold"), bg="#EEEED5")
# hex6.place(x=60, y=20)
hex6 = Text(colour2, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex6.insert(END, "#b8255f")
hex6.config(state='disabled')
hex6.place(x=60, y=20)

hex7 = Text(colour2, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex7.insert(END, "#b8255f")
hex7.config(state='disabled')
hex7.place(x=60, y=65)

hex8 = Text(colour2, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex8.insert(END, "#b8255f")
hex8.config(state='disabled')
hex8.place(x=60, y=110)


hex9 = Text(colour2, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex9.insert(END, "#b8255f")
hex9.config(state='disabled')
hex9.place(x=60, y=160)

hex10 = Text(colour2, width=10, height=1, fg="#000", font=("arial 12 bold"), bg="#EEEED5")
hex10.insert(END, "#b8255f")
hex10.config(state='disabled')
hex10.place(x=60, y=210)

# Bind the Ctrl+C event to copy the selected text
hex6.bind("<Control-c>", copy_text)
hex7.bind("<Control-c>", copy_text)
hex8.bind("<Control-c>", copy_text)
hex9.bind("<Control-c>", copy_text)
hex10.bind("<Control-c>", copy_text)

btn_upload = Button(frame4, 
        text="Upload Image", 
        font=("Helvet 10"),bg="cornflowerblue",
        fg="white", cursor="hand2", activebackground="white", 
        activeforeground="black", width=15, height=2, command=showimage)
btn_upload.place(x=10, y=300)

btn_spectrumize = Button(frame4, 
        text="Spectrumize", 
        font=("Helvet 10"),bg="#d92938", 
        fg="white", 
        cursor="hand2", 
        activeforeground="black", 
        width=15, 
        height=2,
        highlightthickness=2,
        highlightbackground="green", 
        command=spectrumize)

btn_spectrumize.place(x=170, y=300)

selection = StringVar()
cb_option = ttk.Combobox(frame1, value=["Hex Value", "RGB value"], state="r", width=15, textvariable=selection)
cb_option.place(x=650, y=10)
cb_option.set("Hex Value")

picture_frame = Frame(frame4, width=290, height=290, bg="black", relief=GROOVE)
picture_frame.place(x=10, y=5)

img_lbl = Label(picture_frame, bg="black")
img_lbl.place(x=0, y=0)




root.mainloop()