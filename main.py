from pathlib import Path
from tkinter import ttk, font, filedialog
from functools import partial
import tkinter as tk, datetime as dt
from tkinter import simpledialog

#global variables
mainWindow = ""
textPane = ""
menu_bar = None
filePath = ""
exec_dir = Path(__file__).parent
wrap = 0

# TODO: Look over this document for TODO tags. Make sure you have contributed your part on time
# TODO: Brianna and Deon, please claim some of the unclaimed work that needs to be done. Listed below

def stub():
    """
    Placeholder function that throws a `NotImplementedError` exception when called.
    TODO: Removed after all functionality has been implemented.
    Brian Kram
    """
    raise NotImplementedError

def initialize_application_frame():
    """
    Initializes the base application frame. Just the bare minimals.
    Justin Cockrell
    """
    #Very basic tkinter frame. You always have something like this
    print("Now generating the base application frame (Blank)\n\n")
    global mainWindow
    mainWindow = tk.Tk()
    mainWindow.title("Notepad Group Project")
    mainWindow.geometry("800x500")

def toggle_wrap():
    """
    Justin Cockrell.
    Toggles Word in the editor
    """
    global textPane #textPane is global. This is the reference to it.
    global wrap
    if wrap == 0:
        wrap = 1
        textPane.config(wrap=tk.WORD)
    elif wrap == 1:
        wrap = 0
        textPane.config(wrap="none")

def font_window():
    """
    Generates a window to change the font of the text editor. We are only going
    to change text for the whole thing similar to notepad.
    Justin Cockrell
    """
    #Font window local to the function. We only need it in ehre
    fontWindow = tk.Tk()
    fontWindow.title("Choose your font!")
    fontWindow.resizable(0,0)

    #Making the list boxes and placing them
    fontBox = tk.Listbox(fontWindow, height=20, exportselection=False)
    size = tk.Listbox(fontWindow, height=20, exportselection=False)
    style = tk.Listbox(fontWindow, height=20, exportselection=False)
    fontBox.grid(row=0, column=0, sticky="nsew", columnspan=5)
    size.grid(row=0, column=5, sticky="nsew", columnspan=5)
    style.grid(row=0, column=10, sticky="nsew", columnspan=5)

    #Propegate the list boxes using loops
    for f in font.families():
        fontBox.insert('end', f)
    for num in range(8, 72, 2):
        size.insert('end', num)
    for s in "regular", "bold", "italic", "underline":
        style.insert('end', s)

    #Set default font selections so we can't pass a null selection to our function
    fontBox.selection_set(13)
    size.selection_set(4)
    style.selection_set(0)

    #Apply button to apply the font.
    apply = tk.Button(fontWindow, text="Apply", command=partial(get_font,fontBox,size,style))
    apply.grid(row=1, column=1, columnspan=15)

def get_font(type,size,style):
    """
    Action for 'Apply' from the font window. This changes the font to whatever is
    selected
    Justin Cockrell
    """
    #Called by the apply button
    type = type.get(type.curselection())
    size = size.get(size.curselection())
    style = style.get(style.curselection())
    if style == "regular":
        choice = (type,size)
    else:
        choice = (type,size,style)

    textPane.configure(font=choice)
    
 #bryanna: function for searching within program.
def searchTerm():
    global textPane
    textPane.tag_remove('search', '1.0', tk.END)
    wordCount = tk.StringVar()
    #simpledialog was inputed into app to bring up textbox
    userInput = simpledialog.askstring("Search Box", "What are you searching for?")
    myIndex=textPane.search(userInput, "1.0", count=wordCount)
    print(userInput)        #DELETE this- was for debug
    print("index:%s$$$$"%myIndex)   #same here- debug
    
    while myIndex != "":    #function to cycle through all of the file
        print("wordcount: %s $$$" % wordCount.get())#debug
        textPane.tag_add("search",myIndex,"%s + %sc" % (myIndex,wordCount.get()))
        #highlights the searched words/letters in text
        textPane.tag_config("search", background = "yellow", foreground = "black")
        myIndex= textPane.search(userInput,myIndex+" + 1c",stopindex=tk.END, count=wordCount)
        print(myIndex)

#bryanna: function for search and replace.
def searchReplace():    #basically just taking the code from the search function
    global textPane
    wordCount = tk.StringVar()
    userInput = simpledialog.askstring("Search Box", "What are you searching for?")
    replaceWord = simpledialog.askstring("Replace Box", "Replace with what?")
    myIndex=textPane.search(userInput, "1.0", count=wordCount)    
    while myIndex != "":
        textPane.delete(myIndex,"%s + %sc" % (myIndex,wordCount.get()))
        textPane.insert(myIndex, replaceWord)
        myIndex = textPane.search(userInput, myIndex+ "+ 1c", stopindex=tk.END, count=wordCount)
    return

