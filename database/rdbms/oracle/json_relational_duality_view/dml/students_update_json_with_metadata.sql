UPDATE dv_students
SET data = ('{
    "_id": "3C3DCB1CEAEC06A3E063020011ACD2F1",
    "_metadata" : {
        "etag": "E73B0F8ADA21C8F12747AA7FD2019E7C"
    },
    "first_name": "Adam",
    "last_name": "Jones",
    "major": "Computer Science",
    "gpa": 4.2
}')
WHERE JSON_VALUE(data, '$._id') = '3C3DCB1CEAEC06A3E063020011ACD2F1'
;