UPDATE dv_students
SET data = ('{
    "_id": "3C0F7FB3896D0482E063020011AC6833",
    "_metadata" : {
        "etag": "3973014F8B5D930A08C84F91039ED007"
    },
    "first_name": "Adam",
    "last_name": "Jones",
    "major": "Computer Science",
    "gpa": 4.2
}')
WHERE JSON_VALUE(data, '$._id') = '3C0F7FB3896D0482E063020011AC6833'
;