import sqlite3

DB_NAME = 'flights.db'

def connect():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            flight_number TEXT,
            departure TEXT,
            destination TEXT,
            date TEXT,
            seat_number TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def get_reservations():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations')
    rows = cursor.fetchall()
    conn.close()

    # Return list of dicts for easier use
    return [
        {
            "id": row[0],
            "name": row[1],
            "flight_number": row[2],
            "departure": row[3],
            "destination": row[4],
            "date": row[5],
            "seat_number": row[6]
        } for row in rows
    ]

def update_reservation(res_id, name, flight_number, departure, destination, date, seat_number):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    ''', (name, flight_number, departure, destination, date, seat_number, res_id))
    conn.commit()
    conn.close()

def delete_reservation(reservation_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
    conn.commit()
    conn.close()
