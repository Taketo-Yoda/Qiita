-- Insert initial data into lecture_halls table
INSERT INTO lecture_halls (id, name, capacity) VALUES ('L001', 'Main Auditorium', 300);
INSERT INTO lecture_halls (id, name, capacity) VALUES ('L002', 'Science Lab', 150);
INSERT INTO lecture_halls (id, name, capacity) VALUES ('L003', 'Engineering Workshop', 200);
--
-- Insert initial data into courses table
INSERT INTO courses (id, title, lecture_hall_id) VALUES ('C001', 'Introduction to Computer Science', 'L001');
INSERT INTO courses (id, title, lecture_hall_id) VALUES ('C002', 'Advanced Mathematics', 'L002');
INSERT INTO courses (id, title, lecture_hall_id) VALUES ('C003', 'Physics Fundamentals', 'L003');
INSERT INTO courses (id, title, lecture_hall_id) VALUES ('C004', 'Data Structures and Algorithms', 'L001');
INSERT INTO courses (id, title, lecture_hall_id) VALUES ('C005', 'Thermodynamics', 'L002');
--
-- Insert initial data into enrollments table
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB3896D0482E063020011AC6833', 'C001');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB3896D0482E063020011AC6833', 'C002');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB3896D0482E063020011AC6833', 'C004');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB3896E0482E063020011AC6833', 'C002');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB3896E0482E063020011AC6833', 'C003');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB3896E0482E063020011AC6833', 'C005');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB389710482E063020011AC6833', 'C001');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB389710482E063020011AC6833', 'C003');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB389710482E063020011AC6833', 'C004');
INSERT INTO enrollments (student_id, course_id) VALUES ('3C0F7FB389710482E063020011AC6833', 'C005');
