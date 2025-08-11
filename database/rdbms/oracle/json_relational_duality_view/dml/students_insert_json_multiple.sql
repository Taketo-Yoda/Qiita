/*
    This query will cause an error,
    but the purpose is to check the returned error.
*/
INSERT INTO dv_students VALUES (
    '[
        {
            "first_name": "Emily",
            "last_name": "Harris",
            "major": "Biology",
            "gpa": 4.1
        },
        {
            "first_name": "Frank",
            "last_name": "Johnson",
            "major": "Chemistry",
            "gpa": 3.9
        }
    ]'
);
