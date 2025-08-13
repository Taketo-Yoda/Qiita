CREATE TABLE lecture_halls (
    id VARCHAR2(36) DEFAULT SYS_GUID() PRIMARY KEY,
    name VARCHAR2(50) NOT NULL,
    capacity NUMBER(4) NOT NULL
);
CREATE TABLE courses (
    id VARCHAR2(36) DEFAULT SYS_GUID() PRIMARY KEY,
    title VARCHAR2(50) NOT NULL,
    lecture_hall_id VARCHAR2(36) NOT NULL,
    FOREIGN KEY (lecture_hall_id) REFERENCES lecture_halls(id)
);
CREATE TABLE enrollments (
    student_id VARCHAR2(36) NOT NULL,
    course_id VARCHAR2(36) NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
