import os

from database import get_connection


UPLOAD_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "outputs",
    "medical_reports"
)


def upload_report(user):
    print("\n========== UPLOAD REPORT ==========")

    if user["role"] == "patient":
        patient_id = user["patient_id"]
    else:
        patient_id = input("Patient ID: ")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    filename = input("Filename: ")
    description = input("Description: ")
    content = input("Report content: ")

    file_path = os.path.join(UPLOAD_DIR, filename)

    try:
        with open(file_path, "w") as file:
            file.write(content)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO medical_records
            (patient_id, filename, description)
            VALUES (?, ?, ?)
        """, (
            patient_id,
            filename,
            description
        ))

        conn.commit()
        conn.close()

        print("Report uploaded.")

    except Exception as error:
        print("File error:", error)


def view_records(user):
    print("\n========== MEDICAL RECORDS ==========")

    patient_id = input("Enter Patient ID: ")

    # INTENTIONALLY VULNERABLE:
    # No authorization check is performed.
    #
    # A patient logged in as Patient 1 can enter Patient 2
    # and access Patient 2's records.

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM medical_records
        WHERE patient_id = ?
    """, (patient_id,))

    records = cursor.fetchall()

    for record in records:
        print("\n----------------------")
        print("Record ID:", record[0])
        print("Patient ID:", record[1])
        print("Filename:", record[2])
        print("Description:", record[3])

    conn.close()


def download_report(user):
    print("\n========== DOWNLOAD REPORT ==========")

    filename = input("Filename: ")

    # INTENTIONALLY VULNERABLE:
    # The filename is controlled by the user and is not validated.
    file_path = os.path.join(UPLOAD_DIR, filename)

    try:
        with open(file_path, "r") as file:
            print("\n========== REPORT ==========")
            print(file.read())

    except FileNotFoundError:
        print("Report not found.")

    except Exception as error:
        print("Error:", error)