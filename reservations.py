import tkinter as tk
from database import get_reservations

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f8f9fa")

        tk.Label(self, text="Your Reservations", font=("Helvetica", 18, "bold"), bg="#f8f9fa", fg="#004c77").pack(pady=(20, 10))

        control_frame = tk.Frame(self, bg="#f8f9fa")
        control_frame.pack(pady=(0, 10))

        self.search_entry = tk.Entry(control_frame, width=30)
        self.search_entry.pack(side="left", padx=(0, 10))

        tk.Button(control_frame, text="Search", command=self.update_reservations).pack(side="left", padx=(0, 10))

        tk.Button(control_frame, text="Book New Flight", bg="#007bff", fg="white", relief="flat",
                  command=lambda: controller.show_frame("BookingPage")).pack(side="left", padx=10)

        tk.Button(control_frame, text="Back to Home", bg="#555", fg="white", relief="flat",
                  command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=10)

        self.reservations_frame = tk.Frame(self, bg="#f8f9fa")
        self.reservations_frame.pack(pady=10, fill="both", expand=True)

        self.update_reservations()

    def update_reservations(self):
        for widget in self.reservations_frame.winfo_children():
            widget.destroy()

        reservations = get_reservations()
        search_query = self.search_entry.get().lower()

        filtered = [r for r in reservations if search_query in r["name"].lower()]

        if not filtered:
            tk.Label(self.reservations_frame, text="No Reservations Found", font=("Helvetica", 12, "bold"), bg="#f8f9fa", fg="#555").pack()
            tk.Label(self.reservations_frame, text="You haven’t booked any flights yet.", bg="#f8f9fa", fg="#777").pack()
            return

        for res in filtered:
            text = f"{res['date']} - {res['name']} - Flight {res['flight_number']} from {res['departure']} to {res['destination']} | Seat {res['seat_number']}"
            tk.Label(self.reservations_frame, text=text, bg="#f8f9fa", anchor="w", padx=10).pack(fill="x", pady=2)
