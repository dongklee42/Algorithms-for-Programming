-- 오랜기간 보호한 동물(1)
SELECT *
FROM (
    SELECT I.name, I.datetime
    FROM animal_ins I
        LEFT OUTER JOIN
         animal_outs O
    ON I.animal_id = O.animal_id
    WHERE O.datetime IS NULL
    ORDER BY I.datetime
    )
WHERE ROWNUM <= 3;
