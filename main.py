import tkinter as tk
from database import initialize_db
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window icon
        self.iconbitmap(r'D:\University\Acadmic courses\Sprints\SE x Python\Project\flight_reservation_app\assets\airplane-takeoff-icon-plane-departure-600nw-2499578157.ico')

        self.title("Flight Reservation System")
        self.geometry("1366x768")
        self.resizable(False, False)

        initialize_db()

        # Navigation Bar (shared)
        nav_frame = tk.Frame(self, bg="#004c77", height=40)
        nav_frame.pack(side="top", fill="x")

        self.btn_home = tk.Button(nav_frame, text="Home", fg="white", bg="#004c77", relief="flat",
                             command=lambda: self.show_frame("HomePage"))
        self.btn_home.pack(side="left", padx=10, pady=5)

        self.btn_booking = tk.Button(nav_frame, text="Book Flight", fg="white", bg="#004c77", relief="flat",
                                command=lambda: self.show_frame("BookingPage"))
        self.btn_booking.pack(side="left", padx=10, pady=5)

        self.btn_reservations = tk.Button(nav_frame, text="Reservations", fg="white", bg="#004c77", relief="flat",
                                     command=lambda: self.show_frame("ReservationsPage"))
        self.btn_reservations.pack(side="left", padx=10, pady=5)

        self.btn_edit = tk.Button(nav_frame, text="Edit Reservation", fg="white", bg="#004c77", relief="flat",
                             command=lambda: self.show_frame("EditReservationPage"))
        self.btn_edit.pack(side="left", padx=10, pady=5)

        # Spacer to push name_label to the right
        spacer = tk.Label(nav_frame, text="", bg="#004c77")
        spacer.pack(side="left", expand=True)

        # Your name label right aligned
        name_label = tk.Label(nav_frame, text="~pant0x", fg="white", bg="#004c77", font=("Courier", 12, "bold"))
        name_label.pack(side="right", padx=10, pady=5)

        # Container for pages below nav
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for Page in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = Page.__name__
            frame = Page(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        # Update nav button backgrounds for active page
        active_bg = "#006699"
        default_bg = "#004c77"

        self.btn_home.config(bg=active_bg if page_name == "HomePage" else default_bg)
        self.btn_booking.config(bg=active_bg if page_name == "BookingPage" else default_bg)
        self.btn_reservations.config(bg=active_bg if page_name == "ReservationsPage" else default_bg)
        self.btn_edit.config(bg=active_bg if page_name == "EditReservationPage" else default_bg)

        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
