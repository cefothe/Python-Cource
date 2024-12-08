import tkinter as tk
import random
import threading

def create_popup():
    # Create the main window for pop-up
    popup = tk.Toplevel()
    popup.title("Virus Alert")
    
    # Set larger window size (e.g., 500x200)
    popup.geometry("500x200")
    
    # Generate a random position for the window
    x = random.randint(0, popup.winfo_screenwidth() - 500)
    y = random.randint(0, popup.winfo_screenheight() - 200)
    popup.geometry(f"+{x}+{y}")
    
    # Display the "hacked" message
    label = tk.Label(popup, text="You have been hacked!", font=("Arial", 18), fg="red")
    label.pack(expand=True)
    
    # Ensure the window stays on top
    popup.attributes("-topmost", True)
    
    # Make the window appear without the minimize/maximize/close buttons
    popup.overrideredirect(True)

# Create the main Tk instance (hidden)
root = tk.Tk()
root.withdraw()

# Create 30 popup windows in separate threads
for _ in range(30):
    threading.Thread(target=create_popup).start()

# Run the main event loop
root.mainloop()
