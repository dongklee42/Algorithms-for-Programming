-- 보호소에서 중성화한 동물
SELECT animal_id, animal_type, name
FROM (
    SELECT O.animal_id, O.animal_type, O.name, O.sex_upon_outcome
    FROM animal_ins I
        LEFT OUTER JOIN
         animal_outs O
    ON I.animal_id = O.animal_id
    WHERE I.sex_upon_intake LIKE 'Intact%'
     )
WHERE sex_upon_outcome NOT LIKE 'Intact%'
ORDER BY animal_id
;
