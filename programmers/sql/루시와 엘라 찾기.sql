"""
루시와 엘라 찾기
https://programmers.co.kr/learn/courses/30/lessons/59046
"""
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS 
WHERE NAME = 'Ella' or NAME = 'Lucy' or NAME = 'Pickle' or NAME = 'Rogan' 
or NAME = 'Sabrina' or NAME = 'Mitty' ORDER BY ANIMAL_ID;



/*
select animal_id, name, sex_upon_intake
from animal_ins
where name in ('Lucy', 'Ella', 'Pickle', 'Sabrina', 'Mitty')
order by animal_id
*/