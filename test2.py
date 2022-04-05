import tkinter as tk

root = tk.Tk()
root.title('Inventory')
root.configure(background='#b8b6b6')

def submitted_window():

    root2 = tk.Tk()
    root2.title('Submitted!')

    submitted_label = tk.Label(root2, text='Submitted!', width=25)
    submitted_label.grid(row=0, column=0)

    ok_button = tk.Button(root2, text='Ok', command=root2.destroy)
    ok_button.grid(row=1, column=0)

    root2.mainloop()


def clear_entries():

    drive_manufacturer_entry.delete(0, 'end')
    drive_size_entry.delete(0, 'end')
    drive_form_factor_entry.delete(0, 'end')
    drive_speed_entry.delete(0, 'end')
    drive_price_entry.delete(0, 'end')


drive_manufacturer_label = tk.Label(root, text='Manufacturer', bg='#b8b6b6')
drive_manufacturer_label.grid(row=0, column=0)

drive_manufacturer_entry = tk.Entry(root, justify='center')
drive_manufacturer_entry.grid(row=0, column=1)

drive_size_label = tk.Label(root, text='Size', bg='#b8b6b6')
drive_size_label.grid(row=1, column=0)

drive_size_entry = tk.Entry(root, justify='center')
drive_size_entry.grid(row=1, column=1)

drive_form_factor_label = tk.Label(root, text='Form Factor', bg='#b8b6b6')
drive_form_factor_label.grid(row=2, column=0)

drive_form_factor_entry = tk.Entry(root, justify='center')
drive_form_factor_entry.grid(row=2, column=1)

drive_speed_label = tk.Label(root, text='Speed', bg='#b8b6b6')
drive_speed_label.grid(row=3, column=0)

drive_speed_entry = tk.Entry(root, justify='center')
drive_speed_entry.grid(row=3, column=1)

drive_price_label = tk.Label(root, text='Price', bg='#b8b6b6')
drive_price_label.grid(row=4, column=0)

drive_price_entry = tk.Entry(root, justify='center')
drive_price_entry.grid(row=4, column=1)

clear_button = tk.Button(root, text='Clear', pady=5, command=clear_entries)
clear_button.grid(row=5, column=0)

submit_button = tk.Button(root, text='Submit', pady=5, command=submitted_window)
submit_button.grid(row=5, column=1)



root.mainloop()