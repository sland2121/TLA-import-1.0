"""
author: Sayeri Lala
7-9-2014
Synnex Co., Hyve Solutions, Fremont

TLAdb_import_tool.py sets up the gui tool for user to import TLAs.
"""

import config
import MySQLdb
import importdb
import Tkinter as tk
import tkFileDialog as tkfd
import tkMessageBox as tkmb
import xlrd
config.warnings.filterwarnings('ignore', category = MySQLdb.Warning)
global root
global temp_frame

"""
openFile:
Launches file dialog for user to browse and upload a .xls file.
If file successfully retrieved, import TLA options become available.
"""
def openFile():
    #returns an opened file
    fname = tkfd.Open(filetypes = [("xls files","*.xls")])
    fpath = fname.show()
    if fname:
        try:
            TLA_workbook = xlrd.open_workbook(fpath, formatting_info = True)
            
            #option 1: import all TLAs
            tk.Button(root, text = "Import ALL TLAs", command = \
                      lambda: importdb.importAllTLAtoDB(TLA_workbook)).pack()

            #option 2: import inputted TLAs
            tk.Button(root, text = "Input TLAs to import",
                      command = lambda: inputTLAs(TLA_workbook)).pack()
            tkmb.showinfo("Success!", "Spreadsheet successfully loaded.")
        except:
            tkmb.showerror("Error", "Failed to read file\n '%s'\n\
Make sure file is a type .xls" % fpath)

"""
import_input_TLAs:
import TLAs in input (TLA_entries_str) into RCKHYVEDB.
"""
def import_input_TLAs(TLA_entries_str, TLA_workbook):
    #format input into list type
    TLA_entries_list = TLA_entries_str.replace(" ", "").split(",")
    
    importdb.importTLAtoDB(TLA_workbook, \
                  TLA_entries_list)
"""
inputTLAs:
opens Entry window for user to input TLAs and import TLAs
into RCKHYVEDB.
"""
def inputTLAs(TLA_workbook):
    inputTLA_window = tk.Tk()
    inputTLA_window.iconbitmap("synnex.ico")
    inputTLA_window.title("Input TLAs")

    TLA_entry = tk.Entry(inputTLA_window)
    TLA_entry.pack()

    #tk.Button(inputTLA_window, text = "Import inputted TLAs", command = lambda: test(TLA_entry)).pack()
    tk.Button(inputTLA_window, text = "Import TLAs e.g., 15-000308, 15-000309,...",
              command = lambda: import_input_TLAs(TLA_entry.get(), TLA_workbook)).pack()

"""
logintoDB:
login tool for 192.168.68.60. Upon successful login, user can upload
spreadsheet file.
"""
def logintoDB(user, pw):
    #request login for database access
    try:
        db = MySQLdb.connect(config.server_link, user, pw, config.database)
        config.user = user
        config.pw = pw
        tkmb.showinfo("Success!","Database login successful.\n\
Click Browse to load TLA spreadsheet.")
        browse_button = tk.Button(temp_frame, text = "Browse", command =
                                  openFile, width = 10).pack() 
    except:
        tkmb.showerror("Error", "Login failed. Try again.")

"""
startwindow:
GUI setup. Opens window for user to input username/password for
database login.
"""
def startwindow():
    root.title("TLA Database Tool")
    root.iconbitmap("synnex.ico")
    tk.Label(temp_frame, text = "Database login").pack()
    user_label = tk.Label(temp_frame, text = "username").pack()
    user = tk.Entry(temp_frame, textvariable = tk.StringVar())
    user.pack()
    pw_label = tk.Label(temp_frame, text = "password").pack()
    pw = tk.Entry(temp_frame, show = "*", textvariable = tk.StringVar())
    pw.pack()
    
    login_button = tk.Button(temp_frame, text = "Login", command = \
                             lambda: logintoDB(user.get(), pw.get()))
    #login_button.bind("<Enter>",(lambda event: logintoDB(user.get(),pw.get())))
    login_button.pack()
    
#main    
root = tk.Tk()
temp_frame = tk.Frame(root)
temp_frame.pack()
startwindow()
root.mainloop()


