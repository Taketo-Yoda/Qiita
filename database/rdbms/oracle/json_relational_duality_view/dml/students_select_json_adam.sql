SELECT
    JSON_SERIALIZE(data PRETTY) AS data
FROM
    dv_students
WHERE
    JSON_VALUE(data, '$.first_name') = 'Adam'
;
