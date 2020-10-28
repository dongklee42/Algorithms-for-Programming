-- 최대값 구하기
SELECT datetime AS 시간
FROM (
        SELECT datetime
        FROM animal_ins
        ORDER BY datetime DESC
     )
WHERE ROWNUM = 1;