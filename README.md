# Face Recognition Attendance System

A desktop attendance application that combines OpenCV face recognition, a Tkinter workflow, a modern PyQt5 web-based shell, and MySQL-backed student and attendance records.

## Features

- Student record management with input validation
- Webcam-based face sample capture and LBPH model training
- Real-time recognition with automatic, once-per-day attendance marking
- Attendance search, filtering, deletion, and CSV export
- Classic Tkinter dashboard and an optional PyQt5/HTML/CSS dashboard
- MySQL schema with student and attendance tables

## Privacy

Facial samples, trained classifiers, database contents, exported attendance files, local credentials, and logs are intentionally excluded from version control. Obtain informed consent before collecting biometric data and follow the privacy and retention laws that apply in your jurisdiction.

## Requirements

- Python 3.9 or newer
- MySQL Server 8.x or a compatible MySQL installation
- A webcam for sample capture and recognition
- Windows for the current desktop integration (`os.startfile` is used by gallery actions)

## Installation

```powershell
git clone https://github.com/raafea24/face-recognition-attendance-system.git
cd face-recognition-attendance-system
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Database setup

Set the connection values for your local MySQL instance. `DB_PASSWORD` defaults to an empty string if it is not set; no password is stored in the repository.

```powershell
$env:DB_HOST = "127.0.0.1"
$env:DB_PORT = "3306"
$env:DB_USER = "root"
$env:DB_PASSWORD = "your-local-password"
$env:DB_NAME = "FaceRecognitionSystem"
python create_attendance_table.py
```

The setup command creates the database when necessary and applies [database_schema.sql](database_schema.sql). To verify connectivity later, run:

```powershell
python db_check.py
```

## Run the application

Classic Tkinter interface:

```powershell
python main.py
```

Modern PyQt5 interface:

```powershell
python modern_main.py
```

Use the Student Details module to add records and capture face samples, then use Train Data to generate the local `classifier.xml` model. The ignored `face_data/` directory is created automatically when needed.

## Dataset naming

Training IDs are parsed from the second dot-separated token in each filename. The generated format is `user.<student_id>.<sample_number>.jpg`, for example `user.1.25.jpg`. Files that do not match this structure are skipped.

For useful training data, capture varied lighting, angles, and expressions while keeping the face visible and unobstructed. The current LBPH acceptance distance is configured in `face_recognition.py`; lower values represent closer matches.

## Project structure

```text
backend/                 PyQt-to-Tkinter bridge and launch helpers
frontend/                HTML, CSS, JavaScript, and safe UI assets
APP Pictures/            Tkinter interface assets
database_schema.sql      Complete MySQL schema
attendance_schema.sql    Standalone attendance table schema
student.py               Student management and sample capture
train.py                 LBPH model training
face_recognition.py      Recognition and attendance integration
attendance.py            Attendance management interface
main.py                  Classic Tkinter entry point
modern_main.py           Modern PyQt5 entry point
```

