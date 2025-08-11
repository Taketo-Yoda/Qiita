CREATE OR REPLACE JSON RELATIONAL VIEW dv_students
AS
SELECT
    JSON {
        '_id': s.id,
        'first_name': s.first_name,
        'last_name': s.last_name,
        'major': s.major,
        'gpa': s.gpa
    }
FROM
    students s
WITH UPDATE INSERT DELETE;
