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

    # function to take user back home
def write(master,name,oc,pin):
    if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0) or name==""):
        messagebox.showinfo("Error", "Invalid Credentials \nPlease try Again.")
        master.destroy()
        return
    
    #logic to create an account
    f1=open("Accnt_Record.txt", 'r')
    accnt_no = int(f1.readline())
    accnt_no+=1
    f1.close()

    f1=open("Accnt_Record.txt", 'w')
    f1.write(str(accnt_no))
    f1.close()

    fdet=open(str(accnt_no)+".txt","w")
    fdet.write(name+"\n"+oc+"\n"+pin)
    





    
