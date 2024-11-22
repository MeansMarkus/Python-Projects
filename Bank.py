import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime

#Handling of invalid credentials

#function that us a combo try and catch to handle ValueError
def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0
    #function to check whether acc number is valid or not
def check_acc_nmb(num):
    try: 
        fpin=open(num + ".txt","r")
    except FileNotFoundError:
        messagebox.showinfo("Invalid Account Number", "Try Again")
        return 0
    fpin.close()
    return

    
