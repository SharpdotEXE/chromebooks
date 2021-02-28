import tkinter as tk

root = tk.Tk()
root.title('Chromebook forms')
root.configure(background='#b8b6b6')


def warranty_yes_check_state():

    warranty_no_check.deselect()


def warranty_no_check_state():

    warranty_yes_check.deselect()


location_label = tk.Label(root, text='Location', bg='#b8b6b6')
location_label.grid(row=0, column=0)

location_entry = tk.Entry(root, justify='center')
location_entry.grid(row=0, column=1)

date_label = tk.Label(root, text='Date Acquired', bg='#b8b6b6')
date_label.grid(row=1, column=0)

date_entry = tk.Entry(root, justify='center')
date_entry.grid(row=1, column=1)

service_tag_label = tk.Label(root, text='Service Tag#', bg='#b8b6b6')
service_tag_label.grid(row=2, column=0)

service_tag_entry = tk.Entry(root, justify='center')
service_tag_entry.grid(row=2, column=1)

issue_label = tk.Label(root, text='Issue', bg='#b8b6b6')
issue_label.grid(row=3, column=0)

issue_entry = tk.Entry(root, justify='center')
issue_entry.grid(row=3, column=1)

warranty_label = tk.Label(root, text='Under Warranty?', bg='#b8b6b6')
warranty_label.grid(row=0, column=2)


warranty_yes_check = tk.Checkbutton(root, text='Yes', bg='#b8b6b6', command=warranty_yes_check_state)
warranty_yes_check.grid(row=1, column=2)

warranty_no_check = tk.Checkbutton(root, text='No', bg='#b8b6b6', command=warranty_no_check_state)
warranty_no_check.grid(row=1, column=3)

warranty_date_label = tk.Label(root, text='Warranty Expiration Date', bg='#b8b6b6')
warranty_date_label.grid(row=2, column=2)

warranty_date_entry = tk.Entry(root, justify='center')
warranty_date_entry.grid(row=2, column=3)

submit_button = tk.Button(root, text='Submit', pady=5)
submit_button.grid(row=4, column=2)


root.mainloop()
