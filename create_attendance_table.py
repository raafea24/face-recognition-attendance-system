"""
Create the application tables in the configured MySQL database using database_schema.sql.

- Uses mysql-connector-python
- Reads the SQL file and executes statements
- Verifies by SHOW TABLES and DESCRIBE attendance
- Configuration is read from the DB_* environment variables documented in README.md.
"""
import os
import pathlib
import re
import sys
import mysql.connector

from db_config import DEFAULT_DATABASE, get_db_config

DB_NAME = os.getenv("DB_NAME", DEFAULT_DATABASE)

ROOT = pathlib.Path(__file__).parent
SCHEMA_PATH = ROOT / "database_schema.sql"


def main():
    print("== Creating attendance table ==")
    if not SCHEMA_PATH.exists():
        print("Schema file not found:", SCHEMA_PATH)
        sys.exit(1)
    if not re.fullmatch(r"[A-Za-z0-9_]+", DB_NAME):
        print("DB_NAME may contain only letters, numbers, and underscores.")
        sys.exit(1)

    # Connect to server first to ensure DB exists
    try:
        conn = mysql.connector.connect(**get_db_config(include_database=False))
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
        conn.commit()
        cur.close(); conn.close()
        print(f"Database ensured: {DB_NAME}")
    except Exception as e:
        print("Error ensuring database:", e)
        sys.exit(1)

    sql_text = SCHEMA_PATH.read_text(encoding="utf-8")
    # Strip out MySQL line comments to avoid connector issues
    cleaned_lines = []
    for line in sql_text.splitlines():
        l = line.strip('\n')
        if l.strip().startswith('--'):
            continue
        cleaned_lines.append(l)
    cleaned_sql = '\n'.join(cleaned_lines)
    statements = [s.strip() for s in cleaned_sql.split(';') if s.strip()]

    try:
        conn = mysql.connector.connect(**get_db_config())
        cur = conn.cursor()
        for stmt in statements:
            cur.execute(stmt)
        conn.commit()
        print("Schema applied.")

        cur.execute("SHOW TABLES")
        print("Tables:", [r[0] for r in cur.fetchall()])
        cur.execute("DESCRIBE attendance")
        print("attendance columns:")
        for row in cur.fetchall():
            print(" -", row[0], row[1])
        cur.close(); conn.close()
        print("Done: attendance table ready.")
    except Exception as e:
        print("Error applying schema:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