def upper_selection():
    """
    Takes the selected range from the text pane and converts that text to uppercase in place.
    """
    global textPane
    try:
        start = tk.SEL_FIRST #The first index of the selected range
        end = tk.SEL_LAST #the last index of the highlighted range


        selection = textPane.get(start,end) #store the selected text in a variable
        textPane.insert(start, selection.upper())#insert the uppercase stuff
        textPane.delete(start,end) #delete the selection (the not converted)
    except:
        return

def lower_selection():
    """
    Takes the selected range from the text pane and converts that text to lowercase in place.
    """
    global textPane
    try:
        start = tk.SEL_FIRST #The first index of the selected range
        end = tk.SEL_LAST #the last index of the highlighted range
        selection = textPane.get(start,end)#store the selected text in a variable
        textPane.insert(start, selection.lower())#insert the lowercase stuff
        textPane.delete(start,end)#delete the selection (the not converted)
    except:
        return

def insert_date_time():
    global textPane
    dateTime = dt.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
    textPane.insert(textPane.index(tk.INSERT), dateTime)

def initialize_components():
    """
    All additional GUI elements are currently in this function
    All are configured and added here.
    Justin Cockrell and Brian Kram
    Edits in the menu by deon
    """
    #I put our components into 1 function. We can add the menus here, the scrollbars here.. Seperate if needed
    print("Now adding components \n\n")

    # Menu Bar
    # TODO: figure out how to get rid of menubutton arrows

    """
    Justin's proposed way of handling menus. 
    menuBar = tk.Menu(mainWindow)
    fileMenu = tk.Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="Open")
    fileMenu.add_separator()
    fileMenu.add_command(label="Save")
    menuBar.add_cascade(label="file", menu=fileMenu)
    mainWindow.config(menu=menuBar) This is what makes it a universal menu bar and makes it mac ready 
    """
    global wrap
    global menu_bar
    menu_bar = ttk.Frame(mainWindow)
    menu_bar.pack(side="top")
    # File menu
    file = ttk.Menubutton(menu_bar, text="File")
    file.grid(row=0, column=0)
    file_menu = tk.Menu(file, tearoff=0)
    file_menu.add_command(label="Open...", command=open_file)
    file_menu.add_command(label="New Window...", command=launch)
    file_menu.add_separator()
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As...", command=partial(save_file,True))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=mainWindow.destroy)
    file["menu"] = file_menu # Associate menu with button
    # Edit menu
    edit = ttk.Menubutton(menu_bar, text="Edit")
    edit.grid(row=0, column=1)
    edit_menu = tk.Menu(edit, tearoff=0)
    edit_menu.add_command(label="Find...", command=searchTerm) #TODO: Brianna
    edit_menu.add_command(label="Find and Replace...", command=searchReplace) #TODO: Brianna
    edit_menu.add_separator()
    edit_menu.add_command(label="Uppercase Selection", command=upper_selection) #TODO: Brianna
    edit_menu.add_command(label="Lowercase Selection", command=lower_selection) #TODO: Brianna
    edit_menu.add_separator()
    edit_menu.add_command(label="Sort Lines Alphabetically", command=sortLines) #TODO: Brianna
    edit_menu.add_command(label="Insert Date / Time Here", command=insert_date_time)
    edit["menu"] = edit_menu # Associate menu with button
    # View menu
    view = ttk.Menubutton(menu_bar, text="View")
    view.grid(row=0, column=2)
    view_menu = tk.Menu(view, tearoff=0)
    #view_menu.add_command(label="Toggle Word Wrap", command=toggle_wrap) #TODO: Brianna
    view_menu.add_checkbutton(label="Word Wrap",offvalue=0,onvalue=1,variable=wrap,command=toggle_wrap)
    view_menu.add_command(label="Text Formatting...", command=font_window) # Justin - Done
    view["menu"] = view_menu # Associate menu with button
    # Help menu
    help = ttk.Menubutton(menu_bar, text="Help")
    help.grid(row=0, column=3)
    help_menu = tk.Menu(help, tearoff=0)
    help_menu.add_command(label="Help", command=show_help)
    help_menu.add_command(label="About", command=show_about)
    help["menu"] = help_menu # Associate menu with button


    #define and place scrollbars - Justin Cockrell
    scrollBarx = tk.Scrollbar(mainWindow, orient="horizontal")
    scrollBary = tk.Scrollbar(mainWindow)
    scrollBarx.pack(side="bottom", fill="x")
    scrollBary.pack(side="right", fill="y")

    #define and place the main textbox - Justin Cockrell
    global textPane #textPane is global. This is the reference to it.
    textPane = tk.Text(mainWindow, wrap="none")
    # config Section for the scroll bars. This adds functionality to scroll - Justin Cockrell
    scrollBarx.config(command=textPane.xview)
    scrollBary.config(command=textPane.yview)
    textPane.config(yscrollcommand=scrollBary.set,
                    xscrollcommand=scrollBarx.set)
    textPane.pack(expand=True, fill="both")




