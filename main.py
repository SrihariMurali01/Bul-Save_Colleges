import os
import pandas as pd
from tkinter import *
from tkinter import messagebox

FONT = ("Times New Roman", 16, "bold")


def bulk_save():
    file_path = filepath.get()
    file_path = file_path.replace(os.sep, '/')
    file_path = file_path.replace("\"", "")
    suffix_entry = suffix.get().upper()
    try:
        with open(file_path) as data:
            df = pd.read_csv(data)
            num_dict = df.to_dict(orient='records')
    except FileNotFoundError:
        messagebox.showinfo(title="BULK SAVE", message="Welcome to Bulk Save! Looks like you have not entered the file path correctly. Please enter the FULL PATH of the file along with the file name and extension. Happy Saving!")
    else:
        try:
            with open("D:/numbers.vcf", mode='a') as output_file:
                output_file.truncate(0)
                for item in num_dict:
                    template = str("BEGIN:VCARD\n"
                                   "VERSION:2.1\n"
                                   f"N:{suffix_entry};{item['Name']};\n"
                                   f"FN:{item['Name']} {suffix_entry}\n"
                                   f"TEL;CELL:{item['Numbers']}\n"
                                   "END:VCARD\n\n")
                    output_file.write(template)
                messagebox.showinfo(title="Save Complete",
                                    message="The file is saved in D drive as 'numbers.vcf'. Please collect your output from there and send it to your phone/tablet.\nThank you for using Bulk Save!\n\n *A small word of caution. In order to achieve maximum efficiency of results, please ensure that the CSV file is accurate")
        except FileNotFoundError:
            messagebox.showinfo(title="Bulk Saver",
                                message="Welcome to Bulk Save!This application helps you save a lot of time saving a lot of contacts at the same time. Please make sure the csv file entered is accurate in order to achieve efficient results! Happy saving!")
            with open("D:/numbers.vcf", mode="w"):
                bulk_save()
        finally:
            filepath.delete(0, END)
            suffix.delete(0, END)
            filepath.insert(0, "Please enter the FULL PATH of the file(including filename and extension)")
            suffix.insert(0, "Please enter your college name(Abbreviation)")


# ------------------------------- UI ----------------------------

window = Tk()
window.title("BULK SAVE")
window.config(padx=50, pady=50)

logo = PhotoImage(file="images/logo.png")
img_canvas = Canvas(width=200, height=200)
img_canvas.create_image(100, 100, image=logo)
img_canvas.grid(column=1, row=0)

filepath = Entry()
filepath.insert(0, "Please enter the FULL PATH of the .csv file(including filename and extension)")
filepath.config(width=70)
filepath.grid(column=1, row=1, columnspan=2)
file_label = Label(text="File Path:", font=FONT)
file_label.grid(column=0, row=1)

suffix = Entry()
suffix.insert(0, "Please enter your college name(Abbreviation)")
suffix.config(width=70)
suffix.grid(column=1, row=2, columnspan=2)
suffix_label = Label(text="      Suffix:", font=FONT)
suffix_label.grid(column=0, row=2)

submit_button = Button(borderwidth=3, command=bulk_save)
submit_button.config(text="Submit", width=50)
submit_button.grid(column=1, row=3, columnspan=2)

window.mainloop()
