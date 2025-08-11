SET HEADING OFF;
SELECT
    JSON_SERIALIZE(data PRETTY)
FROM
    dv_students_with_courses
WHERE
    JSON_VALUE(data, '$.first_name') = 'Adam'
;
