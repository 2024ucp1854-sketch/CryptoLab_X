from database import initialize_database
from auth import login

from patients import (
    register_patient,
    search_patient,
    view_patient
)

from appointments import (
    book_appointment,
    view_appointments
)

from prescriptions import (
    add_prescription,
    view_prescriptions
)

from billing import (
    create_bill,
    view_bills
)

from medical_records import (
    upload_report,
    view_records,
    download_report
)


def admin_menu(user):

    while True:

        print("\n========== ADMIN ==========")
        print("1. Register Patient")
        print("2. Search Patient")
        print("3. View Patient")
        print("4. Book Appointment")
        print("5. View Appointments")
        print("6. Add Prescription")
        print("7. View Prescriptions")
        print("8. Create Bill")
        print("9. View Bills")
        print("10. Upload Medical Report")
        print("11. View Medical Records")
        print("12. Download Medical Report")
        print("13. Logout")

        choice = input("Choice: ")

        if choice == "1":
            register_patient()

        elif choice == "2":
            search_patient()

        elif choice == "3":
            patient_id = input("Patient ID: ")
            view_patient(patient_id)

        elif choice == "4":
            book_appointment(user)

        elif choice == "5":
            view_appointments(user)

        elif choice == "6":
            add_prescription()

        elif choice == "7":
            view_prescriptions(user)

        elif choice == "8":
            create_bill()

        elif choice == "9":
            view_bills(user)

        elif choice == "10":
            upload_report(user)

        elif choice == "11":
            view_records(user)

        elif choice == "12":
            download_report(user)

        elif choice == "13":
            break

        else:
            print("Invalid choice.")


def doctor_menu(user):

    while True:

        print("\n========== DOCTOR ==========")
        print("1. Search Patient")
        print("2. View Appointments")
        print("3. Add Prescription")
        print("4. View Prescriptions")
        print("5. Upload Medical Report")
        print("6. View Medical Records")
        print("7. Logout")

        choice = input("Choice: ")

        if choice == "1":
            search_patient()

        elif choice == "2":
            view_appointments(user)

        elif choice == "3":
            add_prescription()

        elif choice == "4":
            view_prescriptions(user)

        elif choice == "5":
            upload_report(user)

        elif choice == "6":
            view_records(user)

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


def patient_menu(user):

    while True:

        print("\n========== PATIENT ==========")
        print("1. View Profile")
        print("2. Book Appointment")
        print("3. View Appointments")
        print("4. View Prescriptions")
        print("5. View Bills")
        print("6. View Medical Records")
        print("7. Upload Medical Report")
        print("8. Download Medical Report")
        print("9. Logout")

        choice = input("Choice: ")

        if choice == "1":
            view_patient(user["patient_id"])

        elif choice == "2":
            book_appointment(user)

        elif choice == "3":
            view_appointments(user)

        elif choice == "4":
            view_prescriptions(user)

        elif choice == "5":
            view_bills(user)

        elif choice == "6":
            view_records(user)

        elif choice == "7":
            upload_report(user)

        elif choice == "8":
            download_report(user)

        elif choice == "9":
            break

        else:
            print("Invalid choice.")


def main():

    initialize_database()

    print("\n======================================")
    print("      HOSPITAL MANAGEMENT SYSTEM")
    print("======================================")

    while True:

        print("\n1. Login")
        print("2. Exit")

        choice = input("Choice: ")

        if choice == "1":

            user = login()

            if user:

                if user["role"] == "admin":
                    admin_menu(user)

                elif user["role"] == "doctor":
                    doctor_menu(user)

                elif user["role"] == "patient":
                    patient_menu(user)

        elif choice == "2":

            print("Thank you for using Hospital Management System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()