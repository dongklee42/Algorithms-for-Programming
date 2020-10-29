-- 입양 시각 구하기 2.
SELECT A.HOUR AS HOUR, COUNT(B.HOUR) AS COUNT 
FROM (
        SELECT ROWNUM - 1 AS HOUR
        FROM dual
        CONNECT BY LEVEL <= 24
     ) A
     LEFT OUTER JOIN
     (
        SELECT EXTRACT(HOUR FROM CAST(datetime AS TIMESTAMP)) AS HOUR
        FROM animal_outs
     ) B
ON A.HOUR = B.HOUR
GROUP BY A.HOUR
ORDER BY A.HOUR;