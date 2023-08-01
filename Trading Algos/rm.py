import tkinter as tk
import datetime
import time

def set_alarm():
    alarm_time_str = entry_time.get()
    try:
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time_str:
                label_status.config(text="Alarm triggered!")
                break
            label_status.config(text=f"Current Time: {current_time}")
            root.update()
            time.sleep(1)
    except ValueError:
        label_status.config(text="Invalid time format!")

# Create the main application window
root = tk.Tk()
root.title("GUI Alarm Clock")

# Time Entry
entry_time = tk.Entry(root, width=10)
entry_time.pack()

# Set Alarm Button
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack()

# Status Label
label_status = tk.Label(root, text="")
label_status.pack()

# Start the application
root.mainloop()
