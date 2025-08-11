CREATE TABLE students (
    id VARCHAR2(32) DEFAULT SYS_GUID() PRIMARY KEY,
    first_name VARCHAR2(50) NOT NULL,
    last_name VARCHAR2(50) NOT NULL,
    major VARCHAR2(50) NOT NULL,
    gpa NUMBER(3, 2)
);
