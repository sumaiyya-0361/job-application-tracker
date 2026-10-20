
import sqlite3

DB_NAME = "jobs.db"


def create_table():
    """Create the job applications table if it doesn't exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            job_role TEXT NOT NULL,
            location TEXT,
            status TEXT NOT NULL,
            applied_date TEXT,
            job_link TEXT,
            notes TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_application(company, job_role, location, status,
                    applied_date, job_link, notes):
    """Save a new job application."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO applications
        (company, job_role, location, status, applied_date, job_link, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (company, job_role, location, status,
          applied_date, job_link, notes))

    connection.commit()
    connection.close()


def get_applications():
    """Retrieve all saved job applications."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM applications ORDER BY id DESC")
    applications = cursor.fetchall()

    connection.close()
    return applications


def delete_application(application_id):
    """Delete a job application using its ID."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM applications WHERE id = ?",
        (application_id,)
    )

    connection.commit()
    connection.close()
