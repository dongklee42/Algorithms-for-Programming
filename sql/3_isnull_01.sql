-- 이름이 있는 동물의 아이디
SELECT animal_id
FROM animal_ins
WHERE name IS NOT NULL
ORDER BY animal_id;