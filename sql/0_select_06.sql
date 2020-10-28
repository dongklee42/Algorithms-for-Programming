-- 상위 n개의 레코드
SELECT *
FROM (
        SELECT name
        FROM animal_ins
        ORDER BY datetime
     )
WHERE ROWNUM = 1;