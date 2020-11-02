-- 없어진 기록 찾기
SELECT O.animal_id AS ANIMAL_ID, O.name AS NAME
FROM animal_outs O
     LEFT OUTER JOIN
     animal_ins I
ON O.animal_id = I.animal_id
WHERE I.animal_id IS NULL
ORDER BY O.animal_id;