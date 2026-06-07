import sqlite3


def get_connection():
    return sqlite3.connect("scanner.db")


def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        risk TEXT,
        scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_scan(target, risk):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO scans(target, risk)
        VALUES (?, ?)
        """,
        (target, risk)
    )

    conn.commit()
    conn.close()


def get_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM scans ORDER BY id DESC"
    )

    data = cursor.fetchall()

    conn.close()

    return data