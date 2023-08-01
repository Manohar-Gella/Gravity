import tkinter as tk

def submit_form():
    # Retrieve form data
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    # Do something with the data (e.g., store it in a database, print it)
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

    # Clear form fields
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Puyon GUI School Form")

# Form Labels
label_name = tk.Label(root, text="Name:")
label_name.pack()

label_age = tk.Label(root, text="Age:")
label_age.pack()

label_grade = tk.Label(root, text="Grade:")
label_grade.pack()

# Form Entry Fields
entry_name = tk.Entry(root)
entry_name.pack()

entry_age = tk.Entry(root)
entry_age.pack()

entry_grade = tk.Entry(root)
entry_grade.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Start the application
root.mainloop()
