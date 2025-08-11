CREATE OR REPLACE JSON RELATIONAL VIEW dv_students_with_courses
AS
SELECT
    JSON {
        '_id': s.id,
        'first_name': s.first_name,
        'last_name': s.last_name,
        'major': s.major,
        'gpa': s.gpa,
        'enrollments' : [
            SELECT
                JSON {
                    'student_id': e.student_id,
                    'course_id': e.course_id,
                    'course' : (
                        SELECT
                            JSON {
                                '_id': c.id,
                                'title': c.title,
                                'lecture_hall_id': c.lecture_hall_id
                            }
                        FROM
                            courses c
                        WHERE
                            c.id = e.course_id
                    )
                }
            FROM
                enrollments e
            WHERE
                e.student_id = s.id
        ]
    }
FROM
    students s
;
