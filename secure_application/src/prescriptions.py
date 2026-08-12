from database import get_connection


def add_prescription():
    print("\n========== ADD PRESCRIPTION ==========")

    patient_id = input("Patient ID: ")
    doctor = input("Doctor: ")
    medicine = input("Medicine: ")
    dosage = input("Dosage: ")
    instructions = input("Instructions: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prescriptions
        (patient_id, doctor, medicine, dosage, instructions)
        VALUES (?, ?, ?, ?, ?)
    """, (
        patient_id,
        doctor,
        medicine,
        dosage,
        instructions
    ))

    conn.commit()
    conn.close()

    print("Prescription added.")


def view_prescriptions(user):
    conn = get_connection()
    cursor = conn.cursor()

    if user["role"] == "patient":
        cursor.execute("""
            SELECT * FROM prescriptions
            WHERE patient_id = ?
        """, (user["patient_id"],))
    else:
        cursor.execute("SELECT * FROM prescriptions")

    prescriptions = cursor.fetchall()

    print("\n========== PRESCRIPTIONS ==========")

    for prescription in prescriptions:
        print("\n----------------------")
        print("Prescription ID:", prescription[0])
        print("Patient ID:", prescription[1])
        print("Doctor:", prescription[2])
        print("Medicine:", prescription[3])
        print("Dosage:", prescription[4])
        print("Instructions:", prescription[5])

    conn.close()