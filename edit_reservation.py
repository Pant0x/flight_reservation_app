import tkinter as tk
from tkinter import ttk, messagebox
from database import get_reservations, update_reservation

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Edit Reservation", font=("Arial", 24))
        label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "From", "To", "Date", "Flight Number", "Seat Number"), show="headings")  # Added columns
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(pady=10, fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Label(form_frame, text="From:").grid(row=1, column=0, sticky="e")
        tk.Label(form_frame, text="To:").grid(row=2, column=0, sticky="e")
        tk.Label(form_frame, text="Date:").grid(row=3, column=0, sticky="e")
        tk.Label(form_frame, text="Flight Number:").grid(row=4, column=0, sticky="e")  # Added
        tk.Label(form_frame, text="Seat Number:").grid(row=5, column=0, sticky="e")  # Added

        self.name_entry = tk.Entry(form_frame)
        self.from_entry = tk.Entry(form_frame)
        self.to_entry = tk.Entry(form_frame)
        self.date_entry = tk.Entry(form_frame)
        self.flight_number_entry = tk.Entry(form_frame)  # Added
        self.seat_number_entry = tk.Entry(form_frame)  # Added

        self.name_entry.grid(row=0, column=1, padx=5, pady=2)
        self.from_entry.grid(row=1, column=1, padx=5, pady=2)
        self.to_entry.grid(row=2, column=1, padx=5, pady=2)
        self.date_entry.grid(row=3, column=1, padx=5, pady=2)
        self.flight_number_entry.grid(row=4, column=1, padx=5, pady=2)  # Added
        self.seat_number_entry.grid(row=5, column=1, padx=5, pady=2)  # Added

        self.update_button = tk.Button(self, text="Update Reservation", command=self.update_reservation)
        self.update_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        self.back_button.pack(pady=5)

        self.selected_id = None
        self.load_reservations()

    def load_reservations(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        reservations = get_reservations()
        for res in reservations:
            self.tree.insert("", "end", values=res)

    def on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        values = self.tree.item(selected[0])["values"]
        self.selected_id = values[0]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, values[1])
        self.from_entry.delete(0, tk.END)
        self.from_entry.insert(0, values[2])
        self.to_entry.delete(0, tk.END)
        self.to_entry.insert(0, values[3])
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, values[4])
        self.flight_number_entry.delete(0, tk.END)  # Added
        self.flight_number_entry.insert(0, values[5])  # Added
        self.seat_number_entry.delete(0, tk.END)  # Added
        self.seat_number_entry.insert(0, values[6])  # Added

    def update_reservation(self):
        if not self.selected_id:
            messagebox.showwarning("No Selection", "Please select a reservation to update.")
            return

        name = self.name_entry.get().strip()
        from_city = self.from_entry.get().strip()
        to_city = self.to_entry.get().strip()
        date = self.date_entry.get().strip()
        flight_number = self.flight_number_entry.get().strip()
        seat_number = self.seat_number_entry.get().strip()

        if not (name and from_city and to_city and date and flight_number and seat_number):
            messagebox.showerror("Input Error", "All fields must be filled.")
            return

        update_reservation(self.selected_id, name, flight_number, from_city, to_city, date, seat_number)
        messagebox.showinfo("Success", "Reservation updated successfully.")
        self.load_reservations()
        self.selected_id = None
        self.name_entry.delete(0, tk.END)
        self.from_entry.delete(0, tk.END)
        self.to_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.flight_number_entry.delete(0, tk.END)
        self.seat_number_entry.delete(0, tk.END)
