import tkinter as tk

root = tk.Tk()
root.title('Chromebook forms')

# root = tk.Frame(root)
# root.place(relwidth=.8)



location_label = tk.Label(root, text='Location ')
location_label.grid(row=0, column=0)

location_entry = tk.Entry(root)
location_entry.grid(row=0, column=1)

service_tag_label = tk.Label(root, text='Service Tag# ')
service_tag_label.grid(row=1, column=0)

service_tag_entry = tk.Entry(root)
service_tag_entry.grid(row=1, column=1)

issue_label = tk.Label(root, text='Issue ')
issue_label.grid(row=2, column=0)

issue_entry = tk.Entry(root)
issue_entry.grid(row=2, column=1)

# submit_button = tk.Button(root, text='Submit', pady=5)
# submit_button.grid(row=3, column=1)

warranty_label = tk.Label(root, text='Under Warranty?')
warranty_label.grid(row=0, column=2)

warranty_yes_label = tk.Label(root, text='Yes')
warranty_yes_label.grid(row=1, column=2)

warranty_no_label = tk.Label(root, text='No')
warranty_no_label.grid(row=1, column=4)

warranty_yes_check = tk.Checkbutton(root)
warranty_yes_check.grid(row=1, column=3)

warranty_no_check = tk.Checkbutton(root)
warranty_no_check.grid(row=1, column=5)

warranty_date_label = tk.Label(root, text='Warranty Expiration Date')
warranty_date_label.grid(row=2, column=2)

warranty_date_entry = tk.Entry(root)
warranty_date_entry.grid(row=2, column=3)

root.mainloop()
