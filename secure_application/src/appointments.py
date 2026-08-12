from database import get_connection


def book_appointment(user):
    print("\n========== BOOK APPOINTMENT ==========")

    if user["role"] == "patient":
        patient_id = user["patient_id"]
    else:
        patient_id = input("Patient ID: ")

    doctor = input("Doctor: ")
    date = input("Date: ")
    reason = input("Reason: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO appointments
        (patient_id, doctor, appointment_date, reason)
        VALUES (?, ?, ?, ?)
    """, (patient_id, doctor, date, reason))

    conn.commit()
    conn.close()

    print("Appointment booked successfully.")


def view_appointments(user):
    print("\n========== APPOINTMENTS ==========")

    conn = get_connection()
    cursor = conn.cursor()

    if user["role"] == "patient":
        cursor.execute("""
            SELECT * FROM appointments
            WHERE patient_id = ?
        """, (user["patient_id"],))
    else:
        cursor.execute("SELECT * FROM appointments")

    appointments = cursor.fetchall()

    for appointment in appointments:
        print("\n----------------------")
        print("Appointment ID:", appointment[0])
        print("Patient ID:", appointment[1])
        print("Doctor:", appointment[2])
        print("Date:", appointment[3])
        print("Reason:", appointment[4])

    conn.close()