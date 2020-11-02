-- 코드를 입력하세요
SELECT I.animal_id AS ANIMAL_ID, I.name AS NAME
FROM animal_ins I
     INNER JOIN
     animal_outs O
ON I.animal_id = O.animal_id
WHERE I.datetime > O.datetime
ORDER BY I.datetime;