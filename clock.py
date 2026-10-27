"""A simple digital clock built with Python's standard-library Tkinter GUI."""

import tkinter as tk
from datetime import datetime


def main() -> None:
    root = tk.Tk()
    root.title("Digital Clock")
    root.resizable(False, False)
    root.configure(bg="#101820")

    time_label = tk.Label(
        root,
        font=("Segoe UI", 48, "bold"),
        fg="#FEE715",
        bg="#101820",
        padx=24,
        pady=20,
    )
    time_label.pack()

    date_label = tk.Label(
        root,
        font=("Segoe UI", 14),
        fg="#FFFFFF",
        bg="#101820",
        padx=24,
        pady=4,
    )
    date_label.pack()

    def update_clock() -> None:
        now = datetime.now()
        time_label.config(text=now.strftime("%I:%M:%S %p"))
        date_label.config(text=now.strftime("%A, %B %d, %Y"))
        root.after(1000, update_clock)

    update_clock()
    root.mainloop()


if __name__ == "__main__":
    main()