from database import get_connection


def register_patient():
    print("\n========== REGISTER PATIENT ==========")

    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    phone = input("Phone: ")
    history = input("Medical history: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO patients
        (name, age, gender, phone, medical_history)
        VALUES (?, ?, ?, ?, ?)
    """, (name, age, gender, phone, history))

    patient_id = cursor.lastrowid

    conn.commit()
    conn.close()

    print("Patient registered successfully.")
    print("Patient ID:", patient_id)


def search_patient():
    print("\n========== SEARCH PATIENT ==========")

    name = input("Enter patient name: ")

    conn = get_connection()
    cursor = conn.cursor()

    # INTENTIONALLY VULNERABLE:
    # SQL Injection vulnerability.
    query = "SELECT * FROM patients WHERE name LIKE '%" + name + "%'"

    try:
        cursor.execute(query)
        patients = cursor.fetchall()

        if not patients:
            print("No patients found.")

        for patient in patients:
            print("\n----------------------")
            print("Patient ID:", patient[0])
            print("Name:", patient[1])
            print("Age:", patient[2])
            print("Gender:", patient[3])
            print("Phone:", patient[4])
            print("Medical History:", patient[5])

    except Exception as error:
        print("Database error:", error)

    conn.close()


def view_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM patients WHERE id = ?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    conn.close()

    if patient:
        print("\n========== PATIENT ==========")
        print("ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Gender:", patient[3])
        print("Phone:", patient[4])
        print("Medical History:", patient[5])
    else:
        print("Patient not found.")