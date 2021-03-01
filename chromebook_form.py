import tkinter as tk

root = tk.Tk()
root.title('Chromebooks')
root.configure(background='#b8b6b6')


def on_submit():

    service_tag = service_tag_entry.get()
    location = location_entry.get()
    date_acquired = date_entry.get()
    issue = issue_entry.get()
    warranty_expiration = warranty_date_entry.get()

    # change path as necessary
    with open('C:/Users/wav11/PycharmProjects/pythonProject/chromebooks.txt', 'a') as file_object:
        file_object.write(f'service_tag = {service_tag}\n')
        file_object.write(f'location = {location}\n')
        file_object.write(f'date_acquired = {date_acquired}\n')
        file_object.write(f'issue = {issue}\n')
        file_object.write(f'warranty_expiration = {warranty_expiration}\n')
        file_object.write('\n')

    print('submitted!')

    submitted_window()


def submitted_window():

    root2 = tk.Tk()
    root2.title('Submitted!')

    submitted_label = tk.Label(root2, text='Submitted!', width=25)
    submitted_label.grid(row=0, column=0)

    ok_button = tk.Button(root2, text='Ok', command=root2.destroy)
    ok_button.grid(row=1, column=0)

    root2.mainloop()


def clear_entries():

    service_tag_entry.delete(0, 'end')
    date_entry.delete(0, 'end')
    location_entry.delete(0, 'end')
    issue_entry.delete(0, 'end')
    warranty_date_entry.delete(0, 'end')


service_tag_label = tk.Label(root, text='Service Tag#', bg='#b8b6b6')
service_tag_label.grid(row=0, column=0)

service_tag_entry = tk.Entry(root, justify='center')
service_tag_entry.grid(row=0, column=1)

date_label = tk.Label(root, text='Date Acquired', bg='#b8b6b6')
date_label.grid(row=1, column=0)

date_entry = tk.Entry(root, justify='center')
date_entry.grid(row=1, column=1)

location_label = tk.Label(root, text='Location', bg='#b8b6b6')
location_label.grid(row=2, column=0)

location_entry = tk.Entry(root, justify='center')
location_entry.grid(row=2, column=1)

issue_label = tk.Label(root, text='Issue', bg='#b8b6b6')
issue_label.grid(row=3, column=0)

issue_entry = tk.Entry(root, justify='center')
issue_entry.grid(row=3, column=1)

warranty_date_label = tk.Label(root, text='Warranty Expiration Date', bg='#b8b6b6')
warranty_date_label.grid(row=4, column=0)

warranty_date_entry = tk.Entry(root, justify='center')
warranty_date_entry.grid(row=4, column=1)

clear_button = tk.Button(root, text='Clear', pady=5, command=clear_entries)
clear_button.grid(row=5, column=0)

submit_button = tk.Button(root, text='Submit', pady=5, command=on_submit)
submit_button.grid(row=5, column=1)


root.mainloop()
