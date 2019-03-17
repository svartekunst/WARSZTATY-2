from models.user import User
from db import connect_me


if __name__ == "__main__":
    conn = connect_me()
    cur = conn.cursor()

    u1 = User()
    u1.email = "pythonmaster@example.com"
    u1.username = "pythonmaster"
    u1.set_password("12345", "abc")
    u1.save_to_db(cur)

    u2 = User()
    u2.email = "harry@example.com"
    u2.username = "griffindorboy"
    u2.set_password("54321", "def")
    u2.save_to_db(cur)

    us = User.load_all_users(cur)
    for u in us:
        print(u.username)

    cur.close()
    conn.close()
    print("OK!")
