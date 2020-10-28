-- 어린 동물 찾기
SELECT animal_id, name
FROM animal_ins
WHERE NOT intake_condition IN 'Aged'
ORDER BY animal_id;