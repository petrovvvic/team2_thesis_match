-- ============================================================
-- Thesis Match - SQLite Database Schema
-- Full-Stack Web Development Project
-- Database: SQLite
-- Purpose: Creates all tables, constraints and indexes
-- ============================================================

-- Important:
-- Foreign key checks must be enabled for each SQLite connection.
-- This PRAGMA is also included here for manual testing with sqlite3.
PRAGMA foreign_keys = ON;

-- ============================================================
-- Drop existing tables
-- Useful during development when rebuilding the database.
-- Tables are dropped in reverse dependency order.
-- ============================================================

PRAGMA foreign_keys = OFF;

DROP TABLE IF EXISTS request_status_history;
DROP TABLE IF EXISTS attachments;
DROP TABLE IF EXISTS request_messages;
DROP TABLE IF EXISTS supervision_requests;
DROP TABLE IF EXISTS thesis_topics;
DROP TABLE IF EXISTS professor_profiles;
DROP TABLE IF EXISTS student_profiles;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS degree_programs;
DROP TABLE IF EXISTS faculties;

PRAGMA foreign_keys = ON;

-- ============================================================
-- 1. faculties
-- Official HWR faculties used as reference data.
-- ============================================================

CREATE TABLE faculties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- 2. degree_programs
-- Study programs assigned to exactly one faculty.
-- ============================================================

CREATE TABLE degree_programs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    degree TEXT NOT NULL,
    study_format TEXT,
    is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1)),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (faculty_id)
        REFERENCES faculties(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    UNIQUE (faculty_id, name, degree, study_format),
    UNIQUE (id, faculty_id)
);

-- ============================================================
-- 3. users
-- Central table for login, role and account status.
-- Passwords must be stored as hashes, never as plain text.
-- ============================================================

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE COLLATE NOCASE,
    password_hash TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,

    role TEXT NOT NULL CHECK (
        role IN ('student', 'professor', 'admin')
    ),

    account_status TEXT NOT NULL DEFAULT 'active' CHECK (
        account_status IN ('active', 'blocked')
    ),

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- 4. student_profiles
-- Additional data for users with role = student.
-- ============================================================

