import tkinter as tk

def book_flight():
    name = entry_name.get()
    source = entry_source.get()
    destination = entry_destination.get()
    date = entry_date.get()
    # You can add further processing or save the booking information to a database.

    # Display a confirmation message
    confirmation_message = f"Flight booked for {name} from {source} to {destination} on {date}."
    confirmation_label.config(text=confirmation_message)

# Create the main window
root = tk.Tk()
root.title("Flight Booking Form")

# Labels
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)

label_source = tk.Label(root, text="Source:")
label_source.grid(row=1, column=0, padx=10, pady=5)

label_destination = tk.Label(root, text="Destination:")
label_destination.grid(row=2, column=0, padx=10, pady=5)

label_date = tk.Label(root, text="Date:")
label_date.grid(row=3, column=0, padx=10, pady=5)

# Entry fields
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

entry_source = tk.Entry(root)
entry_source.grid(row=1, column=1, padx=10, pady=5)

entry_destination = tk.Entry(root)
entry_destination.grid(row=2, column=1, padx=10, pady=5)

entry_date = tk.Entry(root)
entry_date.grid(row=3, column=1, padx=10, pady=5)

# Booking button
book_button = tk.Button(root, text="Book Flight", command=book_flight)
book_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Confirmation message label
confirmation_label = tk.Label(root, text="")
confirmation_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
