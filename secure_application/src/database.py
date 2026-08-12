import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "outputs", "hospital.db")


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            patient_id INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            phone TEXT,
            medical_history TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor TEXT,
            appointment_date TEXT,
            reason TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prescriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor TEXT,
            medicine TEXT,
            dosage TEXT,
            instructions TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            amount REAL,
            description TEXT,
            status TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            filename TEXT,
            description TEXT
        )
    """)

    # Create demo accounts only when database is empty
    cursor.execute("SELECT COUNT(*) FROM users")

    if cursor.fetchone()[0] == 0:

        cursor.execute("""
            INSERT INTO users
            (username, password, role, patient_id)
            VALUES (?, ?, ?, ?)
        """, ("admin", "admin123", "admin", None))

        cursor.execute("""
            INSERT INTO users
            (username, password, role, patient_id)
            VALUES (?, ?, ?, ?)
        """, ("doctor", "doctor123", "doctor", None))

        cursor.execute("""
            INSERT INTO patients
            (name, age, gender, phone, medical_history)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "Rahul Sharma",
            25,
            "Male",
            "9876543210",
            "No major medical history"
        ))

        patient_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO users
            (username, password, role, patient_id)
            VALUES (?, ?, ?, ?)
        """, (
            "patient",
            "patient123",
            "patient",
            patient_id
        ))

    conn.commit()
    conn.close()