CREATE TABLE student_profiles (
    user_id INTEGER PRIMARY KEY,
    matriculation_number TEXT NOT NULL UNIQUE,
    faculty_id INTEGER NOT NULL,
    degree_program_id INTEGER NOT NULL,
    semester INTEGER CHECK (semester IS NULL OR semester >= 1),
    study_focus TEXT,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (faculty_id)
        REFERENCES faculties(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY (degree_program_id)
        REFERENCES degree_programs(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    -- Ensures that the selected degree program belongs to the selected faculty.
    FOREIGN KEY (degree_program_id, faculty_id)
        REFERENCES degree_programs(id, faculty_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ============================================================
-- 5. professor_profiles
-- Additional data for users with role = professor.
-- ============================================================

CREATE TABLE professor_profiles (
    user_id INTEGER PRIMARY KEY,
    faculty_id INTEGER NOT NULL,
    title TEXT,
    research_areas TEXT,
    requirements TEXT,
    max_supervisions INTEGER NOT NULL DEFAULT 5 CHECK (max_supervisions >= 0),
    accepting_requests INTEGER NOT NULL DEFAULT 1 CHECK (accepting_requests IN (0, 1)),
    office TEXT,
    consultation_hours TEXT,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (faculty_id)
        REFERENCES faculties(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ============================================================
-- 6. thesis_topics
-- Thesis topic suggestions created by professors.
-- ============================================================

CREATE TABLE thesis_topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    professor_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    requirements TEXT,
    topic_area TEXT NOT NULL,

    status TEXT NOT NULL DEFAULT 'open' CHECK (
        status IN ('open', 'archived')
    ),

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (professor_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ============================================================
-- 7. supervision_requests
-- Central table for supervision requests from students to professors.
-- ============================================================

CREATE TABLE supervision_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    professor_id INTEGER NOT NULL,
    topic_id INTEGER,

    proposed_title TEXT NOT NULL,
    short_description TEXT NOT NULL,
    motivation TEXT,
    preferred_period TEXT NOT NULL,

    status TEXT NOT NULL DEFAULT 'submitted' CHECK (
        status IN (
            'submitted',
            'in_review',
            'needs_info',
            'accepted',
            'rejected',
            'withdrawn'
        )
    ),

    professor_response TEXT,

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (student_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY (professor_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    FOREIGN KEY (topic_id)
        REFERENCES thesis_topics(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL,

    CHECK (student_id <> professor_id)
);

-- ============================================================
-- 8. request_messages
-- Message history for a specific supervision request.
-- ============================================================

CREATE TABLE request_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    sender_id INTEGER NOT NULL,
    message_text TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (request_id)
        REFERENCES supervision_requests(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (sender_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    UNIQUE (id, request_id)
);

-- ============================================================
-- 9. attachments
-- PDF attachments uploaded during request creation or message exchange.
-- Files are stored in the upload folder.
-- This table only stores metadata.
-- ============================================================

CREATE TABLE attachments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    message_id INTEGER,
    uploaded_by INTEGER NOT NULL,

    attachment_context TEXT NOT NULL CHECK (
        attachment_context IN ('initial', 'message')
    ),

    original_filename TEXT NOT NULL,
    storage_path TEXT NOT NULL UNIQUE,
    mime_type TEXT NOT NULL DEFAULT 'application/pdf',
    file_size INTEGER NOT NULL CHECK (file_size > 0),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (request_id)
        REFERENCES supervision_requests(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (uploaded_by)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    -- Ensures that message attachments belong to a message of the same request.
    FOREIGN KEY (message_id, request_id)
        REFERENCES request_messages(id, request_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    -- initial attachments belong directly to the request and have no message_id.
    -- message attachments must belong to a concrete message.
    CHECK (
        (attachment_context = 'initial' AND message_id IS NULL)
        OR
        (attachment_context = 'message' AND message_id IS NOT NULL)
    ),

    -- MVP rule: only PDF metadata is accepted in the database.
    -- File extension and file size limit are additionally checked in Flask.
    CHECK (mime_type = 'application/pdf')
);

-- ============================================================
-- 10. request_status_history
-- Audit trail for request status changes.
-- ============================================================

CREATE TABLE request_status_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,

    old_status TEXT CHECK (
        old_status IS NULL OR old_status IN (
            'submitted',
            'in_review',
            'needs_info',
            'accepted',
            'rejected',
            'withdrawn'
        )
    ),

    new_status TEXT NOT NULL CHECK (
        new_status IN (
            'submitted',
            'in_review',
            'needs_info',
            'accepted',
            'rejected',
            'withdrawn'
        )
    ),

    changed_by INTEGER NOT NULL,
    comment TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (request_id)
        REFERENCES supervision_requests(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (changed_by)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ============================================================
-- Indexes
-- These indexes support common searches, dashboards and filters.
-- ============================================================

CREATE INDEX idx_users_role
ON users(role);

CREATE INDEX idx_users_account_status
ON users(account_status);

CREATE INDEX idx_degree_programs_faculty
ON degree_programs(faculty_id);

CREATE INDEX idx_student_profiles_faculty
ON student_profiles(faculty_id);

CREATE INDEX idx_student_profiles_degree_program
ON student_profiles(degree_program_id);

CREATE INDEX idx_professor_profiles_faculty
ON professor_profiles(faculty_id);

CREATE INDEX idx_professor_profiles_accepting
ON professor_profiles(accepting_requests);

CREATE INDEX idx_thesis_topics_professor
ON thesis_topics(professor_id);

CREATE INDEX idx_thesis_topics_status
ON thesis_topics(status);

CREATE INDEX idx_thesis_topics_topic_area
ON thesis_topics(topic_area);

CREATE INDEX idx_requests_student
ON supervision_requests(student_id);

CREATE INDEX idx_requests_professor
ON supervision_requests(professor_id);

CREATE INDEX idx_requests_topic
ON supervision_requests(topic_id);

CREATE INDEX idx_requests_status
ON supervision_requests(status);

CREATE INDEX idx_requests_created_at
ON supervision_requests(created_at);

CREATE INDEX idx_messages_request
ON request_messages(request_id);

CREATE INDEX idx_messages_sender
ON request_messages(sender_id);

CREATE INDEX idx_attachments_request
ON attachments(request_id);

CREATE INDEX idx_attachments_message
ON attachments(message_id);

CREATE INDEX idx_attachments_uploaded_by
ON attachments(uploaded_by);

CREATE INDEX idx_attachments_context
ON attachments(attachment_context);

CREATE INDEX idx_history_request
ON request_status_history(request_id);

CREATE INDEX idx_history_changed_by
ON request_status_history(changed_by);

CREATE INDEX idx_history_created_at
ON request_status_history(created_at);

-- ============================================================
-- End of schema.sql
-- ============================================================
