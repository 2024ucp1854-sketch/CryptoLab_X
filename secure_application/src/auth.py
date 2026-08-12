from database import get_connection


def login():
    print("\n========== LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    conn = get_connection()
    cursor = conn.cursor()

    # INTENTIONALLY VULNERABLE:
    # Directly concatenating user input into SQL.
    query = (
        "SELECT id, username, role, patient_id "
        "FROM users "
        "WHERE username = '" + username +
        "' AND password = '" + password + "'"
    )

    try:
        cursor.execute(query)
        user = cursor.fetchone()
    except Exception as error:
        print("Database error:", error)
        conn.close()
        return None

    conn.close()

    if user:
        print("Login successful.")
        print("Welcome,", user[1])

        return {
            "id": user[0],
            "username": user[1],
            "role": user[2],
            "patient_id": user[3]
        }

    print("Invalid username or password.")
    return None