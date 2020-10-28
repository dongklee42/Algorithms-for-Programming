-- 고양이와 개의 마리 수 구하기
SELECT animal_type, COUNT(animal_type) AS count
FROM animal_ins
WHERE animal_type = 'Cat' or animal_type = 'Dog'
GROUP BY animal_type
ORDER BY animal_type ASC;