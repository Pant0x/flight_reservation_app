import tkinter as tk
from tkinter import messagebox
from database import add_reservation

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f8f9fa")

        tk.Label(self, text="Book a Flight", font=("Helvetica", 18, "bold"), bg="#f8f9fa", fg="#004c77").pack(pady=30)

        form_frame = tk.Frame(self, bg="white", bd=1, relief="solid", padx=20, pady=20)
        form_frame.pack()

        self.fields = {}

        self.add_field(form_frame, "Full Name", 0)
        self.add_field(form_frame, "Flight Number", 1)
        self.add_field(form_frame, "Departure", 2)
        self.add_field(form_frame, "Destination", 3)
        self.add_field(form_frame, "Date (YYYY-MM-DD)", 4)
        self.add_field(form_frame, "Seat Number", 5)

        # Buttons
        button_frame = tk.Frame(form_frame, bg="white")
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Cancel", command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=10)
        tk.Button(button_frame, text="Book Flight", bg="#007bff", fg="white", relief="flat", command=self.book_flight).pack(side="left")

    def add_field(self, parent, label, row):
        tk.Label(parent, text=label, bg="white", anchor="w").grid(row=row, column=0, sticky="w", pady=5)
        entry = tk.Entry(parent, width=30)
        entry.grid(row=row, column=1, pady=5)
        self.fields[label] = entry

    def book_flight(self):
        data = {k: v.get() for k, v in self.fields.items()}
        if any(val == "" for val in data.values()):
            messagebox.showwarning("Missing Info", "Please fill all fields.")
            return

        add_reservation(
            data["Full Name"],
            data["Flight Number"],
            data["Departure"],
            data["Destination"],
            data["Date (YYYY-MM-DD)"],
            data["Seat Number"]
        )
        messagebox.showinfo("Success", "Flight booked successfully!")
        self.controller.show_frame("HomePage")
