-- Insert initial data into lecture_halls table
INSERT INTO lecture_halls
    (id, name, capacity)
VALUES
    ('L001', 'Main Auditorium', 300),
    ('L002', 'Science Lab', 150),
    ('L003', 'Engineering Workshop', 200)
;
--
-- Insert initial data into courses table
INSERT INTO courses
    (id, title, lecture_hall_id)
VALUES
    ('C001', 'Introduction to Computer Science', 'L001'),
    ('C002', 'Advanced Mathematics', 'L002'),
    ('C003', 'Physics Fundamentals', 'L003'),
    ('C004', 'Data Structures and Algorithms', 'L001'),
    ('C005', 'Thermodynamics', 'L002')
;
--
-- Insert initial data into enrollments table
INSERT INTO enrollments
    (student_id, course_id)
VALUES
    ('3C3DCB1CEAEC06A3E063020011ACD2F1', 'C001'),
    ('3C3DCB1CEAEC06A3E063020011ACD2F1', 'C002'),
    ('3C3DCB1CEAEC06A3E063020011ACD2F1', 'C004'),
    ('3C3DCB1CEAEE06A3E063020011ACD2F1', 'C002'),
    ('3C3DCB1CEAEE06A3E063020011ACD2F1', 'C003'),
    ('3C3DCB1CEAEE06A3E063020011ACD2F1', 'C005'),
    ('3C3DCB1CEAF006A3E063020011ACD2F1', 'C001'),
    ('3C3DCB1CEAF006A3E063020011ACD2F1', 'C003'),
    ('3C3DCB1CEAF006A3E063020011ACD2F1', 'C004'),
    ('3C3DCB1CEAF006A3E063020011ACD2F1', 'C005')
;
