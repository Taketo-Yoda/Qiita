CREATE TABLE students (
    id VARCHAR2(36) DEFAULT SYS_GUID() PRIMARY KEY,
    first_name VARCHAR2(20) NOT NULL,
    last_name VARCHAR2(20) NOT NULL,
    major VARCHAR2(20) NOT NULL,
    gpa NUMBER(3, 2)
);
