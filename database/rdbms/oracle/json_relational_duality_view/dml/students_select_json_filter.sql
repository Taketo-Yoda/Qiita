SET HEADING ON;
SET LINESIZE 1000;
SET PAGESIZE 10;
SELECT
    JSON {
        'ex_first_name': JSON_VALUE(data, '$.first_name'),
        'ex_last_name': JSON_VALUE(data, '$.last_name'),
        'ex_gpa': JSON_VALUE(data, '$.gpa')
    } AS data
FROM
    dv_students
WHERE
    JSON_VALUE(data, '$.gpa') >= 3.5
ORDER BY
    JSON_VALUE(data, '$.gpa') DESC
;
