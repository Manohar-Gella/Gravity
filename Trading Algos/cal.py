import tkinter as tk

def calculate():
    principal = float(entry_principal.get())
    rate = float(entry_rate.get()) / 100
    time = float(entry_time.get())

    compound_interest = principal * (1 + rate) ** time

    result_label.config(text=f"Compound Interest: {compound_interest:.2f}")

# Create the main window
root = tk.Tk()
root.title("Finance Calculator")

# Labels
label_principal = tk.Label(root, text="Principal:")
label_principal.grid(row=0, column=0, padx=10, pady=5)

label_rate = tk.Label(root, text="Rate (%):")
label_rate.grid(row=1, column=0, padx=10, pady=5)

label_time = tk.Label(root, text="Time (years):")
label_time.grid(row=2, column=0, padx=10, pady=5)

# Entry fields
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=5)

entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1, padx=10, pady=5)

entry_time = tk.Entry(root)
entry_time.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Compound Interest", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
