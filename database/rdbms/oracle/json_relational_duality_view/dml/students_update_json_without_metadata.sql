UPDATE dv_students
SET data = ('{
    "_id": "3C3DCB1CEAEC06A3E063020011ACD2F1",
    "first_name": "Adam",
    "last_name": "Jones",
    "major": "Computer Science",
    "gpa": 4.5
}')
WHERE JSON_VALUE(data, '$._id') = '3C3DCB1CEAEC06A3E063020011ACD2F1'
;