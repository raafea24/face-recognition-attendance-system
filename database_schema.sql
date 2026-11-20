-- Complete schema for the Face Recognition Attendance System.
-- Select the target database before applying this file.

CREATE TABLE IF NOT EXISTS student (
  Department VARCHAR(100) NOT NULL,
  Course VARCHAR(100) NOT NULL,
  Year VARCHAR(20) NOT NULL,
  Semester VARCHAR(20) NOT NULL,
  Student_id INT UNSIGNED NOT NULL,
  Name VARCHAR(255) NOT NULL,
  Division VARCHAR(50) NOT NULL,
  Roll_No VARCHAR(50) NOT NULL,
  Gender VARCHAR(20) NOT NULL,
  DOB DATE NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Address VARCHAR(500) NOT NULL,
  Teacher VARCHAR(255) NOT NULL,
  PhotoSample VARCHAR(20) NOT NULL DEFAULT 'No',
  PRIMARY KEY (Student_id),
  UNIQUE KEY uniq_student_roll (Roll_No),
  KEY idx_student_name (Name),
  KEY idx_student_department (Department)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS attendance (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  student_id INT UNSIGNED NOT NULL,
  roll_no VARCHAR(50) NOT NULL,
  student_name VARCHAR(255) NOT NULL,
  attendance_date DATE NOT NULL,
  attendance_time TIME NOT NULL,
  status ENUM('Present','Absent','Late') NOT NULL DEFAULT 'Present',
  detection_confidence DOUBLE NOT NULL,
  marked_by VARCHAR(32) NOT NULL DEFAULT 'System',
  recognized_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uniq_student_date (student_id, attendance_date),
  KEY idx_date (attendance_date),
  KEY idx_student (student_id),
  KEY idx_roll (roll_no),
  CONSTRAINT fk_attendance_student
    FOREIGN KEY (student_id) REFERENCES student (Student_id)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
