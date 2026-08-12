from database import get_connection


def create_bill():
    print("\n========== CREATE BILL ==========")

    patient_id = input("Patient ID: ")
    amount = input("Amount: ")
    description = input("Description: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bills
        (patient_id, amount, description, status)
        VALUES (?, ?, ?, ?)
    """, (
        patient_id,
        amount,
        description,
        "Pending"
    ))

    conn.commit()
    conn.close()

    print("Bill created.")


def view_bills(user):
    conn = get_connection()
    cursor = conn.cursor()

    if user["role"] == "patient":
        cursor.execute("""
            SELECT * FROM bills
            WHERE patient_id = ?
        """, (user["patient_id"],))
    else:
        cursor.execute("SELECT * FROM bills")

    bills = cursor.fetchall()

    print("\n========== BILLS ==========")

    for bill in bills:
        print("\n----------------------")
        print("Bill ID:", bill[0])
        print("Patient ID:", bill[1])
        print("Amount:", bill[2])
        print("Description:", bill[3])
        print("Status:", bill[4])

    conn.close()