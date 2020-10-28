-- 코드를 입력하세요
SELECT name, COUNT(name) AS count
FROM animal_ins
WHERE name IS NOT NULL
HAVING COUNT(name) > 1
GROUP BY name
ORDER BY name;