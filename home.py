import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f8f9fa")

        header = tk.Label(self, text="Welcome to FlySky Reservations", font=("Helvetica", 20, "bold"), bg="#f8f9fa", fg="#004c77")
        header.pack(pady=(40, 10))

        desc = tk.Label(self, text="Book your flights and manage your reservations with our simple and intuitive system.", font=("Helvetica", 11), bg="#f8f9fa", fg="#444")
        desc.pack(pady=(0, 30))

        card_frame = tk.Frame(self, bg="#f8f9fa")
        card_frame.pack()

        # Book Flight Card
        self.create_card(card_frame, "✈️", "Book a Flight", "Reserve your next flight by providing your details and flight information.", "Book Flight", lambda: controller.show_frame("BookingPage"))

        # View Reservations Card
        self.create_card(card_frame, "📋", "View Reservations", "Manage your existing reservations, view details, edit or cancel if needed.", "View Reservations", lambda: controller.show_frame("ReservationsPage"))

    def create_card(self, parent, icon, title, desc, button_text, command):
        card = tk.Frame(parent, bg="white", bd=1, relief="solid", padx=20, pady=20)
        card.pack(side="left", padx=20)

        icon_label = tk.Label(card, text=icon, font=("Helvetica", 30), bg="white")
        icon_label.pack(pady=(0, 10))

        title_label = tk.Label(card, text=title, font=("Helvetica", 13, "bold"), bg="white", fg="#004c77")
        title_label.pack()

        desc_label = tk.Label(card, text=desc, font=("Helvetica", 9), bg="white", wraplength=200, justify="center")
        desc_label.pack(pady=(5, 15))

        btn = tk.Button(card, text=button_text, bg="#007bff", fg="white", relief="flat", command=command)
        btn.pack()
