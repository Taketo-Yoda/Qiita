UPDATE dv_students
SET data = ('{
    "_id": "3C0F7FB3896D0482E063020011AC6833",
    "first_name": "Adam",
    "last_name": "Jones",
    "major": "Computer Science",
    "gpa": 4.5
}')
WHERE JSON_VALUE(data, '$._id') = '3C0F7FB3896D0482E063020011AC6833'
;