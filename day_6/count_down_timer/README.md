
## 1. **Basic Countdown Timer (Seconds Only)**
This timer counts down from a fixed number of seconds and prints each second.
```python
import time

t = 10  # Countdown from 10 seconds
while t > 0:
    print(t)
    time.sleep(1)
    t -= 1
print("Time's up!")
```
- **Loop:** `while t > 0` keeps counting down.
- **Pause:** `time.sleep(1)` waits one second each loop.

***

## 2. **User Input & Minute:Second Formatting**
Let the user set the timer, and display time as `mm:ss`.
```python
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Overwrites the line each second
        time.sleep(1)
        t -= 1
    print("Fire in the hole!!")

# Get user input
user_time = int(input("Enter the time in seconds: "))
countdown(user_time)
```
- **`divmod(t, 60)`:** Splits seconds into minutes and seconds.
- **`end='\r'`:** Keeps the countdown on one line.

***

## 3. **Advanced: GUI & Desktop Notification**
For a graphical timer, use `tkinter` and optionally `plyer` for desktop notifications. (Requires installing extra modules.)
```python
import time
from tkinter import *
from tkinter import messagebox
from plyer import notification

root = Tk()
root.geometry("300x150")
root.title("Countdown Timer")

# Entry for seconds
entry = Entry(root, font=("Arial", 24))
entry.pack(pady=20)

# Countdown function
def start_timer():
    t = int(entry.get())
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        entry.delete(0, END)
        entry.insert(0, timer)
        root.update()
        time.sleep(1)
        t -= 1
    entry.delete(0, END)
    entry.insert(0, "Time's up!")
    messagebox.showinfo("Timer", "Time's up!")
    notification.notify(title="Timer", message="Time's up!")

Button(root, text="Start", command=start_timer).pack()
root.mainloop()
```
- **GUI:** Uses `tkinter` for a window and input box.
- **Notification:** Uses `plyer` for desktop alerts.

***

## 4. **Extra: Playing a Sound (Windows Only)**
After the timer ends, play a sound file (like `alarm.wav`).
```python
import subprocess
subprocess.Popen(['start', 'alarm.wav'], shell=True)
```
- On macOS, use `['open', 'alarm.wav']`.
- On Linux, use `['xdg-open', 'alarm.wav']`.

***
