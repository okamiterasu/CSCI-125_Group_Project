from pathlib import Path
import tkinter as tk
from tkinter import ttk, font, filedialog
from functools import partial


mainWindow = ""
textPane = ""
menu_bar = None
filePath = ""
exec_dir = Path(__file__).parent

# TODO: Look over this document for TODO tags. Make sure you have contributed your part on time
# TODO: Brianna and Deon, please claim some of the unclaimed work that needs to be done. Listed below
# Justin Cockrell and Brian Kram are the only contributers to this revision so far. In addition to the tasks you have



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

def upper_selection():

    global textPane
    start = tk.SEL_FIRST
    end = tk.SEL_LAST
    selection = textPane.get(start,end)
    textPane.insert(start, selection.upper())
    textPane.delete(start,end)

    textPane.tag_add('found', "1.0", tk.END)
    textPane.tag_config("found", bg="red")


def lower_selection():
    global textPane
    print("Lower")

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

def initialize_components():
    """
    All additional GUI elements are currently in this function
    Justin Cockrell and Brian Kram
    """
    #I put our components into 1 function. We can add the menus here, the scrollbars here.. Seperate if needed
    print("Now adding components \n\n")

    # Menu Bar
    # TODO: figure out how to get rid of menubutton arrows

    """
    menuBar = tk.Menu(mainWindow)
    fileMenu = tk.Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="Open")
    fileMenu.add_separator()
    fileMenu.add_command(label="Save")
    menuBar.add_cascade(label="file", menu=fileMenu)
    mainWindow.config(menu=menuBar)
    """

    global menu_bar
    menu_bar = ttk.Frame(mainWindow)
    menu_bar.pack(side="top")
    # File menu
    file = ttk.Menubutton(menu_bar, text="File")
    file.grid(row=0, column=0)
    file_menu = tk.Menu(file, tearoff=0)
    file_menu.add_command(label="Open...", command=open_file)#TODO: Deon
    file_menu.add_command(label="New Window...", command=launch)
    file_menu.add_separator()
    file_menu.add_command(label="Save", command=save_file) #TODO: Deon
    file_menu.add_command(label="Save As...", command=partial(save_file,True)) #TODO: Deon
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=mainWindow.destroy)
    file["menu"] = file_menu # Associate menu with button
    # Edit menu
    edit = ttk.Menubutton(menu_bar, text="Edit")
    edit.grid(row=0, column=1)
    edit_menu = tk.Menu(edit, tearoff=0)
    edit_menu.add_command(label="Cut", command=stub) #TODO: Justin
    edit_menu.add_command(label="Copy", command=stub) #TODO: Justin
    edit_menu.add_separator()
    edit_menu.add_command(label="Find...", command=stub) #TODO: Brianna
    edit_menu.add_command(label="Find and Replace...", command=stub) #TODO: Brianna
    edit_menu.add_separator()
    edit_menu.add_command(label="Uppercase Selection", command=upper_selection) #TODO: Brianna
    edit_menu.add_command(label="Lowercase Selection", command=lower_selection) #TODO: Brianna
    edit_menu.add_separator()
    edit_menu.add_command(label="Sort Lines Alphabetically", command=stub) #TODO: Brianna
    edit["menu"] = edit_menu # Associate menu with button
    # View menu
    view = ttk.Menubutton(menu_bar, text="View")
    view.grid(row=0, column=2)
    view_menu = tk.Menu(view, tearoff=0)
    view_menu.add_command(label="Toggle Word Wrap", command=stub) #TODO: Brianna
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
    textPane.pack(expand=True, fill="both")

    #config Section for the scroll bars. This adds functionality to scroll - Justin Cockrell
    scrollBarx.config(command=textPane.yview)
    scrollBary.config(command=textPane.xview)
    textPane.config(yscrollcommand=scrollBary.set,
                    xscrollcommand=scrollBarx.set)
    #TODO:
    # We need the menu made. Collaborate with team to decide what all menu items
    # We need Scrollbar X / Y and mapping DONE!! - Jcockrell
    # We need the wrap option to be a variable item some how so we can make a menu option toggle that.
    # We need a menu item for each of the discussed string manipulation. Set them up with placeholder function calls.
    # I will replace them with the correct function calls.

def insert_data(data):
    """
    Loads passed data into the text box, replacing whatever is currently in the text box.
    Justin Cockrell
    """
    print("Open_file called me.. Now we're here.")
    #This won't change much. This just adds data to the textbox. Open file will change
    textPane.delete("1.0",tk.END)
    textPane.insert("1.0", data)


#FILE IO SECTION
#Expectation: When clicked, open file will open a filedialog and then pass the path of the file to insert_data
def open_file():
    global filePath
    # TODO: Deon, error handling
    filePath = filedialog.askopenfilename()
    with open(filePath, "r") as file:
        data = file.read()
    # Modified by Deon
    insert_data(data)



#Expectation: When clicked, save file will open a filedialog and then save the file to whatever is returned from the
#filedialog
def save_file(saveAs = False):
    # TODO: Deon
    # Current version built by Justin Cockrell
    global filePath
    if filePath == "" or saveAs:
        filePath = filedialog.asksaveasfilename()
    with open(filePath, "w") as file:
        data = file.write(textPane.get("1.0", tk.END))
    print(textPane.get("1.0", tk.END))


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

def show_about():
    path = exec_dir / "about.txt"
    with path.open() as file:
        header = next(file)
        body = "".join(file)
    
    about_window = tk.Toplevel(master=mainWindow)
    about_window.title("About")
    ttk.Label(master=about_window, text=header).grid(row=0, column=0)
    about_text = tk.Text(master=about_window)
    about_text.insert("1.0", body)
    about_text["state"] = "disabled"
    about_text.grid(row=1, column=0)


def show_help():
    path = exec_dir / "help.txt"
    with path.open() as file:
        header = next(file)
        body = "".join(file)
    
    help_window = tk.Toplevel(master=mainWindow)
    help_window.title("About")
    ttk.Label(master=help_window, text=header).grid(row=0, column=0)
    help_text = tk.Text(master=help_window)
    help_text.insert("1.0", body)
    help_text["state"] = "disabled"
    help_text.grid(row=1, column=0)



launch()