def insert_data(data):
    """
    Loads passed data into the text box, replacing whatever is currently in the text box.
    Justin Cockrell
    """
    #This won't change much. This just adds data to the textbox. Open file will change
    textPane.delete("1.0",tk.END)
    textPane.insert("1.0", data)


#FILE IO SECTION
#Expectation: When clicked, open file will open a filedialog and then pass the path of the file to insert_data
def open_file():
    global filePath #Imports the global filepath variable for use locally
    filePath = filedialog.askopenfilename() #opens a dialog to browse for file, assigning it to the file path.
    if filePath == "":
        "You didn't choose a file, try that again!"
        return
    try:
        with open(filePath, "r") as file: #open the file
            data = file.read() #read data into variable
    except FileNotFoundError:
        print("File not found")
    except OSError:
        print("Something is wrong with that file")
    # Modified by Deon
    insert_data(data) #Justin's function to put the data into the text frame

#Expectation: When clicked, save file will open a filedialog and then save the file to whatever is returned from the
#filedialog
def save_file(saveAs = False): #Optional saveAs variable to turn this into a save as function
    global filePath #import global variable
    if filePath == "" or saveAs:
    #If there is no filepath (so like if they just click save but we don't know the file path
    #Or if we just pass in saveAs = True. This way we can force it to ask for a filename.
        filePath = filedialog.asksaveasfilename() #assign a new filepath
    if filePath == "":
        print("You didn't choose a file! Try that again")
        return
    try:
        with open(filePath, "w") as file: #here we are writing. the variable.
            data = file.write(textPane.get("1.0", tk.END))
    except OSError:
        print("Some kind of access error. ")
    #print(textPane.get("1.0", tk.END))

#bryanna: function for sorted lines in a file. 
def sortLines():
    global textPane     #calling the filepath
    with open(filePath, "r") as file:
        for line in sorted(open(filePath)): #sort function
            sortline = print(line, end= "")
        print (sortline)    #debug 
    textPane.insert("0", sortline())    #insert sorted lines back into application
    #still working on having this insert into application ergg

#Drawing a blank here. Surely we will have to add stuff to main later but I think it may get called in other functions
def launch():
    """
    Launches the necessary components.
    """
    #Calls the main window to open the frame and place compontents..
    #THE BUTTONS call other functions.. You will see a note in initialize_components about that
    initialize_application_frame()
    initialize_components()
    mainWindow.mainloop()


def show_about():  # program that opens about txt
    header = ""
    body = ""
    try:
        # opens about text
        path = exec_dir / "about.txt"
        with path.open() as file:
            header = next(file)
            body = "".join(file)
    except FileNotFoundError:
        print("File not found!")
    except OSError:
        print("File corrupted!")


    about_window = tk.Toplevel(master=mainWindow)
    about_window.title("About")
    ttk.Label(master=about_window, text=header).grid(row=0, column=0)
    about_text = tk.Text(master=about_window)
    about_text.insert("1.0", body)
    about_text["state"] = "disabled"
    about_text.grid(row=1, column=0)


def show_help():  # program that opens help txt
    header = ""
    body = ""
    try:
        # opens help text
        path = exec_dir / "help.txt"
        with path.open() as file:
            header = next(file)
            body = "".join(file)
    except FileNotFoundError:
        print("File not found!")
    except OSError:
        print("File corrupted!")

    help_window = tk.Toplevel(master=mainWindow)
    help_window.title("About")
    ttk.Label(master=help_window, text=header).grid(row=0, column=0)
    help_text = tk.Text(master=help_window)
    help_text.insert("1.0", body)
    help_text["state"] = "disabled"
    help_text.grid(row=1, column=0)


launch()
