import psycopg2


def connect_me():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="postgres",
        database="messenger"
    )
    conn.set_session(autocommit=True)
    return conn


if __name__ == "__main__":
    conn = connect_me()
    print("OK")
    conn.close()
